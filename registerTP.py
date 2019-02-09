import time
import requests


myCredentials = "YWRtaW46" #default username/password (base64 encoded) [admin:]

myEndpoints = [
        {"addr": "10.20.30.40", "code": "1111-2222-3333-4444"},
	{"addr": "10.20.30.45", "code": "5555-6666-7777-8888"}
        ]

def buttonPress(myIpAddr,button,delay):
        xmlMsg = "<Command><UserInterface><OSD><Key><Click><Key>"+button+"</Key></Click></Key></OSD></UserInterface></Command>"

        myRequest = requests.post("http://"+myIpAddr+"/putxml", headers={'Authorization': 'Basic '+myCredentials}, data=xmlMsg)
        if myRequest.status_code == 200:
                print("Button: "+button)
        else:
                print("Error: "+myIpAddr+" with button "+button+" - "+myRequest.reason)

        time.sleep(delay)



for endpoint in myEndpoints:
        device = endpoint['addr']
        myCode = endpoint['code']

        buttonPress(myIpAddr=device, button="ok", delay=4)      #Welcome page
        buttonPress(myIpAddr=device, button="ok", delay=4)      #Network page
        buttonPress(myIpAddr=device, button="ok", delay=10)     #Cloud vs CUCM register

        for number in myCode:
                if number != "-":
                        #Process each number in the activation code
                        buttonPress(myIpAddr=device, button=number, delay=2)

        buttonPress(myIpAddr=device, button="ok", delay=30)     #Submit activation code (then registers)


	input("\nFrom Webex Control Hub, lookup your device and Launch Advanced Settings. From the menu select Security, Users and select admin and reactivate user.\nPress any key when complete ")
	buttonPress(myIpAddr=device, button="ok", delay=4)      #Set Timezone page
	buttonPress(myIpAddr=device, button="ok", delay=4)      #Final successfully registered device
