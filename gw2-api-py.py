
import requests
import json

class _authMethodes:
    def get(_apikey, _url_list) -> dict:
        url = '/'.join(str(x) for x in _url_list)
        auth = "?access_token={}".format(_apikey)
        #print("API Request: {}".format(url + auth))
        try:
            return json.loads(requests.get(url + auth).text)
        except:
            return json.loads(requests.get(url + auth).text)
    def id(_apikey, _url_list, id: int) -> dict:
        url = '/'.join(str(x) for x in _url_list) + "?id={}".format(str(id))
        auth = "&access_token={}".format(_apikey)
        #print("API Request: {}".format(url + auth))
        try:
            return json.loads(requests.get(url + auth).text)
        except:
            return json.loads(requests.get(url + auth).text)
    def ids(_apikey, _url_list, ids: list[int]) -> list[dict]:
        url = '/'.join(str(x) for x in _url_list) + "?ids={}".format(','.join([str(i) for i in ids]))
        auth = "&access_token={}".format(_apikey)
        #print("API Request: {}".format(url + auth))
        try:
            return json.loads(requests.get(url + auth).text)
        except:
            return json.loads(requests.get(url + auth).text)
    def all(_apikey, _url_list) -> dict:
        url = '/'.join(str(x) for x in _url_list) + "?ids=all"
        auth = "&access_token={}".format(_apikey)
        #print("API Request: {}".format(url + auth))
        try:
            return json.loads(requests.get(url + auth).text)
        except:
            return json.loads(requests.get(url + auth).text)






class _publicMethodes:
     def get(_url_list):
        url = '/'.join(str(x) for x in _url_list)
        #print("API Request: {}".format(url))
        try:
            return json.loads(requests.get(url).text)
        except:
            return json.loads(requests.get(url).text)
     def id(_url_list, id):
        url = '/'.join(str(x) for x in _url_list) + "?id={}".format(str(id))
        #print("API Request: {}".format(url))
        try:
            return json.loads(requests.get(url).text)
        except:
            return json.loads(requests.get(url).text)
     def ids(_url_list, ids: list):
        url = '/'.join(str(x) for x in _url_list) + "?ids={}".format(','.join([str(i) for i in ids]))
        #print("API Request: {}".format(url))
        try:
            return json.loads(requests.get(url).text)
        except:
            return json.loads(requests.get(url).text)
     def all(_url_list):
        url = '/'.join(str(x) for x in _url_list) + "?ids=all"
        #print("API Request: {}".format(url))
        try:
            return json.loads(requests.get(url).text)
        except:
            return json.loads(requests.get(url).text)
        



class _publicInfoMethodes:
     def get(_url_list) -> str:
        url = '/'.join(str(x) for x in _url_list)
        #print("API Request: {}".format(url))
        try:
            return json.loads(requests.get(url).text)
        except:
            return requests.get(url).text
    
class _authInfoMethodes:
     def get(_apikey, _url_list) -> dict:
        url = '/'.join(str(x) for x in _url_list)
        auth = "?access_token={}".format(_apikey)
        try:
            return json.loads(requests.get(url + auth).text)
        except:
            return requests.get(url + auth).text




