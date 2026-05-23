r"""Smoke tests for every public and (optionally) private gw2-api-py endpoint.

Run:
    .\.venv\Scripts\python.exe test.py

The script walks the live API object tree, calling every endpoint that takes
no arguments. Endpoints that would alter or generate secrets (e.g.
``createsubtoken``) and endpoints that require a path parameter
(character / guild id) are skipped automatically.
"""

import getpass
import importlib.util
import inspect
import sys
import time
from pathlib import Path

_HERE = Path(__file__).parent
_spec = importlib.util.spec_from_file_location("gw2", _HERE / "gw2-api-py.py")
gw2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gw2)

API = gw2.API


# --------------------------------------------------------------------------- #
# Endpoint discovery
# --------------------------------------------------------------------------- #

# Endpoints we never call automatically (writable / secret-modifying / known-broken).
SKIP_CALL = {
    "createsubtoken",   # would mint a sub-token (secret-modifying)
    "commerce",         # /v2/commerce index route returns 503 upstream
}


def classify(node):
    """Return 'public', 'private', or 'skip' based on __call__ source."""
    call = getattr(type(node), "__call__", None)
    if call is None:
        return "skip"
    try:
        src = inspect.getsource(call)
    except (OSError, TypeError):
        return "skip"
    if "_authMethodes" in src or "_authInfoMethodes" in src:
        return "private"
    if "_publicMethodes" in src or "_publicInfoMethodes" in src:
        return "public"
    return "skip"


def walk(node, path):
    """Yield (dotted_path, endpoint_node) for every endpoint instance."""
    if not hasattr(node, "_url_list"):
        return
    yield path, node
    for name, child in vars(node).items():
        if name.startswith("_") or name in ("apikey", "shema", "lang",
                                            "character", "guild"):
            continue
        if hasattr(child, "_url_list"):
            yield from walk(child, f"{path}.{name}")


def discover(api_instance):
    """Return list of (path, node, kind) for every callable endpoint."""
    endpoints = []
    for path, node in walk(api_instance, "API"):
        if any(part is None for part in node._url_list):
            continue
        leaf = path.rsplit(".", 1)[-1]
        if leaf in SKIP_CALL:
            continue
        kind = classify(node)
        if kind == "skip":
            continue
        endpoints.append((path, node, kind))
    return endpoints


# --------------------------------------------------------------------------- #
# Runner
# --------------------------------------------------------------------------- #

PASS = "[ OK ]"
FAIL = "[FAIL]"
SKIP = "[SKIP]"


# Body messages that mean "skip this endpoint, it's not a real failure".
SKIP_MESSAGES = ("API not active", "Invalid access token")


def _is_skip_response(obj):
    """GW2 returns small JSON bodies like ``{"text": "..."}`` for endpoints
    that are disabled or rejected by auth. Treat those as skipped, not failed.
    """
    if isinstance(obj, dict):
        text = obj.get("text", "")
        return any(m in text for m in SKIP_MESSAGES)
    if isinstance(obj, str):
        return any(m in obj for m in SKIP_MESSAGES)
    return False


def run_one(node):
    start = time.perf_counter()
    try:
        data = node()
    except Exception as e:
        dt = (time.perf_counter() - start) * 1000
        resp = getattr(e, "response", None)
        if resp is not None:
            try:
                body = resp.json()
            except ValueError:
                body = resp.text
            if _is_skip_response(body):
                reason = body.get("text") if isinstance(body, dict) else str(body)
                return "skip", dt, reason
        return False, dt, f"{type(e).__name__}: {e}"
    dt = (time.perf_counter() - start) * 1000
    if _is_skip_response(data):
        reason = data.get("text") if isinstance(data, dict) else str(data)
        return "skip", dt, reason
    preview = repr(data)
    if len(preview) > 70:
        preview = preview[:67] + "..."
    return True, dt, preview


def run_phase(title, endpoints):
    print()
    print("=" * 100)
    print(title)
    print("=" * 100)
    passed = failed = skipped = 0
    failures = []
    for path, node, _kind in endpoints:
        ok, dt, msg = run_one(node)
        if ok == "skip":
            marker = SKIP
            skipped += 1
        elif ok:
            marker = PASS
            passed += 1
        else:
            marker = FAIL
            failed += 1
            failures.append((path, msg))
        print(f"{marker} {path:<55} {dt:7.0f} ms   {msg}")
    print("-" * 100)
    print(f"{title}: {passed} passed, {failed} failed, {skipped} skipped "
          f"(of {len(endpoints)})")
    return passed, failed, skipped, failures


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def main():
    api_pub = API()
    all_pub = discover(api_pub)
    public_endpoints = [e for e in all_pub if e[2] == "public"]
    private_seen = sum(1 for e in all_pub if e[2] == "private")

    print(f"Discovered {len(public_endpoints)} public endpoints "
          f"and {private_seen} private endpoints "
          f"(always skipped: {', '.join(sorted(SKIP_CALL))}).")

    pub_pass, pub_fail, pub_skip, pub_failures = run_phase(
        "PUBLIC ENDPOINTS (no API key)", public_endpoints
    )

    print()
    print("=" * 100)
    print("Optional: test PRIVATE endpoints")
    print("=" * 100)
    print("Enter a Guild Wars 2 API key to also test private endpoints.")
    print("Leave blank to skip. (Input is hidden.)")
    try:
        key = getpass.getpass("API key: ").strip()
    except (EOFError, KeyboardInterrupt):
        key = ""

    priv_pass = priv_fail = priv_skip = 0
    priv_failures = []
    if key:
        api_priv = API(apikey=key)
        all_priv = discover(api_priv)
        private_endpoints = [e for e in all_priv if e[2] == "private"]
        priv_pass, priv_fail, priv_skip, priv_failures = run_phase(
            "PRIVATE ENDPOINTS (using supplied API key)", private_endpoints
        )
    else:
        print("(no key supplied - private endpoints skipped)")

    print()
    print("=" * 100)
    print("SUMMARY")
    print("=" * 100)
    print(f"  Public : {pub_pass} passed, {pub_fail} failed, {pub_skip} skipped")
    if key:
        print(f"  Private: {priv_pass} passed, {priv_fail} failed, {priv_skip} skipped")
    else:
        print(f"  Private: not tested")
    if pub_failures or priv_failures:
        print()
        print("Failures:")
        for path, msg in pub_failures + priv_failures:
            print(f"  - {path}: {msg}")
    print("=" * 100)

    sys.exit(0 if (pub_fail == 0 and priv_fail == 0) else 1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAborted.")
        sys.exit(130)
