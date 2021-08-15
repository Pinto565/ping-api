import subprocess
import os
from datetime import datetime
import pytz
import socket

def time():
    IST = pytz.timezone('Asia/Kolkata')
    update_time = (datetime.now(IST).strftime('%Y:%m:%d %H:%M:%S %Z %z'))
    return update_time


hosts = os.environ["HOSTS"]

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
        devicestatus = {
            "host" : host,
            "ip address" : socket.gethostbyname(host),
            "status" : pinghost(host)
        }
        status["device status"].append(devicestatus)