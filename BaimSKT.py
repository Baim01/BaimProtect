# -*- coding: utf-8 -*-
import SINGLEKILLER
from SINGLEKILLER.lib.curve.ttypes import *	
from datetime import datetime	
import io,os,re,ast,six,sys,glob,json,time,timeit,codecs,random,shutil,urllib,urllib2,urllib3,goslate,html5lib,requests,threading,wikipedia,subprocess,googletrans	,pytz
from gtts import gTTS	
from random import randint	
from time import sleep	
from urllib import urlopen, urlretrieve, urlencode	
from io import StringIO	
from bs4 import BeautifulSoup	
from threading import Thread	
from googletrans import Translator	

if (six.PY2):
    import urllib2
    import urllib
else:
    import urllib.request
    import urllib.parse
baim = SINGLEKILLER.LINE()
baim.login(token="Esolg6U8QbLrvoBGDnbf.a2jtIjiEA6OEd8Hqa7J97W.FDaejBegW9KcHKI/2HKZla2JH2m5Glpc17R81P7YDzg=")
baim.loginResult()
ki = SINGLEKILLER.LINE()
ki.login(token="EsNluuF1Zt82Y7ONOG09.JJp3+9nQAl9aBBedbFgVcq.gpvw5B5IpVjjJMATd2SHC8N/c9Wnb73in0x5v0t8JyE=")
ki.loginResult()
ki2= SINGLEKILLER.LINE()
ki2.login(token="")
ki2.loginResult()
ki3 = SINGLEKILLER.LINE()
ki3.login(token="")
ki3.loginResult()
ki4 = SINGLEKILLER.LINE()
ki4.login(token="")
ki4.loginResult()
ki5 = SINGLEKILLER.LINE()
ki5.login(token="")
ki5.loginResult()
ki6 = SINGLEKILLER.LINE()
ki6.login(token="")
ki6.loginResult()
ki7 = SINGLEKILLER.LINE()
ki7.login(token="")
ki7.loginResult()
ki8 = SINGLEKILLER.LINE()
ki8.login(token="")
ki8.loginResult()
ki9 = SINGLEKILLER.LINE()
ki9.login(token="")
ki9.loginResult()
ki10 = SINGLEKILLER.LINE()
ki10.login(token="")
ki10.loginResult()
print """
█▀▀█▒█▀▀█▒███▒██▒██▒▒▒▒▒▒████▒█▒▒██▒▒
█▒▒█▒█▒▒█▒▒█▒▒█▒█▒█▒▒▒▒▒▒█▒▒▒▒█▒█▒▒
███▒▒████▒▒█▒▒█▒█▒█▒▒▒▒▒▒████▒██▒▒
█▒▒█▒█▒▒█▒▒█▒▒█▒▒▒█▒▒▒▒▒▒▒▒▒█▒█▒█▒▒
█▄▄█▒█▒▒█▒███▒█▒▒▒█▒▒▒▒▒▒████▒█▒▒██▒▒

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒███▒▒
▓▓░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▓▓▒▒█▒▒▒▒
▓▓░░░░░░░░░▒░░░░░▒░░▒░░░░░░░░░░░░░░░░░░░▓▓▒▒███▒▒
▓▓░░░░░░░░░▒░░░░░▒░░▒░░░░░░░░░░░░░░░░░░░▓▓▒▒▒▒█▒▒
▓▓░░▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░▓▓▒▒███▒▒
▓▓░░▒░░░▒░░▒░░░▒░░░▒░░░▒░░░▒░░░░░░░░░░░░▓▓▒▒▒▒▒▒▒
▓▓░░▒░▒░▒▒▒▒░░░▒░░░▒░░░▒░░░▒▒▒▒▒▒▒▒▒░░░░▓▓▒▒█▒▒█▒
▓▓░░▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▒░░▒░░░▓▓▒▒█▒█▒▒
▓▓░░░▒░░░░░▒░░░▒░░░▒░░░▒░░░▒░░░░░▒▒▒▒░░░▓▓▒▒██▒▒▒
▓▓░░▒░░░░░░▒░░░▒░░░▒░░░▒░░░▒░░░░░▒░░▒░░░▓▓▒▒█▒█▒▒
▓▓░░▒░▒░▒▒▒▒░░░▒░░░▒░░░▒░░░▒▒▒▒▒▒▒▒▒░░░░▓▓▒▒█▒▒█▒
▓▓░░▒░░░▒░░▒░░░▒░░░▒░░░▒░░░▒░░░░░░░░░░░░▓▓▒▒▒▒▒▒▒
▓▓░░▒▒▒▒▒░░▒░░░▒░░░▒░░░▒░░░▒░░░░░░░░░░░░▓▓▒▒█████
▓▓░░░░░░░░░▒░░░▒░░░▒░░░▒░░░▒░░░░░░░░░░░░▓▓▒▒▒▒█▒▒
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒▒▒█▒▒
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒▒▒█▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒█▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒████▒█▒▒██▒▒▒█▒▒██▒███▒█▒▒▒█▒▒▒███▒███▒▒
▒█▒▒▒▒█▒█▒▒▒▒▒█▒█▒▒▒▒█▒▒█▒▒▒█▒▒▒█▒▒▒█▒▒█▒▒
▒████▒██▒▒▒▒▒▒██▒▒▒▒▒█▒▒█▒▒▒█▒▒▒██▒▒███▒▒
▒▒▒▒█▒█▒█▒▒▒▒▒█▒█▒▒▒▒█▒▒█▒▒▒█▒▒▒█▒▒▒██▒▒
▒████▒█▒▒██▒▒▒█▒▒██▒███▒███▒███▒███▒█▒█▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒█▒▒
\n
Login śєʟғ =====[☬ßΔꀧm⃠☬]=====
"""

reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage="""(╣••℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́к̰̰̈́ ̰в̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́••╣)
╔═B༘̈́̈́L༘̈́̈́Ä༘́̈́C༘̈́̈́K༘̈́̈́   ̈́Ö༘́̈́F༘̈́̈́ ̈́  G༘̈́̈́Ä༘́̈́M༘̈́̈́Ë༘́̈́R༘̈́̈́═╗
║1║ ✰ Me
║2║ ✰ Add
║3║ ✰ Gift
║4║ ✰ Spam gift️
║5║ ✰ Cn "text"
║6║ ✰ Clockname "text"
║7║ ✰ TL:"text"
║8║ ✰ Ban:"mid"
║9║ ✰ Unban:"mid"
║10║ ✰ Bl:on
║11║ ✰ Unbl:on
║12║ ✰ Mcheck
║13║ ✰ Mybio:
║14║ ✰ Mybots
║15║ ✰ Mymid
║16║ ✰ Mygroups
║17║ ✰ Group id
║18║ ✰ Message set:"text"
║19║ ✰ Message confirm
║20║ ✰ Msg add-"text"
║21║ ✰ Com set:"text"
║22║ ✰ Comment
║13║ ✰ Comban/del/cek
║24║ ✰ Help set:"text"
║25║ ✰ Change
║26║ ✰ Gn "text"
║27║ ✰ Clink/Curl
║28║ ✰ Kick:"mid"
║29║ ✰ Invite:"mid"
║30║ ✰ Creator
║31║ ✰ Gcancel:"jumlah"
║32║ ✰ Gcancelall
║33║ ✰ Ginfo
║34║ ✰ Check
║35║ ✰ Cctv
║36║ ✰ Glink
║37║ ✰ Spam on/off
║38║ ✰ Gurl
║39║ ✰ Clink
║40║ ✰ Blocklist
║41║ ✰ Banlist
║42║ ✰ Update
║23║ ✰ Creator
║44║ ✰ Sc:"mid"
║45║ ✰ Ban "@"
║46║ ✰ Unban "@"
║47║ ✰ Sc @
║48║ ✰ Nuke
║49║ ✰ Backup
║50║ ✰ Tagall
║51║ ✰ Kick@mbl 
║52║ ✰ Reinvite
║53║ ✰ Conban
║54║ ✰ Clearban
║55║ ✰ Gid
║56║ ✰ Grupname
║57║ ✰ Lurk:on/off
║58║ ✰ Lurkers
║59║ ✰ Wc️
║60║ ✰ Sp
║61║ ✰ stafflist
║62║ ✰ Reboot
║63║ ✰ Leaveallgroup
║64║ ✰ Pmfavorite
║65║ ✰ Broken
║╩═══NEXT PAGE═══╦
║🃏║ ✰ {  Media  }
║🇲🇨║ ✰ {Translate}
║⚙️║ ✰ {    Set   }
║🏴║ ✰ {Helpbots}
║🔧║ ✰ {Settings}
║🔛║ ✰ {Setauto}
╚══╩════════╝
  """
helpMedia="""(╣••℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́к̰̰̈́ ̰в̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́••╣)
╔═B༘̈́̈́L༘̈́̈́Ä༘́̈́C༘̈́̈́K༘̈́̈́   ̈́Ö༘́̈́F༘̈́̈́ ̈́  G༘̈́̈́Ä༘́̈́M༘̈́̈́Ë༘́̈́R༘̈́̈́═╗
║╦═══MEDIA═══
║1║ ✰ Youtube *text*
║2║ ✰ Youtubesearch *user*
║3║ ✰ Audio "text"
║4║ ✰ Lirik "text"
║5║ ✰ Ig "name"
║5║ ✰ Tts "judul/nama band"
║6║ ✰ Gimage 
║7║ ✰ Image *text*
║8║ ✰ Google *text*
║9║ ✰ Micadd @
║10║ ✰ Micdel @
║11║ ✰ Miclist
║12║ ✰ Picturl @
║13║ ✰ Coverurl @
║14║ ✰ Copy @
║15║ ✰ Getname @
║16║ ✰ Getinfo @
║17║ ✰ pict @️
║18║ ✰ Getcontact @
║19║ ✰ Getvid @
║20║ ✰ Getmid @
║21║ ✰ Copy @     
║22║ ✰ Recopy
║23║ ✰ Getcover @    
║24║  ✰ Getbio @
║25║ ✰ Getinfo @
║26║ ✰ youinfo @
║27║ ✰ info "mid"
║28║ ✰ Contact "mid"
║29║ ✰ Id "idline"
║30║ ✰ Memlist
║31║ ✰ Setimage:
║32║ ✰ Papimage
║33║ ✰ Setvideo:
║34║ ✰ Papvideo
║25║ ✰ Checkdate
║36║ ✰ Myname
║37║ ✰ Mybio
║38║ ✰ Mypict
║39║ ✰ Myvid
║40║ ✰ Urlpict
║41║ ✰ Mycover
║42║ ✰ Urlcover
║43║ ✰ Hay "text"
║44║ ✰ Record "text"
║45║ ✰ Xvideo "text"
║46║ ✰ Smule "id smule"
║47║ ✰ Time
║48║ ✰ Imagetxt "text"
║49║ ✰ Cuaca*txt
║50║ ✰ Lokasi*txt
║51║ ✰ Shalat*txt
║52║ ✰ Anime"text"
║53║ ✰ Cekmovie"text"
║54║ ✰ Video"text"
║55║ ✰ Playstore"txt"
║56║ ✰ Twitter*txt
║57║ ✰ Klip"text"
║48║✰ Github*txt
║59║✰ Facebook*txt
║60║✰ Wikipedia*txt
║61║✰ Checkdate*ttl
║62║✰ Virus
║╩══BROADCAST═══
║📩║ ✰ sendpm "text"
║📨║ ✰ sendgrup "text"
║╩═══NEXT PAGE═╦
║🃏║ ✰ {  Media  }
║🇲🇨║ ✰ {Translate}
║⚙️║ ✰ {    Set   }
║🏴║ ✰ {Helpbots}
║🔧║ ✰ {Settings}
║🔛║ ✰ {Setauto}
╚══╩══════╝
"""
helpFun = """(╣℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́к̰̰̈́ ̰в̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́╣)
╔═B༘̈́̈́L༘̈́̈́Ä༘́̈́C༘̈́̈́K༘̈́̈́   ̈́Ö༘́̈́F༘̈́̈́ ̈́  G༘̈́̈́Ä༘́̈́M༘̈́̈́Ë༘́̈́R༘̈́̈́═╗
║╦═══MEDIA═══
║1║ ✰ sider:*txt*
║2║ ✰ tagme:*txt
║3║ ✰ welcome:*txt
║4║ ✰ left:*txt
║5║ ✰ message set:*txt*
║6║ ✰ STKID:*sticker id
║7║ ✰ STKPKGID:*stkr gid
║8║ ✰ STKVER:*version
║9║ ✰ cekresponse
║╩══NEXT PAGE══╦
║🃏║ ✰ {  Media  }
║🇲🇨║ ✰ {Translate}
║⚙️║ ✰ {    Set   }
║🏴║ ✰ {Helpbots}
║🔧║ ✰ {Settings}
║🔛║ ✰ {Setauto}
╚══╩══════╝
"""
helpself="""
╔╦═C༘֮֮O༘֮֮M༘֮֮M༘֮֮A༘֮֮N༘֮֮D༘֮֮ ֮A༘֮֮L༘֮֮L༘֮֮ ֮B༘֮֮O༘֮֮T༘֮֮S༘֮֮═╦╗
║ ═══════════║
║1║ ✰ Fuck1/10 "@"
║2║ ✰ Kick1/10 "@"
║3║ ✰ All mid
║4║ ✰ Reinvite
║5║ ✰ B1-10 mid
║6║ ✰ B1-10name "text"
║7║ ✰ B1-10
║8║ ✰ B1-10 gift
║9║ ✰ B1-10 in
║10║ ✰ B1-10 bye
║11║ ✰ Bc "text"
║12║ ✰ Say "text"
║13║ ✰ Bom "text"
║14║ ✰ Allgift
║15║ ✰ Spam gift️
║16║ ✰ Botcopy
║18║ ✰ Botbackup
║19║ ✰ Botpict
║20║ ✰ Botcover
║21║ ✰ Botak
║22║ ✰ Allname "nama"
║23║ ✰ Allbio "status"
║24║ ✰ Sendcontact "text"
║25║ ✰ Botbyeall  
║••℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́к̰̰̈́ ̰в̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́••
╚═══════════╝
  """
