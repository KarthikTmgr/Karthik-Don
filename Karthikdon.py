#!/usr/bin/python2

#coding=utf-8

#The Credit For This Code Goes To Kartikdon

#If You Wanna Take Credits For This Code, Please Look Yourself Again...

#Reserved2020

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

from mechanize import Browser

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():

	print "\x1b[1;91mExit"	os.sys.exit()

def acak(b):

    w = 'ahtdzjc'

    d = ''

    for i in x:

        d += '!'+w[random.randint(0,len(w)-1)]+i

    return cetak(d)

def cetak(b):

    w = 'ahtdzjc'

    for i in w:

        j = w.index(i)

        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))

    x += '\033[0m'

    x = x.replace('!0','\033[0m')

    sys.stdout.write(x+'\n')

def jalan(z):

	for e in z + '\n':

		sys.stdout.write(e)

		sys.stdout.flush()

		time.sleep(0.01)

#KarthikDon

##### LOGO #####

logo = """

                 .88888888:.

                88888888.88888.

              .8888888888888888.

              888888888888888888

              88' _`88'_  `88888

              88 88 88 88  88888

              88_88_::_88_:88888

              88:::,::,:::::8888

              88`:::::::::'`8888

             .88  `::::'    8:88.

            8888            `8:888.

          .8888'             `888888.

         .8888:..  .::.  ...:'8888888:.

        .8888.'     :'     `'::`88:88888

       .8888        '         `.888:8888.

      888:8         .           888:88888

    .888:88        .:           888:88888:

    8888888.       ::           88:888888

    `.::.888.      ::          .88888888

   .::::::.888.    ::         :::`8888'.:.

  ::::::::::.888   '         .::::::::::::

  ::::::::::::.8    '      .:8::::::::::::.

 .::::::::::::::.        .:888:::::::::::::

 :::::::::::::::88:.__..:88888:::::::::::'

  `'.:::::::::::88888888888.88:::::::::'

        `':::_:' -- '' -'-' `':_::::'`

---------------------------------------------

\033[1;96m|-------+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-----|

\033[1;96m|               Nep Anonymous               |

\033[1;96m|This Tool is Only for Nepali FB Acounts|

\033[1;96m|------+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+------|

\033[1;91m [⚡\033[1;97mAuthor Name: Karthik Mgr    ⚡\033[1;91m]

\033[1;91m [⚡\033[1;97mYutube Chnl: Dark sec Anonymous ⚡\033[1;91m]

\033[1;91m [⚡       \033[1;97mFrom: Nepal     ⚡\033[1;91m]

\033[1;95m«-_-_-_-_-_-_-_-_-\033[1;91mlegendkarthik\033[1;95m-_-_-_-_-_-_-_-_-»

"""

def tik():

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(0.1)

back = 0

berhasil = []

cekpoint = []

oks = []

id = []

listgrup = []

vulnot = "\033[31mNot Vuln"

vuln = "\033[32mVuln"

os.system("clear")

print  """

\033[1;91m░██╗░░░░░░░██╗███████╗██╗░░░░░

\033[1;91m░██║░░██╗░░██║██╔════╝██║░░░░░

\033[1;91m░╚██╗████╗██╔╝█████╗░░██║░░░░░

\033[1;91m░░████╔═████║░██╔══╝░░██║░░░░░

\033[1;91m░░╚██╔╝░╚██╔╝░███████╗███████╗

\033[1;91m░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝

\033[1;91m░█████╗░░█████╗░███╗░░░███╗███████╗

\033[1;91m██╔══██╗██╔══██╗████╗░████║██╔════╝

\033[1;91m██║░░╚═╝██║░░██║██╔████╔██║█████╗░░

\033[1;91m██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░

\033[1;91m╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗

\033[1;91m░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝

\033[1;95m«-_-_-_-_-_-_-_-_-\033[1;91mkarthikdon\033[1;95m-_-_-_-_-_-_-_-_-»

\033[1;92mNote1: Enter Tool usernam and Password 

\033[1;92mNote2: This Tool is only for Nepal

\033[1;95m«-_-_-_-_-_-_-_-_-\033[1;91mkarthikdon\033[1;95m-_-_-_-_-_-_-_-_-»

 """

CorrectUsername = "KarthikTMagar"

CorrectPassword = "Karthikisdon"

loop = 'true'

while (loop == 'true'):

    username = raw_input("\033[1;91m \x1b[1;91mTool Username \x1b[1;91m: \x1b[1;92m")

    if (username == CorrectUsername):

    	password = raw_input("\033[1;91m \x1b[1;91mTool Password \x1b[1;91m: \x1b[1;92m")

        if (password == CorrectPassword):

            print "Logged in successfully as " + username #Dev:Babar_Ali

	    time.sleep(2)

            loop = 'false'

        else:

            print "\033[1;93mWrong Password"

            os.system('xdg-open https://youtube.com/channel/UCUNxE6_SW5EYO2Z56Jhz-mA')

    else:

        print "\033[1;94mWrong Username"

        os.system('xdg-open https://youtube.com/channel/UCUNxE6_SW5EYO2Z56Jhz-mA')

##### LICENSE #####

#=================#

def lisensi():

	os.system('clear')

	login()

####login#########

def login():

	os.system('clear')

	print logo

	print "\033[1;91m[1]\x1b[1;94mLogin With Facebook Account  "

        time.sleep(0.05)

	print "\033[1;91m[0]\033[1;94mExit             "

	pilih_login()

def pilih_login():

	peak = raw_input("\n\033[1;96mChoose an Option: \033[1;95m")

	if peak =="":

		print "\x1b[1;91mFill in correct