class API:
    def endpoints():
        def Classmethodes(Object):
            return [method for method in dir(Object) if method.startswith('__') is False]
        Object =API
        endpoints = []
        for methode1 in Classmethodes(Object):
            endpoints.append(Object.__name__ + "." + methode1)
            for methode2 in Classmethodes(eval(Object.__name__ + "." + methode1)):
                endpoints.append(Object.__name__ + "." + methode1 + "." + methode2)
                for methode3 in Classmethodes(eval(Object.__name__ + "." + methode1 + "." + methode2)):
                    endpoints.append(Object.__name__ + "." + methode1 + "." + methode2 + "." + methode3)
                    for methode4 in Classmethodes(eval(Object.__name__ + "." + methode1 + "." + methode2 + "." + methode3)):
                        endpoints.append(Object.__name__ + "." + methode1 + "." + methode2 + "." + methode3 + "." + methode4)
                        for methode5 in Classmethodes(eval(Object.__name__ + "." + methode1 + "." + methode2 + "." + methode3 + "." + methode4)):
                            endpoints.append(Object.__name__ + "." + methode1 + "." + methode2 + "." + methode3 + "." + methode4 + "." + methode5)
                            for methode6 in Classmethodes(eval(Object.__name__ + "." + methode1 + "." + methode2 + "." + methode3 + "." + methode4 + "." + methode5)):
                                endpoints.append(Object.__name__ + "." + methode1 + "." + methode2 + "." + methode3 + "." + methode4 + "." + methode5 + "." + methode6)
                                for methode7 in Classmethodes(eval(Object.__name__ + "." + methode1 + "." + methode2 + "." + methode3 + "." + methode4 + "." + methode5 + "." + methode6)):
                                    endpoints.append(Object.__name__ + "." + methode1 + "." + methode2 + "." + methode3 + "." + methode4 + "." + methode5 + "." + methode6 + "." + methode7)
                                    for methode8 in Classmethodes(eval(Object.__name__ + "." + methode1 + "." + methode2 + "." + methode3 + "." + methode4 + "." + methode5 + "." + methode6 + "." + methode7)):
                                        endpoints.append(Object.__name__ + "." + methode1 + "." + methode2 + "." + methode3 + "." + methode4 + "." + methode5 + "." + methode6 + "." + methode7 + "." + methode8)
        return list(endpoints)

    def __init__(self,apikey: str = None):
        self.apikey = apikey
        self._url_list = ["https://api.guildwars2.com"]
        #self.v1 = self.v1(apikey=self.apikey, _url_list=self._url_list[:])
        self.v2 = self.v2(apikey=self.apikey, _url_list=self._url_list[:])
    def __call__(self):
        return _publicInfoMethodes.get(self._url_list)

   

    class v2:
        def json(self):
            return _publicInfoMethodes.get(self._url_list[:-1] + ["v2.json?v=latest"])
        def __init__(self,apikey, _url_list,shema: str = "latest", lang: str = "en"):
            '''
            More info about possible shemas and lang`s are available in API.v2.json()
            '''
            self.shema = shema
            self.lang = lang
            self.apikey = apikey
            self._url_list = _url_list
            self._url_list.append("v2")
            self.account = self.account(apikey=self.apikey, _url_list=self._url_list[:])
            self.achievements = self.achievements(apikey=self.apikey, _url_list=self._url_list[:])
            self.adventures = self.adventures(apikey=self.apikey, _url_list=self._url_list[:])
            self.backstory = self.backstory(apikey=self.apikey, _url_list=self._url_list[:])
            self.build = self.build(apikey=self.apikey, _url_list=self._url_list[:])
            self.characters = self.characters(apikey=self.apikey, _url_list=self._url_list[:])
            self.colors = self.colors(apikey=self.apikey, _url_list=self._url_list[:])
            self.commerce = self.commerce(apikey=self.apikey, _url_list=self._url_list[:])
            self.continents = self.continents(_url_list=self._url_list[:])
            self.createsubtoken = self.createsubtoken(apikey=self.apikey, _url_list=self._url_list[:])
            self.currencies = self.currencies(apikey=self.apikey, _url_list=self._url_list[:])
            self.dailycrafting = self.dailycrafting(apikey=self.apikey, _url_list=self._url_list[:])
            self.dungeons = self.dungeons(apikey=self.apikey, _url_list=self._url_list[:])
            self.emblem = self.emblem(apikey=self.apikey, _url_list=self._url_list[:])
            self.emotes = self.emotes(apikey=self.apikey, _url_list=self._url_list[:])
            #self.events = self.events(apikey=self.apikey, _url_list=self._url_list[:])                                   # API not active
            #self.events_state = self.events_state(apikey=self.apikey, _url_list=self._url_list[:])                                   # API not active
            self.files = self.files(apikey=self.apikey, _url_list=self._url_list[:])
            self.finishers = self.finishers(apikey=self.apikey, _url_list=self._url_list[:])
            #self.gemstore = self.gemstore(apikey=self.apikey, _url_list=self._url_list[:])                                   # API not active
            self.gliders = self.gliders(apikey=self.apikey, _url_list=self._url_list[:])
            self.guild = self.guild(apikey=self.apikey, _url_list=self._url_list[:])
            self.home = self.home(apikey=self.apikey, _url_list=self._url_list[:])
            self.items = self.items(apikey=self.apikey, _url_list=self._url_list[:])
            self.itemstats = self.itemstats(apikey=self.apikey, _url_list=self._url_list[:])
            self.jadebots = self.jadebots(apikey=self.apikey, _url_list=self._url_list[:])
            self.legendaryarmory = self.legendaryarmory(apikey=self.apikey, _url_list=self._url_list[:])
            self.legends = self.legends(apikey=self.apikey, _url_list=self._url_list[:])
            self.mailcarriers = self.mailcarriers(apikey=self.apikey, _url_list=self._url_list[:])
            self.mapchests = self.mapchests(apikey=self.apikey, _url_list=self._url_list[:])
            self.maps = self.maps(apikey=self.apikey, _url_list=self._url_list[:])
            self.masteries = self.masteries(apikey=self.apikey, _url_list=self._url_list[:])
            self.materials = self.materials(apikey=self.apikey, _url_list=self._url_list[:])
            self.minis = self.minis(apikey=self.apikey, _url_list=self._url_list[:])
            self.mounts = self.mounts(apikey=self.apikey, _url_list=self._url_list[:])
            self.novelties = self.novelties(_url_list=self._url_list[:])
            self.outfits = self.outfits(_url_list=self._url_list[:])
            self.pets = self.pets(_url_list=self._url_list[:])
            self.professions = self.professions(_url_list=self._url_list[:])
            self.pvp = self.pvp(apikey=self.apikey, _url_list=self._url_list[:])
            self.quaggans = self.quaggans(apikey=self.apikey, _url_list=self._url_list[:])
            self.quests = self.quests(apikey=self.apikey, _url_list=self._url_list[:])
            self.races = self.races(apikey=self.apikey, _url_list=self._url_list[:])
            self.raids = self.raids(apikey=self.apikey, _url_list=self._url_list[:])
            self.recipes = self.recipes(apikey=self.apikey, _url_list=self._url_list[:])
            self.skiffs = self.skiffs(apikey=self.apikey, _url_list=self._url_list[:])
            self.skills = self.skills(apikey=self.apikey, _url_list=self._url_list[:])
            self.skins = self.skins(apikey=self.apikey, _url_list=self._url_list[:])
            self.specializations = self.specializations(apikey=self.apikey, _url_list=self._url_list[:])
            self.stories = self.stories(apikey=self.apikey, _url_list=self._url_list[:])
            self.titles = self.titles(apikey=self.apikey, _url_list=self._url_list[:])
            self.tokeninfo = self.tokeninfo(apikey=self.apikey, _url_list=self._url_list[:])
            self.traits = self.traits(apikey=self.apikey, _url_list=self._url_list[:])
            #self.vendors = self.vendors(apikey=self.apikey, _url_list=self._url_list[:])
            self.wizardsvault = self.wizardsvault(_url_list=self._url_list[:])
            self.worldbosses = self.worldbosses(apikey=self.apikey, _url_list=self._url_list[:])
            self.worlds = self.worlds(apikey=self.apikey, _url_list=self._url_list[:])
            self.wvw = self.wvw(apikey=self.apikey, _url_list=self._url_list[:])
        def __call__(self):
            return _publicInfoMethodes.get(self._url_list)
        class account:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("account")
                self.achievements = self.achievements(apikey=self.apikey, _url_list=self._url_list[:])
                self.bank = self.bank(apikey=self.apikey, _url_list=self._url_list[:])
                self.buildstorage = self.buildstorage(apikey=self.apikey, _url_list=self._url_list[:])
                self.dailycrafting = self.dailycrafting(apikey=self.apikey, _url_list=self._url_list[:])
                self.dungeons = self.dungeons(apikey=self.apikey, _url_list=self._url_list[:])
                self.dyes = self.dyes(apikey=self.apikey, _url_list=self._url_list[:])
                self.emotes = self.emotes(apikey=self.apikey, _url_list=self._url_list[:])
                self.finishers = self.finishers(apikey=self.apikey, _url_list=self._url_list[:])
                self.gliders = self.gliders(apikey=self.apikey, _url_list=self._url_list[:])
                self.home = self.home(apikey=self.apikey, _url_list=self._url_list[:])
                self.inventory = self.inventory(apikey=self.apikey, _url_list=self._url_list[:])
                self.jadebots = self.jadebots(apikey=self.apikey, _url_list=self._url_list[:])
                self.legendaryarmory = self.legendaryarmory(apikey=self.apikey, _url_list=self._url_list[:])
                self.luck = self.luck(apikey=self.apikey, _url_list=self._url_list[:])
                self.mailcarriers = self.mailcarriers(apikey=self.apikey, _url_list=self._url_list[:])
                self.mapchests = self.mapchests(apikey=self.apikey, _url_list=self._url_list[:])
                self.masteries = self.masteries(apikey=self.apikey, _url_list=self._url_list[:])
                self.mastery = self.mastery(apikey=self.apikey, _url_list=self._url_list[:])
                self.materials = self.materials(apikey=self.apikey, _url_list=self._url_list[:])
                self.minis = self.minis(apikey=self.apikey, _url_list=self._url_list[:])
                self.mounts = self.mounts(apikey=self.apikey, _url_list=self._url_list[:])
                self.novelties = self.novelties(apikey=self.apikey, _url_list=self._url_list[:])
                self.outfits = self.outfits(apikey=self.apikey, _url_list=self._url_list[:])
                self.progression = self.progression(apikey=self.apikey, _url_list=self._url_list[:])
                self.pvp = self.pvp(apikey=self.apikey, _url_list=self._url_list[:])
                self.raids = self.raids(apikey=self.apikey, _url_list=self._url_list[:])
                self.recipes = self.recipes(apikey=self.apikey, _url_list=self._url_list[:])
                self.skiffs = self.skiffs(apikey=self.apikey, _url_list=self._url_list[:])
                self.skins = self.skins(apikey=self.apikey, _url_list=self._url_list[:])
                self.titles = self.titles(apikey=self.apikey, _url_list=self._url_list[:])
                self.wallet = self.wallet(apikey=self.apikey, _url_list=self._url_list[:])
                self.wizardsvault = self.wizardsvault(apikey=self.apikey, _url_list=self._url_list[:])
                self.worldbosses = self.worldbosses(apikey=self.apikey, _url_list=self._url_list[:])
                self.mail = self.mail(apikey=self.apikey, _url_list=self._url_list[:])
            def __call__(self):
                return _authMethodes.get(self.apikey, self._url_list)
            class achievements:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("achievements")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class bank:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("bank")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class buildstorage:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("buildstorage")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class dailycrafting:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("dailycrafting")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class dungeons:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("dungeons")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class dyes:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("dyes")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class emotes:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("emotes")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class finishers:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("finishers")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class gliders:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("gliders")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class home:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("home")
                    self.cats = self.cats(apikey=self.apikey, _url_list=self._url_list[:])
                    self.nodes = self.nodes(apikey=self.apikey, _url_list=self._url_list[:])
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
                class nodes:
                    def __init__(self,apikey,_url_list):
                        self.apikey = apikey
                        self._url_list = _url_list
                        self._url_list.append("nodes")
                    def __call__(self):
                        return _authMethodes.get(self.apikey, self._url_list)
                class cats:
                    def __init__(self,apikey,_url_list):
                        self.apikey = apikey
                        self._url_list = _url_list
                        self._url_list.append("cats")
                    def __call__(self):
                        return _authMethodes.get(self.apikey, self._url_list)
            class inventory:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("inventory")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class jadebots:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("jadebots")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class legendaryarmory:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("legendaryarmory")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class luck:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("luck")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class mail:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("mail")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class mailcarriers:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("mailcarriers")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class mapchests:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("mapchests")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class masteries:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("masteries")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class mastery:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("mastery")
                    self.points = self.points(apikey=self.apikey, _url_list=self._url_list[:])
                class points:
                    def __init__(self,apikey,_url_list):
                        self.apikey = apikey
                        self._url_list = _url_list
                        self._url_list.append("points")
                    def __call__(self):
                        return _authMethodes.get(self.apikey, self._url_list)
            class materials:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("materials")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class minis:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("minis")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class mounts:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("mounts")
                    self.skins = self.skins(apikey=self.apikey, _url_list=self._url_list[:])
                    self.types = self.types(apikey=self.apikey, _url_list=self._url_list[:])
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
                class skins:
                    def __init__(self,apikey,_url_list):
                        self.apikey = apikey
                        self._url_list = _url_list
                        self._url_list.append("skins")
                    def __call__(self):
                        return _authMethodes.get(self.apikey, self._url_list) 
                class types:
                    def __init__(self,apikey,_url_list):
                        self.apikey = apikey
                        self._url_list = _url_list
                        self._url_list.append("types")
                    def __call__(self):
                        return _authMethodes.get(self.apikey, self._url_list) 
            class novelties:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("novelties")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list) 
            class outfits:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("outfits")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class progression:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("progression")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class pvp:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("pvp")
                    self.heroes = self.heroes(apikey=self.apikey, _url_list=self._url_list[:])
                class heroes:
                    def __init__(self,apikey,_url_list):
                        self.apikey = apikey
                        self._url_list = _url_list
                        self._url_list.append("heroes")
                    def __call__(self):
                        return _authMethodes.get(self.apikey, self._url_list) 
            class raids:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("raids")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class recipes:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("recipes")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list) 
            class skiffs:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("skiffs")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class skins:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("skins")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class titles:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("titles")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class wallet:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("wallet")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class wizardsvault:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("wizardsvault")
                    self.daily = self.daily(apikey=self.apikey, _url_list=self._url_list[:])
                    self.listings = self.listings(apikey=self.apikey, _url_list=self._url_list[:])
                    self.special = self.special(apikey=self.apikey, _url_list=self._url_list[:])
                    self.weekly = self.weekly(apikey=self.apikey, _url_list=self._url_list[:])
                class daily:
                    def __init__(self,apikey,_url_list):
                        self.apikey = apikey
                        self._url_list = _url_list
                        self._url_list.append("daily")
                    def __call__(self):
                        return _authMethodes.get(self.apikey, self._url_list)
                class listings:
                    def __init__(self,apikey,_url_list):
                        self.apikey = apikey
                        self._url_list = _url_list
                        self._url_list.append("listings")
                    def __call__(self):
                        return _authMethodes.get(self.apikey, self._url_list)
                class special:
                    def __init__(self,apikey,_url_list):
                        self.apikey = apikey
                        self._url_list = _url_list
                        self._url_list.append("special")
                    def __call__(self):
                        return _authMethodes.get(self.apikey, self._url_list)
                class weekly:
                    def __init__(self,apikey,_url_list):
                        self.apikey = apikey
                        self._url_list = _url_list
                        self._url_list.append("weekly")
                    def __call__(self):
                        return _authMethodes.get(self.apikey, self._url_list)
            class worldbosses:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("worldbosses")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
        class achievements:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("achievements")
                self.categories = self.categories(_url_list=self._url_list[:])
                self.daily = self.daily(_url_list=self._url_list[:])
                self.groups = self.groups(_url_list=self._url_list[:])
            def __call__(self) -> list[int]:
                return _publicMethodes.get(self._url_list)
            def id(self, id: int) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids: list[int]) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            class groups:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("groups")
                def __call__(self) -> list[int]:
                    return _publicMethodes.get(self._url_list)
                def id(self, id: str) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids: list[str]) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
            class categories:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("categories")
                def __call__(self) -> list[int]:
                    return _publicMethodes.get(self._url_list)
                def id(self, id: int) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids: list[int]) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
            class daily:                                                                                           # API ENDPOINT CURRENTLY NOT ACTIVE !!!
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("daily")
                    self.tomorrow = self.tomorrow(_url_list=self._url_list[:])
                def __call__(self) -> list[int]:
                    return _publicMethodes.get(self._url_list)
                def id(self, id: int) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids: list[int]) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
                class tomorrow:                                                                                           # API ENDPOINT CURRENTLY NOT ACTIVE !!!
                    def __init__(self,_url_list):
                        self._url_list = _url_list
                        self._url_list.append("tomorrow")
                    def __call__(self) -> list[int]:
                        return _publicMethodes.get(self._url_list)
                    def id(self, id: int) -> dict:
                        return _publicMethodes.id(self._url_list, id)
                    def ids(self, ids: list[int]) -> list[dict]:
                        return _publicMethodes.ids(self._url_list, ids)
                    def all(self) -> list[dict]:
                        return _publicMethodes.all(self._url_list)
        class adventures:                                                                                                # API ENDPOINT CURRENTLY NOT ACTIVE !!! STILL TODO
            def __init__(self,apikey,_url_list, id = None):
                self.id = id
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("adventures")
                self.leaderboards = self.leaderboards(apikey=self.apikey, _url_list=self._url_list[:], id = self.id)
            def __call__(self) -> list[str]:
                return _authMethodes.get(self.apikey, self._url_list)
            class leaderboards:
                def __init__(self,apikey,_url_list, id = None):
                    self.id = id
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("leaderboards")
                def __call__(self) -> list[str]:
                    return _publicMethodes.get(self._url_list)
        class backstory:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("backstory")
                self.answers = self.answers(apikey=self.apikey, _url_list=self._url_list[:])
                self.questions = self.questions(apikey=self.apikey, _url_list=self._url_list[:])
            def __call__(self) -> list[str]:
                return _publicMethodes.get(self._url_list)
            class answers:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("answers")
                def __call__(self) -> list[str]:
                    return _publicMethodes.get(self._url_list)
                def id(self, id: str) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids: list[str]) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
            class questions:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("questions")
                def __call__(self) -> list[str]:
                    return _publicMethodes.get(self._url_list)
                def id(self, id: str) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids: list[str]) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
        class build:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("build")
            def __call__(self) -> dict:
                return _publicMethodes.get(self._url_list)
        class characters:
            def __init__(self, apikey, _url_list, character: str = None):
                self.character = character
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("characters")
                self.backstory = self.backstory(apikey=self.apikey, _url_list=self._url_list[:], character = self.character)
                self.buildtabs = self.buildtabs(apikey=self.apikey, _url_list=self._url_list[:], character = self.character)
                self.core = self.core(apikey=self.apikey, _url_list=self._url_list[:], character = self.character)
                self.crafting = self.crafting(apikey=self.apikey, _url_list=self._url_list[:], character = self.character)
                self.equipment = self.equipment(apikey=self.apikey, _url_list=self._url_list[:], character = self.character)
                self.equipmenttabs = self.equipmenttabs(apikey=self.apikey, _url_list=self._url_list[:], character = self.character)
                self.inventory = self.inventory(apikey=self.apikey, _url_list=self._url_list[:], character = self.character)
                self.recipes = self.recipes(apikey=self.apikey, _url_list=self._url_list[:], character = self.character)
                self.skills = self.skills(apikey=self.apikey, _url_list=self._url_list[:], character = self.character)
                self.specializations = self.specializations(apikey=self.apikey, _url_list=self._url_list[:], character = self.character)
                self.training = self.training(apikey=self.apikey, _url_list=self._url_list[:], character = self.character)
                self.dungeons = self.dungeons(apikey=self.apikey, _url_list=self._url_list[:], character = self.character)
                self.heropoints = self.heropoints(apikey=self.apikey, _url_list=self._url_list[:], character = self.character)
                self.quests = self.quests(apikey=self.apikey, _url_list=self._url_list[:], character = self.character)
                self.sab = self.sab(apikey=self.apikey, _url_list=self._url_list[:], character = self.character)
            def __call__(self, character: str = None) -> object:
                if character:
                    self.character = character
                    return API.v2.characters(apikey=self.apikey, _url_list=self._url_list[:-1], character = self.character)
                else:
                    return _authMethodes.get(self.apikey, self._url_list) 
            class backstory:
                def __init__(self,apikey,_url_list,character):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self.character = character
                    self._url_list.append(self.character)
                    self._url_list.append("backstory")
                def __call__(self) -> dict:
                    return _authMethodes.get(self.apikey, self._url_list) 
            class buildtabs:
                def __init__(self,apikey,_url_list,character):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self.character = character
                    self._url_list.append(self.character)
                    self._url_list.append("buildtabs")
                    self.active = self.active(apikey=self.apikey, _url_list=self._url_list[:], character = self.character)
                def __call__(self) -> dict:
                    return _authMethodes.get(self.apikey, self._url_list) 
                def id(self, id: int = None) -> dict:
                    return _authMethodes.id(self.apikey, self._url_list, id) 
                def active(self) -> dict:
                    return _authMethodes.active(self.apikey, self._url_list) 
                class active:
                    def __init__(self,apikey,_url_list,character):
                        self.apikey = apikey
                        self._url_list = _url_list
                        self.character = character
                        self._url_list.append("active")
                    def __call__(self):
                        return _authMethodes.get(self.apikey, self._url_list) 
            class core:
                def __init__(self,apikey,_url_list,character):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self.character = character
                    self._url_list.append(self.character)
                    self._url_list.append("core")
                def __call__(self) -> dict:
                    return _authMethodes.get(self.apikey, self._url_list) 
            class crafting:
                def __init__(self,apikey,_url_list,character):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self.character = character
                    self._url_list.append(self.character)
                    self._url_list.append("crafting")
                def __call__(self) -> dict:
                    return _authMethodes.get(self.apikey, self._url_list) 
            class equipment:
                def __init__(self,apikey,_url_list,character):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self.character = character
                    self._url_list.append(self.character)
                    self._url_list.append("equipment")
                def __call__(self) -> dict:
                    return _authMethodes.get(self.apikey, self._url_list) 
            class equipmenttabs:
                def __init__(self,apikey,_url_list,character):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self.character = character
                    self._url_list.append(self.character)
                    self._url_list.append("equipmenttabs")
                    self.active = self.active(apikey=self.apikey, _url_list=self._url_list[:], character = self.character)
                def __call__(self) -> list[int]:
                    return _authMethodes.get(self.apikey, self._url_list) 
                def id(self, id: int = None) -> dict:
                    return _authMethodes.id(self.apikey, self._url_list, id) 
                class active:
                    def __init__(self,apikey,_url_list,character):
                        self.apikey = apikey
                        self._url_list = _url_list
                        self.character = character
                        self._url_list.append("active")
                    def __call__(self):
                        return _authMethodes.get(self.apikey, self._url_list) 
            class inventory:
                def __init__(self,apikey,_url_list,character):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self.character = character
                    self._url_list.append(self.character)
                    self._url_list.append("inventory")
                def __call__(self) -> dict:
                    return _authMethodes.get(self.apikey, self._url_list) 
            class recipes:
                def __init__(self,apikey,_url_list,character):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self.character = character
                    self._url_list.append(self.character)
                    self._url_list.append("recipes")
                def __call__(self) -> dict:
                    return _authMethodes.get(self.apikey, self._url_list) 
            class skills:
                def __init__(self,apikey,_url_list,character):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self.character = character
                    self._url_list.append(self.character)
                    self._url_list.append("skills")
                def __call__(self) -> dict:
                    return _authMethodes.get(self.apikey, self._url_list) 
            class specializations:
                def __init__(self,apikey,_url_list,character):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self.character = character
                    self._url_list.append(self.character)
                    self._url_list.append("specializations")
                def __call__(self) -> dict:
                    return _authMethodes.get(self.apikey, self._url_list) 
            class training:
                def __init__(self,apikey,_url_list,character):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self.character = character
                    self._url_list.append(self.character)
                    self._url_list.append("training")
                def __call__(self) -> dict:
                    return _authMethodes.get(self.apikey, self._url_list) 
            class dungeons:
                def __init__(self,apikey,_url_list,character):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self.character = character
                    self._url_list.append(self.character)
                    self._url_list.append("dungeons")
                def __call__(self) -> dict:
                    return _authMethodes.get(self.apikey, self._url_list) 
            class heropoints:
                def __init__(self,apikey,_url_list,character):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self.character = character
                    self._url_list.append(self.character)
                    self._url_list.append("heropoints")
                def __call__(self) -> dict:
                    return _authMethodes.get(self.apikey, self._url_list) 
            class quests:
                def __init__(self,apikey,_url_list,character):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self.character = character
                    self._url_list.append(self.character)
                    self._url_list.append("quests")
                def __call__(self) -> dict:
                    return _authMethodes.get(self.apikey, self._url_list) 
            class sab:
                def __init__(self,apikey,_url_list,character):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self.character = character
                    self._url_list.append(self.character)
                    self._url_list.append("sab")
                def __call__(self) -> dict:
                    return _authMethodes.get(self.apikey, self._url_list) 
        class colors:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("colors")
            def __call__(self) -> list[int]:
                return _publicMethodes.get(self._url_list)
            def id(self, id: str) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids: list[str]) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class commerce:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("commerce")
                self.delivery = self.delivery(apikey=self.apikey, _url_list=self._url_list[:])
                self.exchange = self.exchange(apikey=self.apikey, _url_list=self._url_list[:])
                #self.listings = self.listings(apikey=self.apikey, _url_list=self._url_list[:])
                #self.prices = self.prices(apikey=self.apikey, _url_list=self._url_list[:])
                #self.transactions = self.transactions(apikey=self.apikey, _url_list=self._url_list[:])
                
            def __call__(self) -> list[int]:
                return _publicMethodes.get(self._url_list)
            class delivery:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("delivery")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class exchange:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("exchange")
                    self.coins = self.coins(_url_list=self._url_list[:])
                    self.gems = self.gems(_url_list=self._url_list[:])
                def __call__(self) -> list[int]:
                    return _publicMethodes.get(self._url_list)
                class coins:
                    def __init__(self,_url_list,quantity: int = 100000):
                        self.quantity = quantity
                        self._url_list = _url_list
                        self._url_list.append("coins")
                    def __call__(self, quantity: int = 100000) -> dict:
                        url = '/'.join(self._url_list)
                        try:
                            return json.loads(requests.get(url + "?quantity={}".format(str(quantity))).text)
                        except Exception as e:
                            #print(e)
                            return json.loads(requests.get(url + "?quantity={}".format(str(quantity))).text)
                class gems:
                    def __init__(self,_url_list):
                        self._url_list = _url_list
                        self._url_list.append("gems")
                    def __call__(self, quantity: int = 100000) -> dict:
                        url = '/'.join(self._url_list)
                        try:
                            return json.loads(requests.get(url + "?quantity={}".format(str(quantity))).text)
                        except Exception as e:
                            #print(e)
                            return json.loads(requests.get(url + "?quantity={}".format(str(quantity))).text)
        class continents:
            def __init__(self,_url_list,continent: int = None):
                self.continent = continent
                self._url_list = _url_list
                self._url_list.append("continents")
                self.floors = self.floors(_url_list=self._url_list[:], continent=self.continent, floors=None)
            def __call__(self, continent: int = None) -> object:
                if continent:
                    self.continent = continent
                    return API.v2.continents(_url_list=self._url_list[:-1], continent = self.continent)
                else:
                    return _publicMethodes.get(self._url_list) 
            def id(self, id: int = None) -> dict:
                    return _publicMethodes.id(self._url_list, id) 
            def ids(self, ids: list[int] = None) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
            class floors:
                def __init__(self,_url_list,continent,floors: int = None):
                    self.floors = floors
                    self.continent = continent
                    self._url_list = _url_list
                    self._url_list.append(self.continent)
                    self._url_list.append("floors")
                    self.regions = self.regions(_url_list=self._url_list[:], continent=self.continent, floors=self.floors)
                def __call__(self, floors: int = None) -> object:
                    if floors:
                        self.floors = floors
                        return API.v2.continents.floors(_url_list=self._url_list[:-2], continent=self.continent, floors=self.floors)
                    else:
                        return _publicMethodes.get(self._url_list) 
                def id(self, id: int = None) -> dict:
                    return _publicMethodes.id(self._url_list, id) 
                def ids(self, ids: list[int] = None) -> list[dict]:
                     return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
                class regions:
                    def __init__(self,_url_list,continent,floors,regions: int = None):
                        self.regions = regions
                        self.floors = floors
                        self.continent = continent
                        self._url_list = _url_list
                        self._url_list.append(self.floors)
                        self._url_list.append("regions")
                        self.maps = self.maps(_url_list=self._url_list[:], continent=self.continent, floors=self.floors, regions=self.regions)
                    def __call__(self, regions: int = None) -> object:
                        if regions:
                            self.regions = regions
                            return API.v2.continents.floors.regions(_url_list=self._url_list[:-2], continent=self.continent, floors=self.floors, regions=self.regions)
                        else:
                            return _publicMethodes.get(self._url_list) 
                    def id(self, id: int = None) -> dict:
                        return _publicMethodes.id(self._url_list, id) 
                    def ids(self, ids: list[int] = None) -> list[dict]:
                         return _publicMethodes.ids(self._url_list, ids)
                    def all(self) -> list[dict]:
                        return _publicMethodes.all(self._url_list)
                    class maps:
                        def __init__(self,_url_list,continent,floors,regions,maps: int = None):
                            self.maps = maps
                            self.regions = regions
                            self.floors = floors
                            self.continent = continent
                            self._url_list = _url_list
                            self._url_list.append(self.regions)
                            self._url_list.append("maps")
                            self.sectors = self.sectors(_url_list=self._url_list[:], continent=self.continent, floors=self.floors, regions=self.regions, maps=self.maps)
                            self.pois = self.pois(_url_list=self._url_list[:], continent=self.continent, floors=self.floors, regions=self.regions, maps=self.maps)
                            self.tasks = self.tasks(_url_list=self._url_list[:], continent=self.continent, floors=self.floors, regions=self.regions, maps=self.maps)
                        def __call__(self, maps: int = None) -> object:
                            if maps:
                                self.maps = maps
                                return API.v2.continents.floors.regions.maps(_url_list=self._url_list[:-2], continent=self.continent, floors=self.floors, regions=self.regions, maps=self.maps)
                            else:
                                return _publicMethodes.get(self._url_list) 
                        def id(self, id: int = None) -> dict:
                            return _publicMethodes.id(self._url_list, id) 
                        def ids(self, ids: list[int] = None) -> list[dict]:
                             return _publicMethodes.ids(self._url_list, ids)
                        def all(self) -> list[dict]:
                            return _publicMethodes.all(self._url_list)
                        class sectors:
                            def __init__(self,_url_list,continent,floors,regions,maps,sectors: int = None):
                                self.sectors = sectors
                                self.maps = maps
                                self.regions = regions
                                self.floors = floors
                                self.continent = continent
                                self._url_list = _url_list
                                self._url_list.append(self.maps)
                                self._url_list.append("sectors")
                            def __call__(self, sectors: int = None) -> object:
                                if sectors:
                                    self.sectors = sectors
                                    return API.v2.continents.floors.regions.maps.sectors(_url_list=self._url_list[:-2], continent=self.continent, floors=self.floors, regions=self.regions, maps=self.maps, sectors=self.sectors)
                                else:
                                    return _publicMethodes.get(self._url_list) 
                            def id(self, id: int = None) -> dict:
                                return _publicMethodes.id(self._url_list, id) 
                            def ids(self, ids: list[int] = None) -> list[dict]:
                                 return _publicMethodes.ids(self._url_list, ids)
                            def all(self) -> list[dict]:
                                return _publicMethodes.all(self._url_list)
                        class pois:
                            def __init__(self,_url_list,continent,floors,regions,maps,pois: int = None):
                                self.pois = pois
                                self.maps = maps
                                self.regions = regions
                                self.floors = floors
                                self.continent = continent
                                self._url_list = _url_list
                                self._url_list.append(self.maps)
                                self._url_list.append("pois")
                            def __call__(self, pois: int = None) -> object:
                                if pois:
                                    self.pois = pois
                                    return API.v2.continents.floors.regions.maps.pois(_url_list=self._url_list[:-2], continent=self.continent, floors=self.floors, regions=self.regions, maps=self.maps, pois=self.pois)
                                else:
                                    return _publicMethodes.get(self._url_list) 
                            def id(self, id: int = None) -> dict:
                                return _publicMethodes.id(self._url_list, id) 
                            def ids(self, ids: list[int] = None) -> list[dict]:
                                 return _publicMethodes.ids(self._url_list, ids)
                            def all(self) -> list[dict]:
                                return _publicMethodes.all(self._url_list)
                        class tasks:
                            def __init__(self,_url_list,continent,floors,regions,maps,tasks: int = None):
                                self.tasks = tasks
                                self.maps = maps
                                self.regions = regions
                                self.floors = floors
                                self.continent = continent
                                self._url_list = _url_list
                                self._url_list.append(self.maps)
                                self._url_list.append("tasks")
                            def __call__(self, tasks: int = None) -> object:
                                if tasks:
                                    self.tasks = tasks
                                    return API.v2.continents.floors.regions.maps.tasks(_url_list=self._url_list[:-2], continent=self.continent, floors=self.floors, regions=self.regions, maps=self.maps, tasks=self.tasks)
                                else:
                                    return _publicMethodes.get(self._url_list) 
                            def id(self, id: int = None) -> dict:
                                return _publicMethodes.id(self._url_list, id) 
                            def ids(self, ids: list[int] = None) -> list[dict]:
                                 return _publicMethodes.ids(self._url_list, ids)
                            def all(self) -> list[dict]:
                                return _publicMethodes.all(self._url_list)
        class createsubtoken:
            def __init__(self,apikey, _url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("createsubtoken")
                #
                #
                #
                #
            #def __call__(self, expire: str = None, permissions: list[str] = None, urls: list[str] = None):
                #url = '/'.join(self._url_list)
                #return json.loads(requests.get(url + "?access_token={}".format(str(self.apikey)) + "&expire={}".format(str(expire)) + "&permissions={}".format(",".join(permissions)) + "&urls={}".format(",".join(urls)).text))
            def __call__(self):
                return "for testing disabled!"           
        class currencies:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("currencies")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id: str) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids: list[str]) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class dailycrafting:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("dailycrafting")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id: str) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids: list[str]) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class dungeons:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("dungeons")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id: str) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids: list[str]) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class emblem:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("emblem")
                self.foregrounds = self.foregrounds(_url_list=self._url_list[:])
                self.backgrounds = self.backgrounds(_url_list=self._url_list[:])
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            class foregrounds:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("foregrounds")
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id: str) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids: list[str]) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)   
            class backgrounds:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("backgrounds")
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id: str) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids: list[str]) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list) 
        class emotes:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("emotes")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id: str) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids: list[str]) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list) 
        class events:
                                    ################################################################ TODO https://api.guildwars2.com/v2.json?v=latest index: 84
            pass
        class events_state:
                                    ################################################################ TODO https://api.guildwars2.com/v2.json?v=latest index: 85
            pass
        class files:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("files")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id: str) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids: list[str]) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list) 
        class finishers:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("finishers")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id: str) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids: list[str]) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list) 
        class gemstore:
                                    ################################################################ TODO https://api.guildwars2.com/v2.json?v=latest index: 88
            pass
        class gliders:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("gliders")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id: str) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids: list[str]) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list) 
        class guild:
            def __init__(self,apikey,_url_list,guild: str = None):
                self.guild = guild
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("guild")
                self.log = self.log(apikey=self.apikey,_url_list=self._url_list[:], guild=self.guild)
                self.members = self.members(apikey=self.apikey,_url_list=self._url_list[:], guild=self.guild)
                self.ranks = self.ranks(apikey=self.apikey,_url_list=self._url_list[:], guild=self.guild)
                self.stash = self.stash(apikey=self.apikey,_url_list=self._url_list[:], guild=self.guild)
                self.storage = self.storage(apikey=self.apikey,_url_list=self._url_list[:], guild=self.guild)
                self.teams = self.teams(apikey=self.apikey,_url_list=self._url_list[:], guild=self.guild)
                self.treasury = self.treasury(apikey=self.apikey,_url_list=self._url_list[:], guild=self.guild)
                self.upgrades = self.upgrades(apikey=self.apikey,_url_list=self._url_list[:], guild=self.guild)
                self.permissions = self.permissions(_url_list=self._url_list[:])
                self.search = self.search(_url_list=self._url_list[:])
                self.available_upgrades = self.available_upgrades(_url_list=self._url_list[:])
            def __call__(self, guild: str = None) -> object:
                self.guild = guild
                return API.v2.guild(apikey=self.apikey, _url_list=self._url_list[:-1], guild = self.guild)
            def get(self) -> object:    
                self._url_list.append(self.guild)
                return _publicMethodes.get(self._url_list)
            class log:
                def __init__(self,apikey,_url_list,guild: str = None):
                    self.guild = guild
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append(self.guild)
                    self._url_list.append("log")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class members:
                def __init__(self,apikey,_url_list,guild: str = None):
                    self.guild = guild
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append(self.guild)
                    self._url_list.append("members")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class ranks:
                def __init__(self,apikey,_url_list,guild: str = None):
                    self.guild = guild
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append(self.guild)
                    self._url_list.append("ranks")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class stash:
                def __init__(self,apikey,_url_list,guild: str = None):
                    self.guild = guild
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append(self.guild)
                    self._url_list.append("stash")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class storage:
                def __init__(self,apikey,_url_list,guild: str = None):
                    self.guild = guild
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append(self.guild)
                    self._url_list.append("storage")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class teams:
                def __init__(self,apikey,_url_list,guild: str = None):
                    self.guild = guild
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append(self.guild)
                    self._url_list.append("teams")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class treasury:
                def __init__(self,apikey,_url_list,guild: str = None):
                    self.guild = guild
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append(self.guild)
                    self._url_list.append("treasury")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class upgrades:
                def __init__(self,apikey,_url_list,guild):
                    self.guild = guild
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append(self.guild)
                    self._url_list.append("upgrades")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class permissions:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("permissions")
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
            class search:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("search")
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
            class available_upgrades:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("upgrades")
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
        class home:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("home")
                self.nodes = self.nodes(_url_list = self._url_list[:])
                self.cats = self.cats(_url_list = self._url_list[:])
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            class cats:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("cats")
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
            class nodes:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("nodes")
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
        class items:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("items")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class itemstats:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("itemstats")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class jadebots:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("jadebots")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class legendaryarmory:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("legendaryarmory")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class legends:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("legends")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class mailcarriers:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("mailcarriers")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class mapchests:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("mapchests")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class maps:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("maps")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class masteries:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("masteries")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class materials:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("materials")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class minis:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("minis")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class mounts:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("mounts")
                self.skins = self.skins(_url_list=self._url_list[:])
                self.types = self.types(_url_list=self._url_list[:])
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            class skins:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("skins")
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
            class types:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("types")
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
        class novelties:
            def __init__(self,_url_list):
                self._url_list = _url_list
                self._url_list.append("novelties")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class outfits:
            def __init__(self,_url_list):
                self._url_list = _url_list
                self._url_list.append("outfits")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class pets:
            def __init__(self,_url_list):
                self._url_list = _url_list
                self._url_list.append("pets")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class professions:
            def __init__(self,_url_list):
                self._url_list = _url_list
                self._url_list.append("professions")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class pvp:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("pvp")
                self.stats = self.stats(apikey=self.apikey,_url_list=self._url_list[:])
                self.games = self.games(apikey=self.apikey,_url_list=self._url_list[:])
                self.amulets = self.amulets(_url_list=self._url_list[:])
                self.ranks = self.ranks(_url_list=self._url_list[:])
                self.seasons = self.seasons(_url_list=self._url_list[:])
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
            class stats:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("stats")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class games:
                def __init__(self,apikey,_url_list):
                    self.apikey = apikey
                    self._url_list = _url_list
                    self._url_list.append("games")
                def __call__(self):
                    return _authMethodes.get(self.apikey, self._url_list)
            class amulets:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("amulets")
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
            class ranks:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("ranks")
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
            class seasons:
                def __init__(self,_url_list, season: str = None):
                    self.season = season
                    self._url_list = _url_list
                    self._url_list.append("seasons")
                    self.leaderboards = self.leaderboards(_url_list = self._url_list[:], season=self.season)
                def __call__(self, season: str = None) -> object:
                    if season:
                        self.season = season
                        return API.v2.pvp.seasons(_url_list=self._url_list[:-1], season = self.season)
                    else:
                        return _publicMethodes.get(self._url_list) 
                class leaderboards:
                    def __init__(self,_url_list,season):
                        self.season = season
                        self._url_list = _url_list
                        self._url_list.append(self.season)
                        self._url_list.append("leaderboards")
                        self.legendary = self.legendary(_url_list = self._url_list[:], season=self.season)
                        self.guild = self.guild(_url_list = self._url_list[:], season=self.season)
                        self.ladder = self.ladder(_url_list = self._url_list[:], season=self.season)
                    def __call__(self):
                        return _publicMethodes.get(self._url_list)
                    class legendary:
                        def __init__(self,_url_list,season):
                            self.season = season
                            self._url_list = _url_list
                            self._url_list.append("legendary")
                            self.na = self.na(_url_list = self._url_list[:], season=self.season)
                            self.eu = self.eu(_url_list = self._url_list[:], season=self.season)
                        def __call__(self):
                            return _publicMethodes.get(self._url_list)
                        class na:
                            def __init__(self,_url_list,season):
                                self.season = season
                                self._url_list = _url_list
                                self._url_list.append("na")
                            def __call__(self):
                                return _publicMethodes.get(self._url_list)
                        class eu:
                            def __init__(self,_url_list,season):
                                self.season = season
                                self._url_list = _url_list
                                self._url_list.append("eu")
                            def __call__(self):
                                return _publicMethodes.get(self._url_list)
                    class guild:
                        def __init__(self,_url_list,season):
                            self.season = season
                            self._url_list = _url_list
                            self._url_list.append("guild")
                            self.na = self.na(_url_list = self._url_list[:], season=self.season)
                            self.eu = self.eu(_url_list = self._url_list[:], season=self.season)
                        def __call__(self):
                            return _publicMethodes.get(self._url_list)
                        class na:
                            def __init__(self,_url_list,season):
                                self.season = season
                                self._url_list = _url_list
                                self._url_list.append("na")
                            def __call__(self):
                                return _publicMethodes.get(self._url_list)
                        class eu:
                            def __init__(self,_url_list,season):
                                self.season = season
                                self._url_list = _url_list
                                self._url_list.append("eu")
                            def __call__(self):
                                return _publicMethodes.get(self._url_list)
                    class ladder:
                        def __init__(self,_url_list,season):
                            self.season = season
                            self._url_list = _url_list
                            self._url_list.append("ladder")
                            self.na = self.na(_url_list = self._url_list[:], season=self.season)
                            self.eu = self.eu(_url_list = self._url_list[:], season=self.season)
                        def __call__(self):
                            return _publicMethodes.get(self._url_list)
                        class na:
                            def __init__(self,_url_list,season):
                                self.season = season
                                self._url_list = _url_list
                                self._url_list.append("na")
                            def __call__(self):
                                return _publicMethodes.get(self._url_list)
                        class eu:
                            def __init__(self,_url_list,season):
                                self.season = season
                                self._url_list = _url_list
                                self._url_list.append("eu")
                            def __call__(self):
                                return _publicMethodes.get(self._url_list)
        class quaggans:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("quaggans")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class quests:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("quests")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class races:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("races")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class raids:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("raids")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class recipes:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("recipes")
                self.search = self.search(_url_list=self._url_list[:])
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
            class search:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("search")
                def input(self, itemid: int = None):
                    url = "/".join(self._url_list) + "?input={}".format(str(itemid))
                    try:
                        return json.loads(requests.get(url).text)
                    except:
                        return json.loads(requests.get(url).text)
                

                def output(self, itemid: int = None):
                    url = "/".join(self._url_list) + "?output={}".format(str(itemid))
                    try:
                        return json.loads(requests.get(url).text)
                    except:
                        return json.loads(requests.get(url).text)
        class skiffs:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("skiffs")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class skills:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("skills")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class skins:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("skins")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class specializations:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("specializations")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class stories:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("stories")
                self.seasons = self.seasons(_url_list=self._url_list[:])
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
            class seasons:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("seasons")
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id: str = None):
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids: list[str] = None):
                    return _publicMethodes.ids(self._url_list, ids)
        class titles:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("titles")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class tokeninfo:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("tokeninfo")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
        class traits:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("traits")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class vendors:
                                    ################################################################ TODO https://api.guildwars2.com/v2.json?v=latest index: 151
            pass
        class wizardsvault:
            def __init__(self,_url_list):
                self._url_list = _url_list
                self._url_list.append("wizardsvault")
                self.listings = self.listings(_url_list=self._url_list[:])
                self.objectives = self.objectives(_url_list=self._url_list[:])
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
            class listings:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("listings")
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
            class objectives:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("objectives")
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
        class worldbosses:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("worldbosses")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class worlds:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("worlds")
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
        class wvw:
            def __init__(self,apikey,_url_list):
                self.apikey = apikey
                self._url_list = _url_list
                self._url_list.append("wvw")
                self.abilities = self.abilities(_url_list=self._url_list[:])
                self.matches = self.matches(_url_list=self._url_list[:])
                self.objectives = self.objectives(_url_list=self._url_list[:])
                self.ranks = self.ranks(_url_list=self._url_list[:])
                self.upgrades = self.upgrades(_url_list=self._url_list[:])
                self.rewardtracks = self.rewardtracks(_url_list=self._url_list[:])
            def __call__(self):
                return _publicMethodes.get(self._url_list)
            def id(self, id) -> dict:
                return _publicMethodes.id(self._url_list, id)
            def ids(self, ids) -> list[dict]:
                return _publicMethodes.ids(self._url_list, ids)
            def all(self) -> list[dict]:
                return _publicMethodes.all(self._url_list)
            class abilities:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("abilities")
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
            class matches:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("matches")
                    self.overview = self.overview(_url_list=self._url_list[:])
                    self.scores = self.scores(_url_list=self._url_list[:])
                    self.stats = self.stats(_url_list=self._url_list[:])
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
                class overview:
                    def __init__(self,_url_list):
                        self._url_list = _url_list
                        self._url_list.append("overview")
                    def __call__(self):
                        return _publicMethodes.get(self._url_list)
                    def id(self, id) -> dict:
                        return _publicMethodes.id(self._url_list, id)
                    def ids(self, ids) -> list[dict]:
                        return _publicMethodes.ids(self._url_list, ids)
                    def all(self) -> list[dict]:
                        return _publicMethodes.all(self._url_list)
                class scores:
                    def __init__(self,_url_list):
                        self._url_list = _url_list
                        self._url_list.append("scores")
                    def __call__(self):
                        return _publicMethodes.get(self._url_list)
                    def id(self, id) -> dict:
                        return _publicMethodes.id(self._url_list, id)
                    def ids(self, ids) -> list[dict]:
                        return _publicMethodes.ids(self._url_list, ids)
                    def all(self) -> list[dict]:
                        return _publicMethodes.all(self._url_list)
                class stats:
                    def __init__(self,_url_list, stats: str = None):
                        self.stats = stats
                        self._url_list = _url_list
                        self._url_list.append("stats")
                        self.guilds = self.guilds(_url_list=self._url_list[:], stats=self.stats)
                        self.teams = self.teams(_url_list=self._url_list[:], stats=self.stats)
                    def __call__(self, stats: str = None):
                        self.stats = stats
                        if stats == None:
                            return _publicMethodes.get(self._url_list)
                        else:
                            return API.v2.wvw.matches.stats(_url_list=self._url_list[:-1], stats=self.stats)
                    def id(self, id) -> dict:
                        return _publicMethodes.id(self._url_list, id)
                    def ids(self, ids) -> list[dict]:
                        return _publicMethodes.ids(self._url_list, ids)
                    def all(self) -> list[dict]:
                        return _publicMethodes.all(self._url_list)
                    class guilds:
                        def __init__(self,_url_list, stats: str = None):
                            self.stats = stats
                            self._url_list = _url_list
                            self._url_list.append(self.stats)
                            self._url_list.append("guilds")
                        def __call__(self, guild_id: str = None):
                            self._url_list.append(guild_id)
                            return _publicMethodes.get(self._url_list)
                    class teams:
                        def __init__(self,_url_list, stats: str = None):
                            self.stats = stats
                            self._url_list = _url_list
                            self._url_list.append(self.stats)
                            self._url_list.append("teams")
                        def __call__(self, team_id: str = None):
                            self.team_id = team_id
                            if team_id == None:
                                return _publicMethodes.get(self._url_list)
                            else:
                                return API.v2.wvw.matches.stats.teams(_url_list=self._url_list[:-2], stats=self.stats)
            class objectives:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("objectives")
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
            class ranks:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("ranks")
                def __call__(self):
                    return _publicMethodes.get(self._url_list)
                def id(self, id) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
            class upgrades:
                def __init__(self,_url_list):
                    self._url_list = _url_list
                    self._url_list.append("upgrades")
                def __call__(self) -> list[int]:
                    return _publicMethodes.get(self._url_list)
                def id(self, id) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
            class rewardtracks:                                     # API NOT AKTIVE
                def __init__(self,_url_list):
                    '''
                    NOT ACTIVE
                    '''
                    self._url_list = _url_list
                    self._url_list.append("rewardtracks")
                def __call__(self) -> list[int]:
                    return _publicMethodes.get(self._url_list)
                def id(self, id) -> dict:
                    return _publicMethodes.id(self._url_list, id)
                def ids(self, ids) -> list[dict]:
                    return _publicMethodes.ids(self._url_list, ids)
                def all(self) -> list[dict]:
                    return _publicMethodes.all(self._url_list)
            