helpset="""╔(╣ S༘̏̏Ȅ༘̏T༘̏̏T༘̏̏Ȉ༘̏N༘̏̏G༘̏̏ ̏B༘̏̏Ȍ༘̏T༘̏̏S༘̏̏.╣)╗
║ ✰ Ban:on/Unbl:on
║ ✰ Contact:on/off
║ ✰ Add:on/off
║ ✰ Join:on/off
║ ✰ Leave:on/off
║ ✰ Share:on/off
║ ✰ Com:on/off
║ ✰ Clock:on/off
║ ✰ Respon:on/off
║ ✰ Stickertag:on/off
║ ✰ Welcome:on/off
║ ✰ Left:on/off
║ ✰ Sider:on/off
║ ✰ Notag:on/off
║ ✰ Mimic on/off
║ ✰ Simsimi:on/off
║ ✰ Read:0n/off
║ ✰ Like:on/off
║ ✰ Runtime
║═(╣S̰֮֮Ḛ֮֮T̰֮֮T̰֮֮Ḭ֮֮N̰֮֮G̰֮֮ ֮G̰֮֮R̰֮֮O̰֮֮Ṵ֮֮P̰֮֮S̰֮֮╣)═
║ ★ Pro:on/off
║ ★ Prolink:on/off
║ ★ Proinvite:on/off
║ ★ Procancel:on/off
║ ★ Namelock:on/off
║ ★ Projoin:on/off
║ ★ Allprotect:on/off
║╩═══NEXT PAGE═╦
║🃏║ ✰ {  Media  }
║🇲🇨║ ✰ {Translate}
║⚙️║ ✰ {    Set   }
║🏴║ ✰ {Helpbots}
║🔧║ ✰ {Settings}
║🔛║ ✰ {Setauto}
╚══╩══════╝
║ ╦═B༘̈́̈́L༘̈́̈́Ä༘́̈́C༘̈́̈́K༘̈́̈́   ̈́Ö༘́̈́F༘̈́̈́ ̈́  G༘̈́̈́Ä༘́̈́M༘̈́̈́Ë༘́̈́R༘̈́̈́═╦
╚═•℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́к̰̰̈́ ̰в̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́•╝
"""
translateMessage ="""
╔══════════
║(╣℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́к̰̰̈́ ̰в̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́╣)
║╔═════════
║══════════
║✰║ Afrika/
║✰║ Albanian/
║✰║ Arab/
║✰║ Armenian/
║✰║ Bengali/
║✰║ Catalan/
║✰║ Chinese/
║✰║ Croatian/
║✰║ Czech/
║✰║ Danish/
║✰║ Dutch/
║✰║ English/
║✰║ Australia/
║✰║ Uk/
║✰║ Us/
║✰║ Esperanto/
║✰║ Finnish/
║✰║ French/
║✰║ German/
║✰║ Greek/
║✰║ Hindi/
║✰║ Hungarian/
║✰║ Icelandic/
║✰║ Indonesia/
║✰║ Italia/
║✰║ Japanese/
║✰║ Khmer/
║✰║ Korean/
║✰║ Latin/
║✰║ Latvian/
║✰║ Macedonian/
║✰║ Malaysia/
║✰║ Norwegian/
║✰║ Polish/
║✰║ Portuguese/
║✰║ Romanian/
║✰║ Russian/
║✰║ Sarbian/
║✰║ Sinhala/
║✰║ Slovak/
║✰║ Spanish/
║✰║ Spain/
║✰║ Swadhili/
║✰║ Swedish/
║✰║ Tamil/
║✰║ Thai/
║✰║ Turki/
║✰║ Ukrainian/
║✰║ Vietnam/
║✰║  Welsh/
║╩═══NEXT PAGE═╦
║🃏║ ✰ {  Media  }
║🇲🇨║ ✰ {Translate}
║⚙️║ ✰ {    Set   }
║🏴║ ✰ {Helpbots}
║🔧║ ✰ {Settings}
║🔛║ ✰ {Setauto}
╚══╩══════╝
"""
KAC=[baim,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
mid = baim.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
ki6mid = ki6.getProfile().mid
ki7mid = ki7.getProfile().mid
ki8mid = ki8.getProfile().mid
ki9mid = ki9.getProfile().mid
ki10mid = ki10.getProfile().mid
Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki10mid]
admsa = ""
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'tagme':"Iyain Aja Biar Ceppet",
    'sider1':"Assalamualaikum",
    'joingc':"SΣLAMAT ÐATANG ÐI INÐOMAЯΣT",
    'leftgc':"SΣΣ YOU AGAIN",
    "stickerMention":False,
    'message':"""THANKS FOR ADD ME\n\nINSTAGRAM\n\nhttps://www.instagram.com/muhammadiwan09""",
    "lang":"JP",
    "comment":"Thanks For Add Me",
    "comment1":"❂•••••••••••••••••••••••••❂\n                  https://line.me/R/ti/p/fxsfamilia\n『☬C㊉ЯLD ƘILLΣЯ☬』",
    "commentOn":False,
    "Likeo n":True,
    "Wc on":True,
    "Left on":True,
    "alwayRead":False,
    "Removechat":False,
    "detectMention":False,    
    "kickMention":False,
    "cpp":True,
    "steal":False,
    'pap':{},
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "atjointicket":True,
    "potoMention":{},
    "prankName":True,
    "Sider":{},
    "cyduk":{},
    "pname":{},
    "pro_name":{},
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
settings = {
    "simiSimi":{}
    }
res = {
    'num':{},
    'us':{},
    'au':{},
    }
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
setTime = {}
setTime = wait2['setTime']
mulai = time.time() 
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read)
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items
def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }
     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()
     return image
def updateProfilePicture(self, path):
        file=open(path, 'rb')
        files = {
            'file': file
        }
        params = {
            'name': 'media',
            'type': 'image',
            'oid': self.profile.mid,
            'ver': '1.0',
        }
        data={
            'params': json.dumps(params)
        }
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/p/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Update profile picture failure.')
        return True
def sendVideo(self, to_, path):
        M = Message(to=to_, text=None, contentType = 2)
        M.contentMetadata = None
        M.contentPreview = None
        M2 = self.Talk.client.sendMessage(0,M)
        M_id = M2.id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'video',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        #print r
        if r.status_code != 201:
            raise Exception('Upload video failure.')
        return True
def sendVideoWithURL(self, to_, url):
        path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download video failure.')
        try:
            self.sendVideo(to_, path)
        except Exception as e:
            raise (e)
