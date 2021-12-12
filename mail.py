#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests,json,datetime,os; os.system("clear")
"""
Build Date: Sun Dec 12 16:31:22 WIB 2021

Author: xolvadev

Join us!

t.me/paddirdp - t.me/channel_justinfo
"""

BOLD = "\033[1m"
print(BOLD)

def mail(line):
	r = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
	x = r.text.strip("[").strip("]").strip('"'
	).strip("'")
	now = datetime.datetime.now()
	print(f"""
[Email] >>> {x}

[Date] >>> {now}

[Waiting For Messages..]

Use CTRL+Z To Cancel!\n""")
	print(line)
	user = x.split("@")[0]
	dom = x.split("@")[1]
	z = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain={dom}").text
	c = 0
	while True:
		z = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain={dom}").json()
		if z != "[]":
			try:
				z = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={user}&domain={dom}&id={z[c]['id']}").json()
				print(f"""New Message!

From: {z['from']}

Subject: {z['subject']}
Date: {z['date']}
ID: {z['id']}

Body: {z['body']}

{line}""")
				c += 1
			except KeyboardInterrupt:
				break
				print("[+] Cancelled.")
			except IndexError:
				pass
		else:
			pass
banner = """
           _
          |E]
        .-|=====-.
        | | mail |
     ___|________|
       Py3  ||
            ||
            ||   By xolvadev
     ,;,    ||   )_(,;;;,
     <_>  \ ||   \|/ \_/
     \|/  \\||  \\|   |//
v1.0_\|//_\\|///_\V/_\|//__
"""

def main():
	line = "="*35
	print(banner)
	print(line)
	print("[00] Exit Program.")
	print("[01] Get Email & Receive Message")
	print("[02] Report Bugs - Error")
	print("[03] More Tools")
	print("[04] Join Channel Telegram")
	print(line)
	inp = input("xv@tempmail >>> ")
	while inp == "":
		inp = input("xv@tempmail >>> ")
	if inp in ("00","0"):
		print(line)
		print("Program Succesfully Cancelled.")
	elif inp in ("01","1"):
		print(line)
		mail(line)
	elif inp in ("02","2"):
		print(line)
		print("Redirecting To t.me/xolvadev...")
		os.system("xdg-open t.me/xolvadev")
	elif inp in ("03","3"):
		print(line)
		print("Redirecting To github.com/xolvadev...")
		os.system("xdg-open github.com/xolvadev")
	elif inp in ("04","4"):
		print(line)
		print("Redirecting To t.me/paddirdp...")
		os.system("xdg-open t.me/paddirdp")
	else:
		print(line)
		print("Invalid Options : "+inp)

if __name__=="__main__":
	main()
