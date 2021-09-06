# HOW TO INSTALL?

# API viko-api.herokuapp.com/docs
# pip install requests
# pip install pyfiglet

# BY VIKO kasih bintang kecil donk
from time import sleep
import pyfiglet
import requests
result = pyfiglet.figlet_format("CALL-OTP", font = "banner4" )
print('----------------------[ M R V I K O ]-------------------------')

print(result)

print('----------------------[ Version 1.0 ]-------------------------')
sleep(0.50)
print("CALL-OTP\n\nTutorial: masukan nomor awalan 81515 jangan 0815 atau 62815\nNote: ini cuman call otp khusus buat prank aja jangan dibuat serius\n\nFREE REST-API: viko-api.herokuapp.com/docs\nCTRL + C untuk membatalkan\n")
apikey = 'rxking'
nomore = raw_input("NO TELP >> ")

response = requests.get('https://viko-api.herokuapp.com/api/hack/tlpn?query='+ nomore +'&apikey=' + apikey)

viko = response
print(viko.json()["result"])