def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download audio failure.')
def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M2 = self.Talk.client.sendMessage(0,M)
        M_id = M2.id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise (e)
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def fullwidth(text):
    '''converts a regular string to Unicode Fullwidth
    Preconditions: text, a string'''
    translator = ''
    translator = translator.maketrans('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[]^_`{|}~' , '０１２３４５６７８９ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ！゛＃＄％＆（）＊＋、ー。／：；〈＝〉？＠［］＾＿‘｛｜｝～')
    return text.translate(translator)
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True
def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e
def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = baim.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = baim.getGroup(op.param1)
                if wait["Auto join"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            baim.rejectGroupInvitation(op.param1)
                        else:
                            baim.acceptGroupInvitation(op.param1)
			    G.preventJoinByTicket = False
			    acil.updateGroup(G)
			    Ticket = baim.reissueGroupTicket(op.param1)
			    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
			    ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
			    G.preventJoinByTicket = True
			    baim.updateGroup(G)
                    else:
                        baim.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        baim..rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace(" ",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KAC).kickoutFromGroup(op.param1, matched_list)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                acil.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                baim.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            baim.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = baim.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            baim.updateGroup(G)
                        except:
                            baim.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    baim.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                acil.like(url[25:58], url[66:], likeType=1001)
                ki.like(url[25:58], url[66:], likeType=1001)
                ki2.like(url[25:58], url[66:], likeType=1001)
                ki3.like(url[25:58], url[66:], likeType=1001)
                ki4.like(url[25:58], url[66:], likeType=1001)
                ki5.like(url[25:58], url[66:], likeType=1001)
                ki6.like(url[25:58], url[66:], likeType=1001)
                ki7.like(url[25:58], url[66:], likeType=1001)
                ki8.like(url[25:58], url[66:], likeType=1001)
                ki9.like(url[25:58], url[66:], likeType=1001)
                ki10.like(url[25:58], url[66:], likeType=1001)
                acil.comment(url[25:58], url[66:], wait["comment1"])
                ki.comment(url[25:58], url[66:], wait["comment1"])
                ki2.comment(url[25:58], url[66:], wait["comment1"])
                ki3.comment(url[25:58], url[66:], wait["comment1"])
                ki4.comment(url[25:58], url[66:], wait["comment1"])
                ki5.comment(url[25:58], url[66:], wait["comment1"])
                ki6.comment(url[25:58], url[66:], wait["comment1"])
                ki7.comment(url[25:58], url[66:], wait["comment1"])
                ki8.comment(url[25:58], url[66:], wait["comment1"])
                ki9.comment(url[25:58], url[66:], wait["comment1"])
                ki10.comment(url[25:58], url[66:], wait["comment1"])
#-----------------------------------------------
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = baim.getGroup(op.param1)
                    except:
                        try:
                            G = ki1.getGroup(op.param1)
                        except:
                            try:
                                G = ki2.getGroup(op.param1)
                            except:
                                try:
                                    G = ki3.getGroup(op.param1)
                                except:
                                    try:
                                        G = ki4.getGroup(op.param1)
				    except:
					try:
                                            G = ki5.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        acil.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                ki2.updateGroup(G)
                            except:
                                try:
                                    ki3.updateGroup(G)
                                except:
                                    try:
                                        ki4.updateGroup(G)
                                    except:
                                        try:
                                            ki5.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in Bots:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki5.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        ki.sendText(msg.to,text)
        if op.type == 26:
            msg = op.message
            if msg.to in settings["Simi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                baim.sendText(msg.to, "🤠" + data['result']['response'].encode('utf-8'))
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['detectMention'] == True:
                     contact = baim.getContact(msg.from_)
                     cName = contact.pictureStatus
                     balas = ["Ngomong aja Keless Gk Usah Pake Ngetag",cName + " Ngetag Gift Tikel Yaa..?",cName + " Nggak Usah Tag-Tag! Kalo Kangen Langsung Pc Aja","Dia Lagi Off", cName + " Kenapa Tag Saya?","Dia Lagi Tidur\nJangan Di Tag " + cName, "Jangan Suka Tag Gua " + cName, "Kamu Siapa " + cName + "?", "Ada Perlu Apa " + cName + "?","Woii " + cName + " Jangan Ngetag, Riibut!"]
                     balas1 = "Ini Dia Foto SI Pascol Yang Suka Ngetag...!"
                     ret_ = random.choice(balas)
                     image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention["MENTIONEES"]
                     for mention in mentionees:
                           if mention["M"] in mid:
                                  baim.sendImageWithURL(msg.to,ret_)
                                  msg.contentType = 13
                                  msg.contentMetadata = {'mid': msg.from_}
                                  baim.sendMessage(msg)
                                  baim.sendText(msg.to, wait["tagme"])
                                  break
            if "MENTION" in msg.contentMetadata.keys() != None:
            	if wait['Stickermention'] == True:
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention["MENTIONEES"]
                     for mention in mentionees:
                           if mention["M"] in mid:
                           	msg.contentType = 7
                           	msg.text = ''
                           	msg.contentMetadata = {
                                                  	   'STKPKGID': 1,
                                                  	   'STKTXT': '[]',
                                                  	   'STKVER': 100,
                                                  	   'STKID':110 
                                              		 }
                           	baim.sendText(msg.to, wait["tagme"])
                           	baim.sendMessage(msg)
                           	break
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Kickmention"] == True:
                     contact = baim.getContact(msg.from_)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in mid:
                                  baim.sendText(msg.to,"don't tag me")
                                  baim.kickoutFromGroup(msg.to,[msg.from_])
                                  break
            if msg.contentType == 13:
                if wait['Invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = baim.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             baim.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 baim.findAndAddContactsByMid(target)
                                 baim.inviteIntoGroup(msg.to,[target])
                                 baim.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      acil.sendText(msg.to,"Error")
                                      wait['invite'] = False
                                      break
            if wait["Alwayread"] == True:
                if msg.toType == 0:
                    baim.sendChatChecked(msg.from_,msg.id)
                else:
                    baim.sendChatChecked(msg.to,msg.id)
            if wait["Removechat"] == True:
                if msg.toType == 0:
                    baim.removeAllMessages(op.param2)
                else:
                    baim.removeAllMessages(op.param2)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        baim.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        acil.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        baim.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        baim.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        baim.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        baim.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        baim.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        baim.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    baim.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = acil.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = baim.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        baim.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = baim.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = baim.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        try:
                            baim.sendImageWithURL(msg.to, "http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        except:
                            cu = ""
                        baim.sendText(msg.to,"🎀═displayName═🎀\n✤[" + contact.displayName + "]✤\n🎀═MIDs═🎀\n✤[" + msg.contentMetadata["mid"] + "]✤\n🎀═StatusContact═🎀\n✤" + contact.statusMessage + "✤")
                        baim.sendText(msg.to,"LINKPROFILE\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\nLINKBERANDA\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    baim.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Sk bye"]: 
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
                gid = ki7.getGroupIdsJoined()
                gid = ki8.getGroupIdsJoined()
                gid = ki9.getGroupIdsJoined()
                gid = ki10.getGroupIdsJoined()
                for i in gid:
                  ki.leaveGroup(i)
                  ki2.leaveGroup(i)
                  ki3.leaveGroup(i)
                  ki4.leaveGroup(i)
                  ki5.leaveGroup(i)
                  ki6.leaveGroup(i)
                  ki7.leaveGroup(i)
                  ki8.leaveGroup(i)
                  ki9.leaveGroup(i)
                  ki10.leaveGroup(i)
                if wait["lang"] == "JP":
                  random.choice(KAC).sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh selfbot...!!!\nMakasih...!!!")
                else:
                  baim.sendText(msg.to,"He declined all invitations")
#--------------------------
            elif msg.text in ["Leaveallgroup"]: 
                gid = baim.getGroupIdsJoined()
                for i in gid:
                  acil.leaveGroup(i)
                if wait["lang"] == "JP":
                  baim.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh selfbot...!!!\nMakasih...!!!")
                else:
                  baim.sendText(msg.to,"He declined all invitations")
#----------------------------------------------
            elif "Sendgrup " in msg.text:
                    bctxt = msg.text.replace("Sendgrup ", "")
                    n = baim.getGroupIdsJoined()
                    for manusia in n:
                        baim.sendText(manusia, (bctxt))
            elif "Sendcontact " in msg.text:
					bctxt = msg.text.replace("Sendcontact ", "")
					t = ki.getAllContactIds()
					t = ki2.getAllContactIds()
					t = ki3.getAllContactIds()
					t = ki4.getAllContactIds()
					t = ki5.getAllContactIds()
					t = ki6.getAllContactIds()
					t = ki7.getAllContactIds()
					t = ki8.getAllContactIds()
					t = ki9.getAllContactIds()
					t = ki10.getAllContactIds()
					for manusia in t:
						ki.sendText(manusia,(bctxt))
						ki2.sendText(manusia,(bctxt))
						ki3.sendText(manusia,(bctxt))
						ki4.sendText(manusia,(bctxt))
						ki5.sendText(manusia,(bctxt))
						ki6.sendText(manusia,(bctxt))
						ki7.sendText(manusia,(bctxt))
						ki8.sendText(manusia,(bctxt))
						ki9.sendText(manusia,(bctxt))
						ki10.sendText(manusia,(bctxt))
            elif "Sendpm " in msg.text:
                    bctxt = msg.text.replace("Sendpm ", "")
                    t = baim.getAllContactIds()
                    for manusia in t:
                        baim.sendText(manusia, (bctxt))
            elif "Virus" in msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "BEBAS,'"}
                acil.sendMessage(msg)
            elif msg.text in ["Stafflist"]:
              if Bots == []:
                  baim.sendText(msg.to,"The Friends is empty")
              else:
                  baim.sendText(msg.to,"Tunggu...")
                  mc = "||===FRIENDLIST===||\n=====================\n"
                  for mi_d in Bots:
                      mc += "★" +acil.getContact(mi_d).displayName + "\n"
                  baim.sendText(msg.to,mc)
                  print "[Command]Friendlist executed"                    
            elif "Youinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = acil.getContact(key1)
                cu = baim.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    baim.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    baim.sendText(msg.to,"Profile Picture " + contact.displayName)
                    baim.sendImageWithURL(msg.to,image)
                    baim.sendText(msg.to,"Cover " + contact.displayName)
                    baim.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif "Botak" in msg.text:
                group = baim.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*200 : (j+1)*200]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    ki.sendMessage(msg) 
                    

            elif "Github " in msg.text:
                    a = msg.text.replace("Github ","")
                    b = urllib.quote(a)
                    baim.sendText(msg.to,"「 Searching 」\n" "Type: GitHub Search\nStatus: Processing...")
                    baim.sendText(msg.to, "Title: " + a + "\nLink: https://github.com/search?utf8=✓&q="+b)
            elif 'playstore ' in msg.text.lower():
                    tob = msg.text.lower().replace('playstore ',"")
                    baim.sendText(msg.to,"Please wait...")
                    baim.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                    baim.sendText(msg.to,"This is link aplication")     
            elif "Wikipedia " in msg.text:
                  try:
                      wiki = msg.text.lower().replace("Wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      baim.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              baim.sendText(msg.to, pesan)
                          except Exception as e:
                              baim.sendText(msg.to, str(e))
            elif "Twitter " in msg.text:
                    a = msg.text.replace("Twitter ","")
                    b = urllib.quote(a)
                    baim.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Processing")
                    baim.sendText(msg.to, "https://www.twitter.com" + b)
                    baim.sendText(msg.to,"「 Searching 」\n" "Type:Search Info\nStatus: Success") 
            elif "Smule " in msg.text:
                    a = msg.text.replace("Smule ","")
                    b = urllib.quote(a)
                    baim.sendText(msg.to,"Searching to id smule..")
                    baim.sendText(msg.to, "Nama: "+b+"\nId smule: http://smule.com/" +b)
            elif "Google " in msg.text:
                    a = msg.text.replace("Google ","")
                    b = urllib.quote(a)
                    baim.sendText(msg.to,"Searching google..")
                    baim.sendText(msg.to, "Search: "+b+"\nsuccess: http://google.com/" +b)
	    elif "Xvideos " in msg.text:
		    a = msg.text.replace("Xvideos ","")
                    b = urllib.quote(a)
                    baim.sendText(msg.to,"Searching ....\n" "Type:Search Xvideos\nStatus: Processing")
                    baim.sendText(msg.to, "{ Xvideos search page }\n\nTitle: "+b+"\nSource : Xvideos\nhttp://xvideos.com/?k=" +b)
            elif "Picturl @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Picturl @","")
                _nametarget = _name.rstrip(' ')
                gs = baim.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    baim.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = baim.sendText.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            baim.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Coverurl @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Coverurl @","")
                _nametarget = _name.rstrip(' ')
                gs = baim.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    baim.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = baim.sendText.getContact(target)
                            cu = baim.sendText.channel.getCover(target)
                            path = str(cu)
                            baim.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"         
            elif msg.text in ["Pmfavorite"]:
                dj = baim.getFavoriteMids()
                kontak = baim.getContacts(dj)
                num = 1
                family = str(len(dj))
                msgs = "[List Favorite Friends Guys]"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\nTotal Friend : %i" % len(kontak)
                baim.sendText(msg.to, msgs)
            elif msg.text.lower()  == 'Set auto':
                   baim.sendText(msg.to,helpFun)
            elif msg.text.lower() == 'Help':
                if wait["lang"] == "JP":
                    baim.sendText(msg.to,helpMessage)
                else:
                    baim.sendText(msg.to,helpMessage)
            elif msg.text.lower() == 'Media':
                if wait["lang"] == "JP":
                    baim.sendText(msg.to,helpMedia)
                else:
                    baim.sendText(msg.to,helpMedia)
            elif msg.text.lower() == 'Helpbots':
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,helpself)
                else:
                    baim.sendText(msg.to,helpself)
            elif msg.text.lower() == 'Settings':
                if wait["lang"] == "JP":
                    baim.sendText(msg.to,helpset)
                else:
                    baim.sendText(msg.to,helpset)
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = baim.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    ki.updateGroup(group)
                else:
                    baim.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok👈")
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    group = baim.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    baim.updateGroup(group)
                else:
                    baim.sendText(msg.to,"Can not be used for groups other than")
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                baim.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                baim.findAndAddContactsByMid(midd)
                baim.inviteIntoGroup(msg.to,[midd])
            elif "Me" == msg.text:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': mid}
                       baim.sendMessage(msg)
                       eltime = time.time() - mulai
                       van = "Bot has been active "+waktu(eltime)
                       baim.sendText(msg.to,van) 
            elif "Mybots" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                baim.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                baim.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                baim.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                baim.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                baim.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                baim.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                baim.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                baim.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                baim.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki10mid}
                baim.sendMessage(msg)
            elif "Respon" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                ki7.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                ki8.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                ki9.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki10mid}
                ki10.sendMessage(msg)
                ki.sendText(msg.to,"AMAN TERKENDALI KOMANDAN 👮")
            elif "B1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "B2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
            elif "B3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif "B4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
            elif "B5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
            elif "B6" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg)
            elif "B7" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                ki7.sendMessage(msg)
            elif "B8" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                ki8.sendMessage(msg)
            elif "B9" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                ki9.sendMessage(msg)
            elif "B10" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki10mid}
                ki10.sendMessage(msg)
            elif "Creator" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ufce863f62f40706c01fa4a3c3c4cb096'}
                acil.sendMessage(msg)
            elif msg.text in ["Allgift","B1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift","i gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                baim.sendMessage(msg)

            elif msg.text in ["Allgift","B2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)

            elif msg.text in ["Allgift","B3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["Allgift","B4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki4.sendMessage(msg)
            elif msg.text in ["Allgift","B5 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki5.sendMessage(msg)
            elif msg.text in ["Allgift","B6 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                ki6.sendMessage(msg)
            elif msg.text in ["Allgift","B7 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                ki7.sendMessage(msg)
            elif msg.text in ["Allgift","B8 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '13'}
                msg.text = None
                ki8.sendMessage(msg)
            elif msg.text in ["Allgift","B9 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '11'}
                msg.text = None
                ki9.sendMessage(msg)
            elif msg.text in ["Allgift","B10 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki10.sendMessage(msg)
            elif msg.text in ["Spam gift"]:
				#if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '12'}
					msg.text = None
					ki.sendMessage(msg)
					ki2.sendMessage(msg)
					ki3.sendMessage(msg)
					ki4.sendMessage(msg)
					ki5.sendMessage(msg)
					ki6.sendMessage(msg)
					ki7.sendMessage(msg)
					ki8.sendMessage(msg)
					ki9.sendMessage(msg)
					ki10.sendMessage(msg)
            elif msg.text in ["Clink"]:
                if msg.toType == 2:
                    group = baim.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    baim.updateGroup(group)
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"URL open ô€¨ô€„Œ")
                    else:
                        baim.sendText(msg.to,"URL open ô€¨ô€„Œ")
                else:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"It can not be used outside the group👈")
                    else:
                        baim.sendText(msg.to,"Can not be used for groups other than")
            elif msg.text in ["Curl"]:
                if msg.toType == 2:
                    group = baimgetGroup(msg.to)
                    group.preventJoinByTicket = True
                    baim.updateGroup(group)
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"URL close 👈")
                    else:
                        baim.sendText(msg.to,"URL close 👈")
                else:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        baim.sendText(msg.to,"Can not be used for groups other than ")
            elif msg.text.lower() == 'ginfo':        
                    group = baim.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md ="✥GROUP NAME✥\n" + group.name + "\n\n✥GROUP ID✥\n✿" + group.id +"✿" "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\n✥TOTAL MEMBER✥\n" + str(len(group.members)) + " Orang" + "\n✥PENDINGAN✥\n" + str(len(group.invitee)) + " Orang"
                    baim.sendText(msg.to,md)
            elif "Mymid" == msg.text:
                baim.sendText(msg.to,mid)
            elif "B1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "B2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "B3 mid" == msg.text:
                ki3.sendText(msg.to,ki3mid)
            elif "B4 mid" == msg.text:
                ki4.sendText(msg.to,ki4mid)
            elif "B5 mid" == msg.text:
                ki5.sendText(msg.to,ki5mid)
            elif "B6 mid" == msg.text:
                ki6.sendText(msg.to,ki6mid)
            elif "B7 mid" == msg.text:
                ki7.sendText(msg.to,ki7mid)
            elif "B8 mid" == msg.text:
                ki8.sendText(msg.to,ki8mid)
            elif "B9 mid" == msg.text:
                ki9.sendText(msg.to,ki9mid)
            elif "B10 mid" == msg.text:
                ki10.sendText(msg.to,ki10mid)
            elif "All mid" == msg.text:
                baim.sendText(msg.to,mid)
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki6mid)
                ki7.sendText(msg.to,ki7mid)
                ki8.sendText(msg.to,ki8mid)
                ki9.sendText(msg.to,ki9mid)
                ki10.sendText(msg.to,ki10mid)
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                baim.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+acil.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Allname " in msg.text:
                string = msg.text.replace("Allname ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
                    baim.sendText(msg.to,"􀜁􀇔􏿿NAMA BOT BERHASIL DI TERAPKAN MENJADI\n👉" + string + "👈")
            elif "Allbio " in msg.text:
                string = msg.text.replace("Allbio ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki7.getProfile()
                    profile.statusMessage = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki8.getProfile()
                    profile.statusMessage = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki9.getProfile()
                    profile.statusMessage = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki10.getProfile()
                    profile.statusMessage = string
                    ki10.updateProfile(profile)
                    baim.sendText(msg.to,"􀜁􀇔􏿿SEMUA TELAH DI UPDATE BIO PROFILE\n👉" + string + "👈")
            elif "Mybio " in msg.text:
                string = msg.text.replace("Mybio ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = acil.getProfile()
                    profile.statusMessage = string
                    baim.updateProfile(profile)
                    baim.sendText(msg.to,"􀜁􀇔􏿿Update Bio\n👉" + string + "👈")
#------------------------------------------------------------------------------------------#
            elif "Cn " in msg.text:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = acil.getProfile()
                    profile.displayName = string
                    baim.updateProfile(profile)
                    baim.sendText(msg.to,"􀜁􀇔􏿿Update Names👉 " + string + "👈")
#---------------------------------------------------------
            elif "B1name " in msg.text:
                string = msg.text.replace("B1name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B2name " in msg.text:
                string = msg.text.replace("B2name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B3name " in msg.text:
                string = msg.text.replace("B3name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B4name " in msg.text:
                string = msg.text.replace("B4name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
#--------------------------------------------------------
            elif "B5name " in msg.text:
                string = msg.text.replace("B5name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"􀇔 􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "B6name " in msg.text:
                string = msg.text.replace("B6name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"􀜁􀇔􏿿Update Names��" + string + "👈")
#---------------------------------------------------------
            elif "B7name " in msg.text:
                string = msg.text.replace("B7name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#---------------------------------------------------------
            elif "B8name " in msg.text:
                string = msg.text.replace("B8name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                    ki8.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#---------------------------------------------------------
            elif "B9name " in msg.text:
                string = msg.text.replace("B9name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                    ki9.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#---------------------------------------------------------
            elif "B10name " in msg.text:
                string = msg.text.replace("B10name ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
                    ki10.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")

#--------------------------------------------------------
            elif "Contact " in msg.text:
                mmid = msg.text.replace("Contact ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                baim.sendMessage(msg)
            elif msg.text in ["Allprotect on"]:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Protection Enable 􀜁􀇔􏿿✔")
                    else:
                        baim.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Protection Enable􀜁✔􀇔􏿿")
                    else:
                        baim.sendText(msg.to,"It is already On ✔")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Link Protection Enable 􀜁􀇔􏿿✔")
                    else:
                        baim.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Link Protect Enable􀜁􏿿")
                    else:
                        baim.sendText(msg.to,"It is already On ô€¨")
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Invite Protect Enable 􀜁􀇔􏿿✔")
                    else:
                        baim.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Invite Protect Enable􀜁􀇔􏿿")
                    else:
                        baim.sendText(msg.to,"It is already On ¨")
                    if msg.to in wait['pname']:
                        baim.sendText(msg.to,"TURN ON")
                    else:
                        baim.sendText(msg.to,"ALREADY ON")
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = baim.getGroup(msg.to).name
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Cancel Protection Enable 􀜁􀇔􏿿✔")
                    else:
                        baim.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already ON􀜁􀇔􏿿✔")
                    else:
                        baim.sendText(msg.to,"It is already On ✔")
#=====================================================================================
            elif msg.text in ["Allprotect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Protection Disable ✔")
                    else:
                        baim.sendText(msg.to,"sudah dimatikan ✔")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already close")
                    else:
                        baim.sendText(msg.to,"It is already open ✔")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Link Protection Disable ✖")
                    else:
                        baim.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already close✖")
                    else:
                        baim.sendText(msg.to,"It is already open ✔")
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Invite Protection Disable ✖")
                    else:
                        baim.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already close✖")
                    else:
                        baim.sendText(msg.to,"It is already open ✔")
                    if msg.to in wait['pname']:
                        baim.sendText(msg.to,"TURN OFF")
                        del wait['pname'][msg.to]
                    else:
                        baim.sendText(msg.to,"ALREADY OFF")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Cancel Protection Disable ✖")
                    else:
                        baim.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already close✖")
                    else:
                        baim.sendText(msg.to,"It is already open ✔")  

#=====================================================================================   
            elif msg.text.lower() == 'Contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Sudah On")
                    else:
                        baim.sendText(msg.to,"It is already open")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already open ✔")
                    else:
                        baim.sendText(msg.to,"It is already open 􀜁􀇔􏿿")
            elif msg.text.lower() == 'Contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"sudah off ✖")
                    else:
                        baim.sendText(msg.to,"It is already off ✖")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"off already")
                    else:
                        baim.sendText(msg.to,"already Close ✔")
            elif msg.text in ["Pro on"]:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Protection Enable 􀜁??􏿿✔")
                    else:
                        baim.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Protection Enable􀜁✔􀇔􏿿")
                    else:
                        baim.sendText(msg.to,"It is already On ✔")
            elif msg.text in ['Prolink on']:
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Link Protection Enable 􀜁􀇔􏿿✔")
                    else:
                        baim.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Link Protect Enable􀜁􏿿")
                    else:
                        baim.sendText(msg.to,"It is already On ô€¨")
            elif msg.text in ['Proinvite on']:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Invite Protect Enable 􀜁􀇔􏿿✔")
                    else:
                        baim.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Invite Protect Enable􀜁􀇔􏿿")
                    else:
                        baim.sendText(msg.to,"It is already On ¨")
            elif msg.text in ['Procancel on']:
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Cancel Protection Enable 􀜁􀇔􏿿✔")
                    else:
                        baim.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already ON􀜁􀇔􏿿✔")
                    else:
                        baim.sendText(msg.to,"It is already On ✔")
            elif msg.text.lower() == 'Join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Ini sudah on􀜁􀇔􏿿✔")
                    else:
                        baim.sendText(msg.to,"Hal ini sudah terbuka ✔")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already ON􀜁􀇔􏿿✔")
                    else:
                        baim.sendText(msg.to,"It is already On ✔")
            elif msg.text.lower() == 'Blocklist':
                blockedlist = acil.getBlockedContactIds()
                baim.sendText(msg.to, "Please wait...")
                kontak = baim.getContacts(blockedlist)
                num=1
                msgs="✖User Blocked List✖\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                acil.sendText(msg.to, msgs)
            elif msg.text.lower() == 'Join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Auto Join Already Off✔")
                    else:
                        baim.sendText(msg.to,"Auto Join set off✔")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already close✔")
                    else:
                        baim.sendText(msg.to,"It is already open ✔")
            elif msg.text in ["Pro off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Protection Disable ✔")
                    else:
                        baim.sendText(msg.to,"sudah dimatikan ✔")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already close")
                    else:
                        baim.sendText(msg.to,"It is already open ✔")
            elif msg.text in ["Prolink off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Link Protection Disable ✖")
                    else:
                        baim.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already close✖")
                    else:
                        baim.sendText(msg.to,"It is already open ✔")
            elif msg.text in ["Proinvite off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Invite Protection Disable ✖")
                    else:
                        baim.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already close✖")
                    else:
                        baim.sendText(msg.to,"It is already open ✔")
            elif msg.text in ["Procancel off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Cancel Protection Disable ✖")
                    else:
                        baim.sendText(msg.to,"sudah dimatikan ✖")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already close✖")
                    else:
                        baim.sendText(msg.to,"It is already open ✔")
            elif "Join:" in msg.text:
                try:
                    strnum = msg.text.replace("Join:","")
                    if strnum == "off":
                        wait["Cancel"]["on"] = False
                        if wait["lang"] == "JP":
                            baim.sendText(msg.to,"Itu off undangan ditolak✖\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan✖")
                        else:
                            baim.sendText(msg.to,"Off undangan ditolak✖Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["Cancel"]["on"] = True
                        if wait["lang"] == "JP":
                            baim.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis✔")
                        else:
                            baim.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"")
                    else:
                        baim.sendText(msg.to,"Weird value✖")
            elif msg.text in ["Leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"on􀇔􏿿✔")
                    else:
                        baim.sendText(msg.to,"Sudah terbuka 􀜁􀇔✔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Done􀜁􀇔􏿿✔")
                    else:
                        baim.sendText(msg.to,"Is already open􀇔􏿿✔")
            elif msg.text in ["Leave off"]:
                if wait["Leave room"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"off􀜁􀇔􏿿✖")
                    else:
                        baim.sendText(msg.to,"Sudah off􀜁􀇔􏿿✖")
                else:
                    wait["leave room"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Done􀇔􏿿✔")
                    else:
                        baim.sendText(msg.to,"Is already close􀇔􏿿✔")
            elif msg.text in ["Share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Done 􀜁􀇔􏿿✔")
                    else:
                        baim.sendText(msg.to,"Hal ini sudah terbuka ✖")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"on ✔")
                    else:
                        baim.sendText(msg.to,"on ✔")
            elif msg.text in ["Share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Done􀇔􏿿✔")
                    else:
                        baim.sendText(msg.to,"It is already turned off 􀜁􀇔􏿿✔")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"Off ✖")
                    else:
                        baim.sendText(msg.to,"Off ✖")
            elif msg.text.lower() == 'set':
                md = "╔▬▬ㄅꀤngŁҾ ㉿ꀤŁŁҾr▬▬╗\n║▬▬▬ㄅ▬▬㉿▬▬▬║\n"
                if wait["Like on"] == True: md+="║☆║Like on➡️📱\n"
                else: md+="║☆║Like off➡️📴\n"
                if wait["Wc on"] == True: md+="║☆║Welcome on➡️📱\n"
                else: md+="║☆║Welcome off➡️📴\n"
                if wait["Left on"] == True: md+="║☆║Left on➡️📱\n"
                else: md+="║☆║Left:OFF➡️📴\n"
                if wait["DetectMention"] == True: md+="║☆║Respon on➡️📱\n"
                else: md +="║☆║Respon off➡️📴\n"
                if wait["StickerMention"] == True: md+="║☆║Stickertag on➡️📱\n"
                else: md +="║☆║Stickertag off➡️📴\n"
                if settings["simiSimi"] == True: md+="║☆║Simisimi on➡️📱\n"
                else: md+="║☆║Simisimi off➡️📴\n"
                if wait["Alwayread"] == True: md+="║☆║Auto read on➡️📱\n"
                else: md+="║☆║Auto read off ➡️📴\n"
                if wait["Sider"] == True: md+="║☆║Sider on➡️📱\n"
                else: md+="║☆║Sider off➡️📴\n"
                if wait["KickMention"] == True: md+="║☆║Notag on➡️📱\n"
                else:md+="║☆║Notag off➡️📴\n"
                if wait["Contact"] == True: md+="║☆║Contact on➡️📱\n"
                else: md+="║☆║Contact:OFF➡️📴\n"
                if wait["AutoJoin"] == True: md+="║☆║Join on➡️📱\n"
                else: md +="║☆║Join off➡️📴\n"
                if wait["Auto cancel"]["on"] == True:md+="║☆║Cancel:" + str(wait["autoCancel"]["members"]) + "➡️📱\n"
                else: md+= "║☆║Canceloff➡️📴\n"
                if wait["Leave room"] == True: md+="║☆║Leave on➡️📱\n"
                else: md+="║☆║Leave off➡️📴\n"
                if wait["timeline"] == True: md+="║☆║Share on➡️📱\n"
                else:md+="║☆║Share off➡️📴\n"
                if wait["Auto add"] == True: md+="║☆║Add on➡️📱\n"
                else:md+="║☆║Add off➡️??\n"
                if wait["Comment on"] == True: md+="║☆║Com on➡️📱\n"
                else:md+="║☆║Com off➡️📴\n║▬║❨◄▬▬▬►❩\n║☆║◄═PROTECTION═►\n║▬║▬ֆأӣᏩӀҼ ҠأӀӀҼԻ▬╣\n"
                if wait["Protect"] == True: md+="║☆║Pro:ON➡️📱\n"
                else:md+="║☆║Pro off➡️📴\n"
                if wait["Linkprotect"] == True: md+="║☆║ProtectQr on➡️📱\n"
                else:md+="║☆║ProtectQr off➡️📴\n"
                if wait["Inviteprotect"] == True: md+="║☆║Proinvite on➡️📱\n"
                else:md+="║☆║Proinvite off➡️📴\n"
                if wait["Cancelprotect"] == True: md+"║☆║Procancel on➡️📱\n"
                else:md+="║☆║Procanceloff➡️📴\n"
                if wait["pname"] == True: md+="║☆║Namelock on➡️📱\n"
                else: md+="║☆║Namelock off➡️📴\n"   
                acil.sendText(msg.to,md + "║▬▬▬ㄅ▬▬㉿▬▬▬║\n╚▬▬ㄅꀤngŁҾ ㉿ꀤŁŁҾr▬▬╝")
            elif "Creatorgrup" == msg.text:
                try:
                    group = baim.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    GS = acil.getContact(msg.to)
                    baim.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    baim.sendMessage(M)
                    W = baim.getContact(msg.to)
                    baim.sendText(msg.to,"old user")
            elif cms(msg.text,["Add"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u03625388921e6baa1e0fc85003b8fdef'}
                baim.sendText(msg.to,"❂•••••••••✧••••••••••❂")
                baim.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ue9474acfc84b8d5fcb7cca3d98dc40af'}
                baim.sendMessage(msg)
                baim.sendText(msg.to,"❂••••••••✰•✰••••••••❂")
            elif "Tagme: " in msg.text:
                c = msg.text.replace("Tagme: ","")
                if c in [""," ","\n",None]:
                    baim.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["tagme"] = c
                    baim.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif "Welcome: " in msg.text:
                c = msg.text.replace("Welcome: ","")
                if c in [""," ","\n",None]:
                    baim.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["Join gc"] = c
                    baim.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif "Left: " in msg.text:
                c = msg.text.replace("Left: ","")
                if c in [""," ","\n",None]:
                    acil.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["leftgc"] = c
                    baim.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif "Sider: " in msg.text:
                c = msg.text.replace("Sider: ","")
                if c in [""," ","\n",None]:
                    baim.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["sider1"] = c
                    baim.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif "Setrespon: " in msg.text:
                c = msg.text.replace("Setrespon: ","")
                if c in [""," ","\n",None]:
                    baim.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["responName"] = c
                    baim.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif "Cekresponse" in msg.text:
            	baim.sendText(msg.to,"👇Respon saat di tag👇\n" + wait["tagme"])
            	baim.sendText(msg.to,"👇Respon saat di add👇\n" + wait["comment"])
            	baim.sendText(msg.to,"👇Respon saat member join👇\n" + wait["joingc"])
            	baim.sendText(msg.to,"👇Respon saat member left👇\n" + wait["leftgc"])
            	baim.sendText(msg.to,"👇Respon saat member readchat👇\n" + wait["sider1"])
            	baim.sendText(msg.to,"👇Respon saat member memanggil👇\n" + wait["responName"])
            	baim.sendText(msg.to,"👇Respon di autolike👇\n" + wait["comment1"] + "\n\nHAL INI TIDAK DAPAT DI UBAH SESUAI HAK CIPTA\nCREATOR::SINGLEKILLER")
            elif msg.text in ["Left:on"]:
                if wait["leftOn"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Done")
                else:
                    wait["Left on"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Already")
            elif msg.text in ["Left off"]:
                if wait["leftOn"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Done")
                else:
                    wait["leftOn"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Already") 
            elif msg.text in ["Welcome on"]:
                if wait['wcOn'] == True:
                    if wait["lang"] == "JP": 
                        baim.sendText(msg.to,"sudah ON")
                else:
                    wait["Wc on"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"already ON")
            elif msg.text in ["Welcome off"]:
                if wait['wcOn'] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Sudah off")
                else:
                    wait['Wc on'] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already OFF")
            elif msg.text.lower() == 'group id':
                gid = baim.getGroupIdsJoined()
                h = "❂•••••••••ℓ ι ѕ т  ι ∂  g я σ υ ρ••••••••••❂\n "
                for i in gid:
                    h += "[%s]:%s\n" % (baim.getGroup(i).name,i)
                baim.sendText(msg.to,h)
            elif msg.text in ["Gcancelall"]:
                gid = baim.getGroupIdsInvited()
                for i in gid:
                    baim.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    baim.sendText(msg.to,"Success menolak semua undangan")
                else:
                    baim.sendText(msg.to,"He declined all invitations")
            elif msg.text in ["Add:on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Already On✔")
                    else:
                        baim.sendText(msg.to,"Already On✔")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Already On✔")
                    else:
                        baim.sendText(msg.to,"Already On✔")
            elif msg.text in ["Add:off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Hal ini sudah off✖")
                    else:
                        baim.sendText(msg.to,"Hal ini sudah dimatikan✖")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Already Off✖")
                    else:
                        baim.sendText(msg.to,"Untuk mengaktifkan-off✖")
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                baim.sendText(msg.to,"✨We changed the message✨")
            elif "Help set:" in msg.text:
                wait["help"] = msg.text.replace("Help set:","")
                baim.sendText(msg.to,"✨We changed the Help✨")
            elif "Msg add-" in msg.text:
                wait["message"] = msg.text.replace("Pesan add-","")
                if wait["lang"] == "JP":
                    baim.sendText(msg.to,"✨Kami mengubah pesan✨")
                else:
                    baim.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message confirm"]:
                if wait["lang"] == "JP":
                    baim.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    baim.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    baim.sendText(msg.to,"I changed the language to engglis✔")
                else:
                    wait["lang"] = "JP"
                    baim.sendText(msg.to,"I changed the language to indonesia✔")
            elif "Message set: " in msg.text:
                c = msg.text.replace("Message set: ","")
                if c in [""," ","\n",None]:
                    baim.sendText(msg.to,"Is a string that can not be changed✔")
                else:
                    wait["comment"] = c
                    baim.sendText(msg.to,"✨This has been changed✨\n\n" + c)
            elif msg.text in ["Comment:on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Aku berada di✔")
                    else:
                        baim.sendText(msg.to,"To open✔")
                else:
                    wait["Comment on"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"✔")
                    else:
                        baim.sendText(msg.to,"✔")
            elif msg.text in ["Com off"]:
                if wait["Comment on"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Hal ini sudah off ✖")
                    else:
                        baim.sendText(msg.to,"It is already turned off ✖")
                else:
                    wait["Comment on"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Off✖")
                    else:
                        baim.sendText(msg.to,"To turn off✖")
            elif msg.text in ["Com","Comment"]:
                baim.sendText(msg.to,"✨Auto komentar saat ini telah ditetapkan sebagai berikut✨\n\n" + str(wait["comment"]))
            elif msg.text in ["Glink","Url"]:
                if msg.toType == 2:
                    g = baim.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        baim.updateGroup(g)
                    gurl = baim.reissueGroupTicket(msg.to)
                    acil.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        baim.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif "gurl+" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl+","")
                    gurl = acil.reissueGroupTicket(gid)
                    acil.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    baim.sendText(msg.to,"ã‚°ãƒ«ãƒ¼ãƒ—ä»¥å¤–ã§ã¯ä½¿ç”¨ã§ãã¾ã›ã‚“👈")

            elif "gurl" in msg.text:
                if msg.toType == 1:
                    tid = msg.text.replace("gurl","")
                    turl = ki.getUserTicket(tid)
                    ki.sendText(msg.to,"line://ti/p" + turl)
                else:
                    ki.sendText(msg.to,"error")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = baim.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        acil.updateGroup(x)
                    gurl = baim.reissueGroupTicket(msg.to)
                    baim.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Can't be used outside the group")
                    else:
                        baim.sendText(msg.to,"Not for use less than group")
#                else:
#                    baim.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Comban"]:
                wait["wblack"] = True
                baim.sendText(msg.to,"pleaѕe ѕend conтacтѕ ғroм тнe perѕon yoυ wanт тo add тo тнe вlacĸlιѕт…”✚")
            elif msg.text in ["Comban del"]:
                wait["dblack"] = True
                baim.sendText(msg.to,"pleaѕe ѕend conтacтѕ ғroм тнe perѕon yoυ wanт тo add ғroм тнe вlacĸlιѕт…”✚")
            elif msg.text in ["Comban cek"]:
                if wait["commentBlack"] == {}:
                    baim.sendText(msg.to,"noтнιng ιn тнe вlacĸlιѕт✖")
                else:
                    baim.sendText(msg.to,"The following is a blacklist✔")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +baim.getContact(mi_d).displayName + "\n"
                    baim.sendText(msg.to,mc)
            elif msg.text in ["Like:on","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Done")
                else:
                    wait["Like on"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Already")
                        
            elif msg.text in ["Like off","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Already")
            elif "Namelock on" in msg.text:
               # if msg.from_ in admin or owner:
                    if msg.to in wait['pname']:
                        baim.sendText(msg.to,"TURN ON")
                    else:
                        baim.sendText(msg.to,"ALREADY ON")
                        wait['pname'][msg.to] = True
                        wait['pro_name'][msg.to] = baim.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
               # if msg.from_ in admin or owner:
                    if msg.to in wait['pname']:
                        baim.sendText(msg.to,"TURN OFF")
                        del wait['pname'][msg.to]
                    else:
                        baim.sendText(msg.to,"ALREADY OFF")                        
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                baim.sendText(msg.to,"BOT API SIMISIMI TURN ON")
                ki.sendText(msg.to,"already turn active")
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                baim.sendText(msg.to,"BOT API SIMISIMI TURN OFF")
                ki.sendText(msg.to,"already non active")
            elif msg.text in ["Read on","Read on"]:
                if wait['alwayRead'] == True:
                    if wait["alwayRead"] == "JP": 
                        baim.sendText(msg.to,"Auto Sider ON")
                else:
                    wait["Alwayread"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already ON")
            elif msg.text in ["Read off","Read:off"]:
                if wait['alwayRead'] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Auto Sider OFF")
                else:
                    wait['alwayRead'] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already OFF auto read")
            elif msg.text in ["Deletechat"]:
                if wait['Removechat'] == True:
                    if wait["Removechat"] == "JP": 
                        baim.sendText(msg.to,"Success!!!")
                if wait['Removechat'] == False:
                    if wait["lang"] == "JP":
                        pass
            elif "Sider on" in msg.text:
	#      if msg.toType == 2:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                baim.sendText(msg.to,"Sider Telah On")
            elif "Sider off" in msg.text:
	#      if msg.toType == 2:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    baim.sendText(msg.to, "Sider Off")
                else:
                    baim.sendText(msg.to, "Assalamualaikum")
            elif msg.text in ["Autorespon on","Autorespon:on","Respon on","Respon:on"]:
                if wait["detectMention"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Respon on")
                else:
                    wait["detectMention"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"αℓяєα∂у OƝ")
            elif msg.text in ["Respon off"]:
                if wait["detectMention"] == False:
                    if wait["lang"] == "JP":
                        baimsendText(msg.to,"Respon Off")
                else:
                    wait["detectMention"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"αℓяєα∂у OƑƑ")
                        
            elif msg.text in ["Respon1 on"]:
            	if wait["detectMention"] == True: 
		             wait["detectMention1"] == True:
                    wait["detectMention2"] == False
                    wait["detectMention3"] == False
                    wait["kickMention"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Respon1 on")
                else:
                    wait["detectMention"] = True
                    wait["detectMention1"] == True:
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"αℓяєα∂у OƝ")
            
            elif msg.text in ["Respon1 off"]:
                if wait["detectMention"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Respon1 Off")
                else:
                    wait["detectMention"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"αℓяєα∂у OƑƑ")
  
            elif msg.text in ["Respon2 on"]:
                if wait["detectMention"] == True: 
		             wait["detectMention1"] == True:
                    wait["detectMention2"] == False
                    wait["detectMention3"] == False
                    wait["kickMention"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Respon2 on")
                else:
                    wait["detectMention"] = True
                    wait["detectMention1"] == True:
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"αℓяєα∂у OƝ")

            elif msg.text in ["Respon2 off"]:
                if wait["detectMention"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Respon2 Off")
                else:
                    wait["detectMention"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"αℓяєα∂у OƑƑ")

             elif msg.text in ["Respon3 on"]:
                 if wait["detectMention"] == True: 
		             wait["detectMention1"] == True:
                    wait["detectMention2"] == False
                    wait["detectMention3"] == False
                    wait["kickMention"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Respon3 on")
                else:
                    wait["detectMention"] = True
                    wait["detectMention1"] == True:
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"αℓяєα∂у OƝ")

            elif msg.text in ["Respon3 off"]:
                if wait["detectMention"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"Respon3 Off")
                else:
                    wait["detectMention"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"αℓяєα∂у OƑƑ")
         
            elif msg.text in ["Notag on"]:
                if wait["kickMention"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"☠️Ɖ₳₦₲ɆɌ ₮₳₲ ԞƗ€Ԟ Ø₦☠️")
                else:
                    wait["Kick mention"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"already ON")
            elif msg.text in ["Notag:off"]:
                if wait["kickMention"] == False:
                   if wait["lang"] == "JP":
                        ki.sendText(msg.to,"$ɆⱠ₣ ₱ɌØ₮Ɇ€₮ ₮₳₲ Ø₣₣✔")
                else:
                    wait["kickMention"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"already turn OF")
            elif msg.text.lower() == 'Clock on':
                if wait["clock"] == True:
                    baim.sendText(msg.to,"Sudah On")
                else:
                    wait["Clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = baim.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    baim.updateProfile(profile)
                    baim.sendText(msg.to,"Jam on✔")
            elif msg.text in ["Stickertag:on"]:
                if wait["stickerMention"] == True:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"sudah on")
                else:
                    wait["Sticker mention"] = True
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already ON")
            elif msg.text in ["Stickertag:off"]:
                if wait["stickerMention"] == False:
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"sudah off")
                else:
                    wait["stickerMention"] = False
                    if wait["lang"] == "JP":
                        baim.sendText(msg.to,"already OFF")
            elif msg.text.lower() == 'Clock off':
                if wait["clock"] == False:
                    baim.sendText(msg.to,"Hal ini sudah off✖")
                else:
                    wait["clock"] = False
                    baim.sendText(msg.to," Dimatikan ✔")
            elif "Clockname " in msg.text:
                n = msg.text.replace("Jam say ","")
                if len(n.decode("utf-8")) > 30:
                    baim.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    baim.sendText(msg.to,"Ini telah diubah✔\n\n" + n)
            elif msg.text in ["Translate"]:
					if wait["lang"] == "JP":
						baim.sendText(msg.to,translateMessage)
					else:
						baim.sendText(msg.to,helpt)
            elif msg.text.lower() == 'Update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = baim.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    baim.updateProfile(profile)
                    baim.sendText(msg.to,"Diperbarui✔")
                else:
                    acil.sendText(msg.to,"✨Silahkan Aktifkan Nama✨")
            elif ("Fuck " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           baim.kickoutFromGroup(msg.to,[target])
                       except:
                           baim.sendText(msg.to,"Error")
            elif ("Kick1 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki.kickoutFromGroup(msg.to,[target])
                       except:
                           ki.sendText(msg.to,"Error")
            elif ("Kick2 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki2.kickoutFromGroup(msg.to,[target])
                       except:
                           ki2.sendText(msg.to,"Error")
            elif ("Kick3 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki3.kickoutFromGroup(msg.to,[target])
                       except:
                           ki3.sendText(msg.to,"Error")
            elif ("Kick4 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki4.kickoutFromGroup(msg.to,[target])
                       except:
                           ki4.sendText(msg.to,"Error")
            elif ("Kick5 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki5.kickoutFromGroup(msg.to,[target])
                       except:
                           ki5.sendText(msg.to,"Error")
            elif ("Kick6 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki6.kickoutFromGroup(msg.to,[target])
                       except:
                           ki6.sendText(msg.to,"Error")
            elif ("Kick7 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki7.kickoutFromGroup(msg.to,[target])
                       except:
                           ki7.sendText(msg.to,"Error")
            elif ("Kick8 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki8.kickoutFromGroup(msg.to,[target])
                       except:
                           ki8.sendText(msg.to,"Error")
            elif ("Kick9 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki9.kickoutFromGroup(msg.to,[target])
                       except:
                           ki9.sendText(msg.to,"Error")
            elif ("Kick10 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki10.kickoutFromGroup(msg.to,[target])
                       except:
                           ki10.sendText(msg.to,"Error")
            elif ("Sc " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   key = baim.getContact(key1)
                   baim.sendText(msg.to,"" +  key1)

            elif "Bro " in msg.text:
                       nk0 = msg.text.replace("Bro ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = baim.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    baim.sendText(msg.to,"Good Bye")
#-----------------------------------------------------------
            elif ("Bye " in msg.text):
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      random.choice(KAC).kickoutFromGroup(msg.to,[target])
                   except:
                      pass


            elif ("Ban " in msg.text):
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      baim.sendText(msg.to,"Succes Banned")
                   except:
                      pass

            elif msg.text in ["Mygroups"]:
                 gid = baim.getGroupIdsJoined()
                 h = ""
                 for i in gid:
                  h += "[⛓️] %s \n" % (baim.getGroup(i).name + " | 🗜️Members : " + str(len (baim.getGroup(i).members)))
                 baim.sendText(msg.to, "☆「Group List」☆\n"+ h +"🗜️Total Group : " +str(len(gid)))

#----------------------------------------------------------
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = baim.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        baim.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                baim.sendText(msg.to,"Target Unlocked")
                            except:
                                baim.sendText(msg.to,"Error")

            elif "Ban " in msg.text:
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = baim.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									baim.sendText(msg.to,"Target Locked")
                                except:
                                    baim.sendText(msg.to,"Error")

            elif "Unban " in msg.text:
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = baim.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									baim.sendText(msg.to,"Target Unlocked")
                                except:
                                    baim.sendText(msg.to,"Error")
            elif "Id " in msg.text:
                msgg = msg.text.replace("Id ",'')
                conn = baim.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    baim.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    baim.sendMessage(msg)
#_________________________________________________________________________
            elif 'Ig ' in msg.text.lower():
              #if msg.from_ in admin:
                try:
                    instagram = msg.text.lower().replace("ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "≡≡≡≡≡≡I∏ЅƬΔGΓΔΜ I∏FΘ ƱЅΣΓ≡≡≡≡≡≡\n"
                    details = "\n≡≡≡≡≡≡I∏ЅƬΔGΓΔΜ I∏FΘ ƱЅΣΓ≡≡≡≡≡≡"
                    baim.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    baim.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	baim.sendText(msg.to, str(njer))
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    baim.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif msg.text in ["Kalender","Time","Waktu"]:
                       tz = pytz.timezone("Asia/Jakarta")
                       timeNow = datetime.now(tz=tz)
                       day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                       hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                       bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                       hr = timeNow.strftime("%A")
                       bln = timeNow.strftime("%m")
                       for i in range(len(day)):
                           if hr == day[i]: hasil = hari[i]
                       for k in range(0, len(bulan)):
                           if bln == str(k): bln = bulan[k-1]
                       rst = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                       baim.sendText(msg.to, rst)
#==============================================================================#

                
            elif msg.text.lower() == 'Runtime':
                eltime = time.time() - mulai
                van = "ϐᴏᴛ ʜᴀṩ ʙᴇᴇɴ ᴀᴄᴛɪᴠᴇ "+waktu(eltime)
                baim.sendText(msg.to,van) 
                
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = baim.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    baim.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = acil.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            baim.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = acil.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                baim.sendMessage(msg)
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = baim.getContact(key1)
                cu = baim.channel.getCover(key1)
                try:
                    baim.sendText(msg.to, "≡≡≡≡≡[dïšpιαψηαmε]≡≡≡≡≡\n" + contact.displayName)
                except:
                    baim.sendText(msg.to, "≡≡≡≡≡[dïšpιαψηαmε]≡≡≡≡≡\n" + contact.displayName)
            elif msg.text in ["Myname"]:
                    h = baim.getContact(mid)
                    baim.sendText(msg.to,"≡≡≡≡≡[dïšpιαψηαmε]≡≡≡≡≡\n" + h.displayName)
            elif msg.text in ["Mybio"]:
                    h = baim.getContact(mid)
                    baim.sendText(msg.to,"≡≡≡≡≡[š†α†ušmεššαgε]≡≡≡≡≡\n" + h.statusMessage)
            elif msg.text in ["Mypict"]:
                    h = baim.getContact(mid)
                    baim.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid"]:
                    h = baim.getContact(mid)
                    baim.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = baim.getContact(mid)
                    baim.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Mycover"]:
                    h = baim.getContact(mid)
                    cu = baim.channel.getCover(mid)          
                    path = str(cu)
                    baim.sendImageWithURL(msg.to, path)
            elif msg.text in ["Urlcover"]:
                    h = baim.getContact(mid)
                    cu = baim.channel.getCover(mid)          
                    path = str(cu)
                    baim.sendText(msg.to, path)
            elif "Getmid @" in msg.text:
                _name = msg.text.replace("Getmid @","")
                _nametarget = _name.rstrip(' ')
                gs = baim.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        baim.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "Setimage: " in msg.text:
                wait["pap"] = msg.text.replace("Setimage: ","")
                baim.sendText(msg.to, "Pap telah di Set")
            elif msg.text in ["Papimage","Papim","Pap"]:
                baim.sendImageWithURL(msg.to,wait["pap"])
            elif "Setvideo: " in msg.text:
                wait["pap"] = msg.text.replace("Setvideo: ","")
                baim.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in ["Papvideo","Papvid"]:
                baim.sendVideoWithURL(msg.to,wait["pap"])
#=========================
#-----------------------------------------------------------
            elif msg.text == "Check":
                    baim.sendText(msg.to, "Check Yang nyimak")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print wait2

            elif 'Copy ' in msg.text.lower():
                if msg.toType == 2:
                    red = re.compile(re.escape('copy '),re.IGNORECASE)
                    tname = red.sub('',msg.text)
                    tname = tname.lstrip()
                    tname = tname.replace(" @","$spliter$")
                    tname = tname.rstrip()
                    tname = tname.split("$spliter$")
                    tname = tname[0]
                    tname = tname[1:]
                    clist = {
                        "Founded":False,
                        "displayName":"",
                        "statusMessage":"",
                        "pictureStatus":""
                    }
                    mems = baim.getGroup(msg.to).members
                    for targ in mems:
                        if targ.displayName == tname:
                            clist["displayName"] = targ.displayName
                            clist["statusMessage"] = targ.statusMessage
                            clist["pictureStatus"] = targ.pictureStatus
                            clist["Founded"] = True
                    if clist["Founded"]:
                        wait["selfStatus"] = False
                        me = baim.getProfile()
                        me.displayName = clist["displayName"]
                        me.statusMessage = clist["statusMessage"]
                        me.pictureStatus = clist["pictureStatus"]
                        baim.updateDisplayPicture(me.pictureStatus)
                        baim.updateProfile(me)
                        baim.sendText(msg.to,"Done")
                    else:
                        baim.sendText(msg.to,"Done")

            elif "Urlpict @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Urlpict @","")
                _nametarget = _name.rstrip(' ')
                gs = baim.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    baim.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = acil.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            baim.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Urlcover @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Urlcover @","")
                _nametarget = _name.rstrip(' ')
                gs = baim.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    baim.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = acil.getContact(target)
                            cu = baim.channel.getCover(target)
                            path = str(cu)
                            baim.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if wait["blacklist"] == {}:
                    baim.sendText(msg.to,"Tɪᴅᴀᴋ Aᴅᴀ ᴋᴏɴᴛᴀᴋ Bʟᴀᴄᴋʟɪsᴛ")
                else:
                    baim.sendText(msg.to,"≡≡≡≡≡≡≡≡≡≡Lɪsᴛ Bʟᴀᴄᴋʟɪsᴛ≡≡≡≡≡≡≡≡≡≡")
                    h = ""
                    for i in wait["blacklist"]:
                        h = baim.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        baim.sendMessage(M)

#-------------------------------------------------
	    elif "Spam @" in msg.text:
#	      if msg.from_ in admin:
                _name = msg.text.replace("Spam @","")
                _nametarget = _name.rstrip(' ')
                gs = baim.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
		               baim.sendText(msg.to,"Wating in progres...")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
		               ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
		               ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
	  	             ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
		               ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
		               ki6.sendText(g.mid,"Your Account Has Been Spammed !")
		               ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
		               ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
		               ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
		               ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
		               ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
		               ki5.sendText(g.mid,"Your Account Has Been Spammed !")
		               ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
		               ki5.sendText(g.mid,"Your Account Has Been Spammed !")
		               ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
		               ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
		               ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
		               ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki10.sendText(g.mid,"Your Account Has Been Spammed !")
                       baim.sendText(msg.to, "Succes")
                       print " Spammed !"
#--------------------------------------------------------------------------
#-----------------------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		baim.sendText(msg.to,"Target Lock")
#-----------------------------------------------------------
            elif "Leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                text = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (text+"\n")
                if txt[1] == "on":
                    if jmlh <= 10000:
                        for x in range(jmlh):
                            ki.sendText(msg.to, text)
                    else:
                        baim.sendText(msg.to, "Out Of Range!")
                elif txt[1] == "off":
                    if jmlh <= 10000:
                        ki.sendText(msg.to, tulisan)
                    else:
                        baim.sendText(msg.to, "Out Of Range!")
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        baim.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        baim.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        baim.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        baim.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            baim.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+acil.getContact(mi_d).displayName + "\n"
                            baim.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                baim.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                baim.sendText(msg.to,"Mimic change to target")
                            else:
                                baim.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        baim.sendText(msg.to,"Reply Message on")
                    else:
                        baim.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        baim.sendText(msg.to,"Reply Message off")
                    else:
                        baim.sendText(msg.to,"Sudah off")
            elif "Grupname" in msg.text:
                saya = msg.text.replace('Grupname','')
                gid = baim.getGroup(msg.to)
                baim.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "Gid" in msg.text:
                saya = msg.text.replace('Gid','')
                gid = baim.getGroup(msg.to)
                baim.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
            elif msg.text in ["Friendlist"]:    
                contactlist = baim.getAllContactIds()
                kontak = baim.getContacts(contactlist)
                num=1
                msgs="≡≡≡≡≡≡≡≡≡≡Lιѕт Fяιεиd≡≡≡≡≡≡≡≡≡≡"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n≡≡≡≡≡≡≡≡≡≡Lιѕт Fяιεиd≡≡≡≡≡≡≡≡≡≡\n\nTotal Friend : %i" % len(kontak)
                baim.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:   
                kontak = baim.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="≡≡≡≡≡≡≡≡≡≡ĿĪSŦ MƐMßƐŔ≡≡≡≡≡≡≡≡≡≡"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n≡≡≡≡≡≡≡≡≡≡ĿĪSŦ MƐMßƐŔ≡≡≡≡≡≡≡≡≡≡\n\nTotal Members : %i" % len(group)
                baim.sendText(msg.to, msgs)
               
                
            elif msg.text in ["Friendlistmid"]: 
                gruplist = baim.getAllContactIds()
                kontak = baim.getContacts(gruplist)
                num=1
                msgs="≡≡≡≡≡≡≡≡≡≡Lιѕт FяιεиdMιd≡≡≡≡≡≡≡≡≡≡"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n≡≡≡≡≡≡≡≡≡≡Lιѕт FяιεиdMιd≡≡≡≡≡≡≡≡≡≡\n\nTotal Friend : %i" % len(kontak)
                baim.sendText(msg.to, msgs)
                    
#-----------------------------------------------
            elif "Lurk on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         baim.sendText(msg.to,"ɭϋʀϰɪήɡ ɑɭʀəɑɗϔ ʘή")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     baim.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "Lurk off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    baim.sendText(msg.to,"ɭϋʀϰɪήɡ ɑɭʀəɑɗϔ ʘʃʃ")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    baim.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "Lurkers" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             baim.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = baim.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          baim.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
                    else:
                        baim.sendText(msg.to, "Lυɾƙɪɲʛ ɦʌƨ ɲơƭ ƅєєɲ ƨєƭ")           

            elif msg.text in ["Bl on"]:
                wait["wblacklist"] = True
                baim.sendText(msg.to,"Sєη∂ Ƈσηтαcт")
            elif msg.text in ["Unbl:on"]:
                wait["dblacklist"] = True
                baim.sendText(msg.to,"Sєη∂ Ƈσηтαcт")
            elif msg.text.lower() == 'Mcheck':
                if wait["blacklist"] == {}:
                    baim.sendText(msg.to,"₣㊉LL㊉WING IS A BLACҞLISŦ")
                else:
                    baim.sendText(msg.to,"₣㊉LL㊉WING IS A BLACҞLISŦ")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "�" +baim.getContact(mi_d).displayName + "\n"
                    baim.sendText(msg.to,mc)
 #---------Fungsi Banlist With Tag--------#
            elif msg.text in ["Banlist","ip banlist"]:
                if wait["blacklist"] == {}:
                    baim.sendText(msg.to,"N㊉ USER IS BLACҞLISŦEÐ")
                else:
                    ki.sendText(msg.to,"Blacklisted user")
                    mc = " 🛡️≡≡≡≡≡||B L A C Ҟ L I S Ŧ||≡≡≡≡≡🛡️\n"
                    for mi_d in wait["blacklist"]:
                        mc += "🗜️" +baim.getContact(mi_d).displayName + "\n"
                    baim.sendText(msg.to,mc)
                    
                    print "[Command]Banlist executed"
            elif msg.text in ["Clearban"]:
                if msg.toType == 2:
                   wait["blacklist"] = {}
                   baim.sendText(msg.to,"clear all blacklist")
                   ki.sendText(msg.to,"Ð㊉NE ✔")
                   ki2.sendText(msg.to,"Ð㊉NE ✔")
                   ki3.sendText(msg.to,"Ð㊉NE ✔")
                   ki4.sendText(msg.to,"Ð㊉NE ✔")
                   ki5.sendText(msg.to,"Ð㊉NE ✔")
                   ki6.sendText(msg.to,"Ð㊉NE ✔")
                   ki7.sendText(msg.to,"Ð㊉NE ✔")
                   ki8.sendText(msg.to,"Ð㊉NE ✔")
                   ki9.sendText(msg.to,"Ð㊉NE ✔")
                   ki10.sendText(msg.to,"Ð㊉NE ✔")
                   ki.sendText(msg.to,"вℓα¢кℓιѕт ∂σηє αℓℓ яємσνє∂ кσмαη∂αη👮")
            elif msg.text.lower() == 'Kick@mbl':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            baim.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            ki6.kickoutFromGroup(msg.to,[jj])
                            ki7.kickoutFromGroup(msg.to,[jj])
                            ki8.kickoutFromGroup(msg.to,[jj])
                            ki9.kickoutFromGroup(msg.to,[jj])
                            ki10.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
#-----------------------------------------------

#---------------------------------------------------
            elif "Pict @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Pict @","")
                _nametarget = _name.rstrip(' ')
                gs = baim.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    baim.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = baim.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            baim.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#---------------------------------------------------
#---------------------------------------------------
            elif msg.text in ["Recopy"]:
                try:
                    baim.updateDisplayPicture(mybackup.pictureStatus)
                    baim.updateProfile(mybackup)
                    baim.sendText(msg.to, "Success")
                except Exception as e:
                    baim.sendText(msg.to, str (e))
#-----------------------------------------------------------------------
            elif "Youtube " in msg.text:
                try:
                    textToSearch = (msg.text).replace("Youtube ", "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    baim.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    baim.sendText(msg.to,"Could not find it")
            elif "Youtubesearch " in msg.text:
                    query = msg.text.replace("Youtubesearch ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        baim.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
                        
#------------------------------------------------
            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = baim.getContact(key1)
                cu = baim.channel.getCover(key1)
                try:
                    baim.sendText(msg.to,"~Nama\n" + contact.displayName + "\n~Mid\n" + contact.mid + "\n~Bio\n" + contact.statusMessage + "\n~Profile Picture\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n~Header\n" + str(cu))
                except:
                    baim.sendText(msg.to,"~Nama\n" + contact.displayName + "\n~Mid\n" + contact.mid + "\n~Bio\n" + contact.statusMessage + "\n~Profile Picture\n" + str(cu))
            
            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = baim.getContact(key1)
                cu = baim.channel.getCover(key1)
                try:
                    baim.sendText(msg.to,contact.statusMessage)
                except:
                    baim.sendText(msg.to,contact.statusMessage)
            elif "Gimage" in msg.text:
					group = acil.getGroup(msg.to)
					path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
					baim.sendImageWithURL(msg.to,path)
            
            elif "Getprofile @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Getprofile @","")
                _nametarget = _name.rstrip('  ')
                gs = baim.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    baim.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = baim.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            baim.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#------------------------------------------------------------
            elif msg.text in ["Invite"]:
                wait["invite"] = True
                random.choice(KAC).sendText(msg.to,"ՏᎬΝᎠ ᏟϴΝͲᎪᏟͲ")
#------------------------------------------------------------
            elif "Getcover @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Getcover @","")    
                _nametarget = _name.rstrip('  ')
                gs = baim.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    baim.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = baim.getContact(target)
                            cu = baim.channel.getCover(target)          
                            path = str(cu)
                            baim.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif msg.text.lower() == 'Reboot':
                    print "[Command]Like executed"
                    try:
                        baim.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        baim.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif "Hay " in msg.text:
                say = msg.text.replace("Hay ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                baim.sendAudio(msg.to,"hasil.mp3")
            elif "Nuke" in msg.text:
                if msg.toType == 2:
                    print "Nuke ok"
                    _name = msg.text.replace("Nuke","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    gs = ki8.getGroup(msg.to)
                    gs = ki9.getGroup(msg.to)
                    gs = ki10.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        baim.sendText(msg.to,"Limit gw njir..")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                pass
            elif msg.text in ["Tag","Tagall","Mencret"]:
                group = baim.getGroup(msg.to)
                k = len(group.members)//500
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*500 : (j+1)*500]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    baim.sendMessage(msg) 
            elif msg.text.lower() == '.':
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        baim.updateGroup(G)
                        invsend = 0
                        Ticket = baim.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)

#-----------------------------------------------
            elif msg.text.lower() == 'Reinvite':
                if msg.toType == 2:
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        baim.sendText(msg.to,"waitting...")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        G.preventJoinByTicket = False
                        baim.updateGroup(G)
                        invsend = 0
                        Ticket = baim.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Sk1 in" in msg.text:
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        baim.updateGroup(G)
                        invsend = 0
                        Ticket = baim.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Sk2 in" in msg.text:
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        baim.updateGroup(G)
                        invsend = 0
                        Ticket = baim.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "Sk3 in" in msg.text:
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        baim.updateGroup(G)
                        invsend = 0
                        Ticket = baim.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "Sk4 in" in msg.text:
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        baim.updateGroup(G)
                        invsend = 0
                        Ticket = baim.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif "Sk5 in" in msg.text:
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        baim.updateGroup(G)
                        invsend = 0
                        Ticket = baim.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#-----------------------------------------------
            elif "Sk6 in" in msg.text:
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        baim.updateGroup(G)
                        invsend = 0
                        Ticket = baim.reissueGroupTicket(msg.to)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
#-----------------------------------------------
            elif "Sk7 in" in msg.text:
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        baim.updateGroup(G)
                        invsend = 0
                        Ticket = baim.reissueGroupTicket(msg.to)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki7.updateGroup(G)
#-----------------------------------------------
            elif "Sk8 in" in msg.text:
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        baim.updateGroup(G)
                        invsend = 0
                        Ticket = baim.reissueGroupTicket(msg.to)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki8.updateGroup(G)
#-----------------------------------------------
            elif "Sk9 in" in msg.text:
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        baim.updateGroup(G)
                        invsend = 0
                        Ticket = baim.reissueGroupTicket(msg.to)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki9.updateGroup(G)
#-----------------------------------------------
            elif "Sk10 in" in msg.text:
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        baim.updateGroup(G)
                        invsend = 0
                        Ticket = baim.reissueGroupTicket(msg.to)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = baim.getGroup(msg.to)
                        ginfo = baim.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki10.updateGroup(G)
#------------------------------------------------------------------

            elif msg.text.lower() == ',':
                if msg.toType == 2:
                    ginfo = baim.getGroup(msg.to)
                    try:
#                        baim.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Sk bye" in msg.text:
                if msg.toType == 2:
                    ginfo = baim.getGroup(msg.to)
                    try:
                    	ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        baim.eaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Sk1 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = baim.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Sk2 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = baim.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Sk3 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = baim.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Sk4 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = baim.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Sk5 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = baim.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Sk6 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = baim.getGroup(msg.to)
                    try:
                        ki6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Sk7 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = baim.getGroup(msg.to)
                    try:
                        ki7.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Sk8 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = baim.getGroup(msg.to)
                    try:
                        ki8.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Sk9 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = baim.getGroup(msg.to)
                    try:
                        ki9.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Sk10 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = baim.getGroup(msg.to)
                    try:
                        ki10.leaveGroup(msg.to)
                    except:
                        pass

            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = baim.getGroup(msg.to)
                ki9.sendText(msg.to,"​    ω⃢​    є⃢​    ℓ⃢​    ¢⃢​    σ⃢​    м⃢​    є⃢​     ​    т⃢​    σ⃢​     ​    т⃢​    н⃢​    є⃢​     ​    g⃢​    я⃢​    σ⃢​    υ⃢​    ρ⃢     ​ " + str(ginfo.name))
                ki10.sendText(msg.to,"σωηєя gяσυρ " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
            elif "Bc " in msg.text:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
            elif "Say " in msg.text:
				bctxt = msg.text.replace("Say ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
            elif "Bom " in msg.text:
				bctxt = msg.text.replace("Bom ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
#                baim.sendText(msg.to, "вσм ¢нαт ѕєℓєѕαι кσмαη∂αη")
            elif msg.text.lower() == 'Ping':
                ki.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki2.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki3.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki4.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki5.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki6.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki7.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki8.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki9.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki10.sendText(msg.to,"Ping 􀜁􀇔􏿿")

#-----------------------------------------------
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        baim.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        baim.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        baim.updateGroup(G)
                        ki2.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = acil.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        baim.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = baim.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        baim.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        baim.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        baim.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                        baim.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        baim.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in ki8mid:
                    if op.param2 in ki7mid:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                    else:
                        G = ki7.getGroup(op.param1)
                        ki7.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        baim.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in kimid:
                    if op.param2 in ki7mid:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                    else:
                        G = ki8.getGroup(op.param1)
                        ki8.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        baim.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in kimid:
                    if op.param2 in ki9mid:
                        G = ki10.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                    else:
                        G = ki10.getGroup(op.param1)
                        ki10.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                        baim.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                elif op.param3 in ki10mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        baim.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        baim.updateGroup(G)
                        wait["blacklist"][op.param2] = True
            except:
                pass
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ki5.updateGroup(G)
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in Bots:
		    random.choice(KAC).sendText(op.param1,"ωєℓςσмє. ∂σи'т ρℓαу вσтѕ. ι ςαи кιςк уσυ!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["Protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    baim.sendText(op.param1,"")
	    else:
		baim.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["Invite protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    baim.sendText(op.param1,"")
	    else:
		baim.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["Invite protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    baim.cancelGroupInvitation(op.param1,[contact.mid for contact in baim.getGroup(op.param1).invitee])
		else:
		    baim.sendText(op.param1,"")
	    else:
		baim.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["Cancel protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    baim.cancelGroupInvitation(op.param1,[contact.mid for contact in baim.getGroup(op.param1).invitee])
		else:
		    baim.sendText(op.param1,"∂σ иσт ιиνιтє ωιтнσυт ℓιмιтѕ α∂мιи.!")
	    else:
		baim.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["Link protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    baim.sendText(op.param1,"")
	    else:
		baim.sendText(op.param1,"")
        if op.type == 5:
            if wait["Auto add"] == True:
            	c = Message(to=op.param1, from_=None, text=None, contentType=13)
                c.contentMetadata={'mid':'u03625388921e6baa1e0fc85003b8fdef'}
                baim.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/0hPV_dx45gD3liHSNSj09wLl5YARQVMwkxGntGT0YUVhsdeh8oXnIUGUMYVUBGfUgvX3JCHUMUVk8Y")
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    baim.sendText(op.param1,str(wait["message"]))
                    baim.sendMessage(c)
                    ki.sendText(op.param1,str(wait["message"]))
                    ki.sendMessage(c)
                    ki2.sendText(op.param1,str(wait["message"]))
                    ki2.sendMessage(c)
                    ki3.sendText(op.param1,str(wait["message"]))
                    ki3.sendMessage(c)
                    ki4.sendText(op.param1,str(wait["message"]))
                    ki4.sendMessage(c)
                    ki5.sendText(op.param1,str(wait["message"]))
                    ki5.sendMessage(c)
                    ki6.sendText(op.param1,str(wait["message"]))
                    ki6.sendMessage(c)
                    ki7.sendText(op.param1,str(wait["message"]))
                    ki7.sendMessage(c)
                    ki8.sendText(op.param1,str(wait["message"]))
                    ki8.sendMessage(c)
                    ki9.sendText(op.param1,str(wait["message"]))
                    ki9.sendMessage(c)
                    ki10.sendText(op.param1,str(wait["message"]))
                    ki10.sendMessage(c)
                    
#------Open QR Kick start------#
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(KAC).updateGroup(G)
        #------Open Kick finish-----#
#------invite Kick start------#
        if op.type == 13:
            if wait["inviteprotect"] == True:
                if op.param2 not in Bots:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(KAC).updateGroup(G)
        #------invite Kick finish-----#
        if op.type == 55:
            try:
                if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = baim.getContact(op.param2).displayName
                            Np = baim.getContact(op.param2).pictureStatus
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n� " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        baim.sendText(op.param1,"≡≡≡≡≡≡≡≡≡SIÐER≡≡≡≡≡≡≡≡≡\n" + nick[0] + "\n" +  wait["sider1"])
                                        baim.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                    else:
                                        baim.sendText(op.param1,"≡≡≡≡≡≡≡≡≡SIÐER≡≡≡≡≡≡≡≡≡\n" + nick[0] + "\n" +  wait["sider1"])
                                        baim.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                else:
                                    baim.sendText(op.param1,"≡≡≡≡≡≡≡≡≡SIÐER≡≡≡\n" + nick[0] + "\n" +  wait["sider1"])
                                    baim.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                        else:
                            pass
                else:
                    pass
            except:
                pass
        else:
            pass
        
        if op.type == 55:
            if op.param1 in wait2['readPoint']:
                Name = baim.getContact(op.param2).displayName
                if Name in wait2['readMember'][op.param1]:
                    pass
                else:
                    wait2['readMember'][op.param1] += "\n・" + Name
                    wait2['ROM'][op.param1][op.param2] = "・" + Name
            else:
                baim.sendText
        if op.type == 17:
          if wait["Wc on"] == True:
            	ginfo = baim.getGroup(op.param1)
            	contact = baim.getContact(op.param2)
            	c = Message(to=op.param1, from_=None, text=None, contentType=13)
            	c.contentMetadata={'mid':op.param2}
            	baim.sendText(op.param1,wait["joingc"] + "\n" + baim.getContact(op.param2).displayName + "\n∂ι gяυρ " + str(ginfo.name) + "\nρємϐυατ gяυρ" + ginfo.creator.displayName + "\n\n≡≡≡≡≡≡ѕιиgℓє κιℓℓєя τєαм ϐοτ≡≡≡≡≡≡")
            	baim.sendMessage(c)
            	baim.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" + contact.pictureStatus)
            	print ("MEMBER JOIN TO GROUP")
        if op.type == 15:
          if wait["Left on"] == True:
            	c = Message(to=op.param1, from_=None, text=None, contentType=13)
            	c.contentMetadata={'mid':op.param2}
            	baim.sendMessage(c)
            	baim.sendText(op.param1,baim.getContact(op.param2).displayName + "\n" + wait["leftgc"])
            	print ("MEMBER HAS LEFT THE GROUP")
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
        if op.type == 59:
            print op
    except Exception as error:
        print error
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = baim.getProfile()
                profile.displayName = wait["cName"] + nowT
                baim.updateProfile(profile)
            time.sleep(0.30)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
while True:
    try:
        Ops = baim.fetchOps(acil.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(baim.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            baim.Poll.rev = max(baim.Poll.rev, Op.revision)
            bot(Op)

