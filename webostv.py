#!/usr/bin/python3
from pylgtv import WebOsClient

import sys
import logging

host = '192.168.88.18'
config = '/home/homeassistant/.homeassistant/webostv.conf'
timeout = 5

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

try:
    webos_client = WebOsClient(host, config, timeout)

except:
    print("Error connecting to TV")

try:
    #device = webos_client.get_software_info()
    #print("  Device: "+device("product_name"))
    #print("   Model: "+device("model_name"))
    #print("     MAC: "+device("device_id"))
    #print(" Version: "+device("major_ver")+"."+device("minor_ver"))

    for app in webos_client.get_apps():
        print(app)
        print("       ID: "+app["id"])
        print("    Title: "+app["title"])
        print("    Image: "+app["largeIcon"])
        print(" UserData: "+app["userData"])
        print("\n")

    print(webos_client.get_audio_status())

    for service in webos_client.get_services():
        print(service)

    print(webos_client.get_current_app())

except:
    print("Error!")




