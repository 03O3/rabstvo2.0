from requests import post ,get #line:1
import json #line:2
from slavelib import Slaves #line:3
from random import randint #line:4
from time import sleep #line:5
import asyncio as aio #line:6
from colorama import init ,Fore #line:7
init ()#line:9
with open ('config.json','r')as f :#line:11
    config =json .load (f )#line:12
def auth (OOO0OOO0OOOO00O00 :str ,OO0O00OOO0O0OOOOO :str ,two_fa :bool =False ,code :str =None ):#line:13
    return get (f'https://oauth.vk.com/token',params ={'grant_type':'password','client_id':'6146827','client_secret':'qVxWRF1CwHERuIrKBnqe','username':OOO0OOO0OOOO00O00 ,'password':OO0O00OOO0O0OOOOO ,'v':'5.131','2fa_supported':'1','force_sms':'1'if two_fa else '0','code':code if two_fa else None }).json ()#line:24
def loginScreen ():#line:26
    OOO000000000O0OOO ,O00O000OOOO0OOOO0 =input ("Введите логин: "),input ("Введите пароль: ")#line:27
    OO000O000OOOO0O0O =auth (OOO000000000O0OOO ,O00O000OOOO0OOOO0 )#line:28
    if 'validation_sid'in OO000O000OOOO0O0O :#line:29
        get ("https://api.vk.com/method/auth.validatePhone",params ={'sid':OO000O000OOOO0O0O ['validation_sid'],'v':'5.131'})#line:30
        O0O0OOO0O0OOO000O =input ('Введите код из смс:  ')#line:31
        OO000O000OOOO0O0O =auth (OOO000000000O0OOO ,O00O000OOOO0OOOO0 ,two_fa =True ,code =O0O0OOO0O0OOO000O )#line:32
    config ['token']=OO000O000OOOO0O0O ['access_token']#line:34
    with open ('config.json','w')as OO0OO0OOO0OOOOO0O :#line:35
        json .dump (config ,OO0OO0OOO0OOOOO0O ,indent =4 )#line:36
    return OO000O000OOOO0O0O ['access_token']#line:37
if not config ['token']:#line:39
    token =loginScreen ()#line:40
else :#line:41
    token =config ['token']#line:42
api =Slaves (token )#line:44
async def balance ():#line:47
    while True :#line:48
        OO0OOOO0000OO000O =(await getProfile ())["res"]['balance']#line:49
        print (f'{Fore.LIGHTGREEN_EX}Ваш баланс: {OO0OOOO0000OO000O}')#line:50
        await aio .sleep (25 )#line:51
async def farmReklama ():#line:53
    while True :#line:54
        OO000O0000000OO0O =api .farm ()#line:55
        print (f'{Fore.LIGHTGREEN_EX}Вы успешно посмотрели рекламу!')#line:56
        await aio .sleep (10 )#line:57
async def getProfile ():#line:59
    return api .profile ()#line:60
async def getSlaves ():#line:62
    return api .getMySlaves ()#line:63
async def upgradeSlaves (OOOOOO00OO000OO00 :list ):#line:65
    for O0000O0OOO0OOO000 in OOOOOO00OO000OO00 :#line:66
        O0OOOOOO0OO00OO0O =api .upgrade (O0000O0OOO0OOO000 )#line:67
        print (O0OOOOOO0OO00OO0O )#line:68
async def main ():#line:70
    O0O0O00O0OOOOO0OO =aio .get_event_loop ()#line:71
    O0O0O00O0OOOOO0OO .create_task (farmReklama ())#line:72
    O0O0O00O0OOOOO0OO .create_task (balance ())#line:73
    while True :#line:74
        await upgradeSlaves (await getSlaves ())#line:75
        await aio .sleep (5 )#line:76
aio .run (main ())#line:78
