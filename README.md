# gw2-api-py

A small, dependency-light Python wrapper around the
[Guild Wars 2 official API (v2)](https://wiki.guildwars2.com/wiki/API:Main).
Endpoints are exposed as a navigable object tree, so you can autocomplete your
way to the data instead of memorising URLs.

```python
client = API(apikey="YOUR-KEY").v2
print(client.build())                       # {'id': 200967}
print(client.items.id(19684))               # {'name': 'Mithril Ingot', ...}
print(client.account.bank())                # bank slots for the supplied key
```

---

## Features

- **Full v2 surface area** — account, characters, commerce (partial), guild,
  pvp, wvw, achievements, items, recipes, skins, and many more.
- **Robust networking** — a shared `requests.Session` with connection
  pooling, automatic retries with exponential backoff, respect for
  `Retry-After` headers, and sensible timeouts.
- **Batch chunking** — `.ids([...])` calls are automatically split into the
  200-id batches required by the GW2 API.
- **Object-tree navigation** — endpoints mirror the URL hierarchy
  (`API.v2.account.bank` ⇒ `/v2/account/bank`).
- **Introspection** — `API.endpoints()` returns the full dotted list of every
  available endpoint, generated recursively.
- **No heavy dependencies** — just `requests`.

---

## Installation

```cmd
git clone https://github.com/<you>/gw2-api-py.git
cd gw2-api-py
py -3 -m venv .venv
.venv\Scripts\activate
pip install requests
```

> The module file is named `gw2-api-py.py` (hyphens), so it is loaded via
> `importlib` rather than a plain `import` — see the snippet below.

---

## Quick start

```python
import importlib.util
spec = importlib.util.spec_from_file_location("gw2", "gw2-api-py.py")
gw2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(gw2)
API = gw2.API

# Public endpoints — no API key required
api = API()
print(api.v2.build())                        # current game build
print(api.v2.items.id(19684))                # Mithril Ingot
print(api.v2.items.ids([19684, 24, 19721]))  # batch fetch

# Authenticated endpoints — pass your API key
client = API(apikey="YOUR-KEY").v2
print(client.account())
print(client.account.wallet())
print(client.characters())                   # list of character names
print(client.characters(character="My Char").equipment())
```

### Common call patterns

Every leaf endpoint exposes the same four call styles where applicable:

| Call | Equivalent URL | Returns |
| --- | --- | --- |
| `endpoint()`            | `/v2/...`                        | list of ids or root object |
| `endpoint.id(x)`        | `/v2/...?id=x`                   | single object |
| `endpoint.ids([x, y])`  | `/v2/...?ids=x,y` (auto-chunked) | list of objects |
| `endpoint.all()`        | `/v2/...?ids=all`                | every object (use sparingly) |

---

## Discover every endpoint

```python
for ep in API.endpoints():
    print(ep)
```

The walker is recursive, so any newly added endpoint class is picked up
automatically — no hand-maintained list.

---

## Reliability details

The HTTP layer is built around a shared `requests.Session` plus
`urllib3.Retry`:

| Setting                       | Value                          | Why |
| ---                           | ---                            | --- |
| `total` retries               | `5`                            | survives transient blips |
| `backoff_factor`              | `0.5` (0.5s → 8s exponential)  | avoids hammering on failure |
| `status_forcelist`            | `429, 500, 502, 503, 504`      | retry rate-limits and 5xx |
| `respect_retry_after_header`  | `True`                         | honours GW2's rate-limit hints |
| Connect timeout               | `10 s`                         | fail fast on dead hosts |
| Read timeout                  | `30 s`                         | bounded waits |
| ID chunking                   | `200` per request              | GW2's hard cap |

A failed request raises `requests.HTTPError` / `requests.ConnectionError` /
`requests.Timeout` after retries are exhausted — never silently bad data.

---

## Testing

A standalone runner exercises every reachable endpoint:

```cmd
.venv\Scripts\python.exe test.py
```

It:

1. Walks the live API tree and calls every **public** endpoint.
2. Prompts (hidden input) for an API key; if provided, calls every
   **private** endpoint too.
3. Skips endpoints that need a path parameter (character / guild id),
   the `createsubtoken` helper, and `/v2/commerce` (which GW2 currently
   reports as *"API not active"* via a `503` — short-circuited so the
   retry layer doesn't waste ~15 s on it).
4. Treats GW2 responses like `{"text": "API not active"}` and
   `{"text": "Invalid access token"}` as `[SKIP]`, not `[FAIL]`.

Example output:

```text
[ OK ] API.v2.build                                          25 ms   {'id': 200967}
[ OK ] API.v2.items                                         148 ms   [4, 5, 6, 15, 24, ...]
[SKIP] API.v2.tokeninfo                                      24 ms   Invalid access token
[FAIL] API.v2.something                                   15021 ms   HTTPError: 503 ...

Public : 84 passed, 0 failed, 2 skipped
Private: 41 passed, 0 failed, 3 skipped
```

---

## Project layout

```text
gw2-api-py/
├── gw2-api-py.py     # the wrapper
├── test.py           # endpoint smoke-test runner
├── README.md
└── .venv/            # created by you
```

---

## License

No license file is included yet — treat the code as "all rights reserved"
until one is added.
