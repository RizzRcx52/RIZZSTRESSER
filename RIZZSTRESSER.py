# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
from colorama import Fore, Back
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

B = '\033[35m' #MERAH
P = '\033[1;37m' #PUTIH

os.system("clear")


print ("\033[96m                ... ... ......................   ...........")
print ("              .xO...............';oooxddodxkkkdx0NWNNNKKNWXNXN0doKNNNNNNNNNNN")
print ("              .d0..............,llocxxdookkkkxlkOKXXXXK0XXXXXNXKXNNNNNNNNNNNN")
print ("              .l0'.............coolcxxxlkkkxkodOkXXXXXOkXXXXXXNKXNNNNNNNNNNNN")
print ("              .c0;.............'llolxxxdkxoxkkdkk0XXX0KkXKXXXXXXKNNNNNNNNNNNN")
print ("              .;0:.............;oo:lxxxxxkxOOOxxxO0KOOX0K0KXKXXOlo:cldxk0KXNN")
print ("              .,Ol.............lodolxxl,,':,lxxxdkxkdOK0O0OXKXKk'o''''''',,,;")
print ("              .,ko............,llddckxdxddolOOOkxxkx,,,;ldxXKXOd.;.........'.")
print ("              .'xx............:;ldllxkokOOOO000KKK00xxokkcxKXKo:.............")
print ("              ..dO...........,';ddlldkox0000000KXNK0OOOOOl00XO;;,:...........")
print ("              ..o0'..........,.cxoccdxdd0KKKKKKKKKKK00KKdo0XKK'';'...........")
print ("              ..l0,.........'''odcc:ddxclOKKKK0K0KKKKX0dod0XOX;..............")
print ("              ..c0;''''''''',':dcc:;oddl:odk0KKKKK0kxdoldOK0xK,..........''''")
print ("              ;.:Oc'''''''',,,ll;::c:xloldooodkkxdl;colldkXxo0l'''''''''',,;;")
print ("              WXkOx:,,,,,,:dxxxolcdo,lxooxxxddxkkxkx;dxdxKKNNNKo,''''',,,;:lx")
print ("              OkdkOdc,,,'okkkkkkoll;cdoxxxxkkkkkkOOOx;kkKXNNNNNN0,''''''',;ok")
print ("              ;;;dd::;;;lkkOOOOOOkx'xkkdxkxxOOOxkO0KXXxKXNWWNNNNN0;;;;;;;;;:c")
print ("              cccoxccccckkOOkkkOOOocOOOOOkOOOOk0XWWWNNXdNWWWNNWWWNd:::ccccc::")
print ("              dddoxxdddxOOOOxxkkOO;kOOOOOOO00KNWWNNNNWWK0WWNNXWWWWKoooooooool")
print ("              OOOoxOOOkkOOOOOdxkkx:OOOO00KKXNWWNNNNNNWWWkXWNXXWWWWXkkkkkkkkkk")
print ("              KKXdxKKXKOkOOOOxldc,:O00XNNWNNNWNXXXNNNXNNOo0XKWWWWWXOOOOO00000")
print ("              XXXdxXXK0dkOOOOo....','';lkOKKXKKKXOOxc;::;,;:lNWWWWXKK0KKXXKXX")
print ("              NNNxdXNXkOkkOOk'..'.','.;;;,,;;;;,,;,;;,,:;;,::kWWWWXXXXXNNXXXX")
print ("              NNNkoXNkKddkkk:...'',;;;;::;,,,'',:;;:::;:::ccccOWWWKXXNNNNNNNN")
print ("              NNNOoKOKkddkkk....',,;;;;:::;',,;;;,;:::::::cccclNWNKXXXXXXXXNN")
print ("              NNN0lk0Odolkkd.....,,,;;;;:::;,;';;;;;::::::::cccKWNXKNNNNNNNNN")
print ("              XXX0cdOxo::kkx......,,,;;;;;;;,,.,,;;;;;:::::::::XWXXXXNNNXNNNN")
print ("              XXXKcddoc:cxkk;.......',,,,,,,,'.',,,,;;;;;;;;,,dNWKXNXXNNNXNNN")
print ("              0NNK:ooldclxkkd'.........'.'''....'''''',''''..lXXN0KXXKXXXXXXX")
print ("              XXXXcolkoloxkxdc;.............. ..............oKXXNKOXXXXXXXXXX")
print ("              XXXOolk0lloxkkkkxc. .. ... ....    .... .. .,x0XXNNW0XKKKXXXXXX")
print ("              KK0olkKxlllxkkkOOkc                      ...;xKNNWWWNKOXXXXNXXX")
print ("\033[95m                                   ~~Welcome Rizz37~~")
print ("\033[93m                      ╚╦════════════════════════════════════════════╦╝")
print ("                 ╔═════╩════════════════════════════════════════════╩═════╗")
gso = input("                     Target : ")
gso = input("                     Method : ")
gso = input("                     Time : ")
gso = input("                     Port : ")
gso = input("                     VIP : ")
print ("\033[91m                                     [ Attack Send!! ]")
print ("\033[93m                 ╚════════════════════════════════════════════════════════╝")
print ("\033[92m                After the attack is sent, type 'STOP' so the attack can stop")
time.sleep(80)
print ("\033[92m 'the attack stops")
