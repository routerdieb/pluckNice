from asyncio.windows_events import NULL
import subprocess
import sys
import re

def setSettingClean(name,value):
    cleanSetting(name)
    Allowline = f'allow https://settings.arpa/?{name}={value}'
    subprocess.run(['pluck', '+',str(Allowline)])

def appendSetting(name,value):
    Allowline = f'allow https://settings.arpa/?{name}={value}'
    subprocess.run(['pluck', '+',str(Allowline)])

def getSingleSetting(name):
    PartAllowline = f'allow https://settings.arpa/?{name}'
    result = subprocess.run(['pluck', 'export'], stdout=subprocess.PIPE)
    export = result.stdout.decode('utf-8')
    for line in export.split("\r\n"):
        if PartAllowline in line:
            if(line.startswith('#')):
                print('either setting pending or a pending conflict')
                return NULL
            else:
                return line

def cleanSetting(name):
    PartAllowline = f'allow https://settings.arpa/?{name}'
    result = subprocess.run(['pluck', 'export'], stdout=subprocess.PIPE)
    export = result.stdout.decode('utf-8')
    for line in export.split("\r\n"):
        if PartAllowline in line:
            if(line.startswith('#')):
                line = re.sub(r'^.*?[+] ', '', line)
                subprocess.run(['pluck', '-',line])
            else:
                subprocess.run(['pluck', '-',line])