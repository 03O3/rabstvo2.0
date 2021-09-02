from time import sleep
from requests import post, get
from vk_api import VkApi


class Slaves():
    def __init__(self, token:str = None):
        self.vk = VkApi(token = token).get_api()
        self.appId = 7804694
        self.referer = self.vk.apps.getEmbeddedUrl(app_id = self.appId)['view_url']
        self.api = self.referer.replace('index', 'api')
        self.headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': self.referer,
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36'
        }
        self.lhash = ''
        self.rhash = ''
        

    def updateLhash(self):
        r = get(self.referer)
        r = r.text.split(',true,')[1].split(str(self.appId))[0].replace("'", '').replace(',', '')
        self.lhash = r
        return self.lhash

    def profile(self):
        data = {
            'notify': 'false',
            'method': 'info',
            "lhash": self.lhash
        }
        resp = post(self.api, headers = self.headers, data = data).json()
        if 'Произошла ошибка. Попробуйте очистить кеш и повторить запрос.' in resp['res']:
            self.updateLhash()
            return self.profile()
        elif 'Слишком много запросов, попробуйте немного позже.' in resp['res']:
            sleep(1)
            return self.profile()
        else:
            return resp

    def updateRhash(self):
        self.rhash = self.profile()['res']['hash']
        return self.rhash

    def farm(self):
        '''Функция для просмотра рекламы'''
        data = {
            'method': 'on_watсhеd',
            'rhash': self.rhash
        }
        resp = post(self.api, headers = self.headers, data = data).json()
        if 'Произошла ошибка. Попробуйте очистить кеш и повторить запрос.' in resp['res']:
            self.updateRhash()
            return self.farm()
        elif 'Слишком много запросов, попробуйте немного позже.' in resp['res']:
            sleep(1)
            return self.farm()
        else:
            return resp

    def coinflip(self):
        data = {
            'bet': 'blue',
            'v': '2',
            'method': 'start_flip',
            'rhash': self.rhash
        }
        resp = post(self.api, headers = self.headers, data = data).json()
        if 'Произошла ошибка. Попробуйте очистить кеш и повторить запрос.' in resp['res']:
            self.updateRhash()
            return self.coinflip()
        elif 'Слишком много запросов, попробуйте немного позже.' in resp['res']:
            sleep(1)
            return self.coinflip()
        else:
            return resp

    def upgrade(self, vkId):
        data = {
            "method": "upgrade",
            "vkid": vkId,
            "rhash": self.rhash
        }
        resp = post(self.api, headers = self.headers, data = data).json()
        if 'Произошла ошибка. Попробуйте очистить кеш и повторить запрос.' in resp['res']:
            self.updateRhash()
            return self.upgrade(vkId)
        elif 'Слишком много запросов, попробуйте немного позже.' in resp['res']:
            sleep(1)
            return self.upgrade(vkId)
        else:
            return resp

    def getMySlaves(self):
        profile = self.profile()
        slavelist = profile['res']['sl'].split('<button onclick=')
        slavelist.pop(0)
        slavelist = [slave.split('profile("')[1].split('",')[0] for slave in slavelist]
        return slavelist



