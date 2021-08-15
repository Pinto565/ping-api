import subprocess
import os
from datetime import datetime
import pytz
import socket

def time():
    IST = pytz.timezone('Asia/Kolkata')
    update_time = (datetime.now(IST).strftime('%Y:%m:%d %H:%M:%S %Z %z')).replace(" +0530","")
    return update_time


hosts =  os.environ["HOSTS"]  #"vpn.opencloud.pattarai.in"

status = {
    "updated time" : time() , 
    "device status" : []
}

def pinghost(host):
    cmd = f"ping {host} -c 1"
    result = subprocess.run(cmd,shell=True,capture_output=True,text=True)
    result_text =  (result.stdout)

    if "Request timed out" in result_text:
        return "offline"
    elif "Destination Host Unreachable" in result_text:
        return "offline"
    else:
        return "online"

def update_status():
    status["device status"] = []
    status["updated time"] = time()
    for host in hosts.split(" "):
        try:
            ip_addr = socket.gethostbyname(host)
            devicestatus = {
            "host" : host ,
            "ip address" : ip_addr ,
            "status" : pinghost(host)
        }
        except:
            ip_addr = "Host Not Found"
            devicestatus = {
            "host" : host ,
            "ip address" : ip_addr ,
            "status" : "offline"
        }
        status["device status"].append(devicestatus)