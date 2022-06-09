import sys
import subprocess
from hideSettings import *
import time

def parse_function(line):
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}'
    match = re.search(regex,line)
    #calc timestamp
    print(match.group(0))
    return int(time.mktime(time.strptime(match.group(0), '%Y-%m-%d %H:%M:%S')))


def timeOutToTimeDiff(timeout):
    unit = timeout[len(timeout)-1]
    measure = int(timeout[0:len(timeout)-1])

    if unit == "h":
        hour = 60 * 60 
        diff = measure * hour 

    if unit == "d":
        day = 24 * 60 * 60 
        diff = measure * day

    if unit == "w":
        week = 7 * 24 * 60 * 60 
        diff = measure * week

    if unit == "m":
        month = 30 * 24 * 60 * 60 
        diff = measure * month

    return diff

    

preventDict = {}
# main at bottom as always
while True:
    result = subprocess.run(['pluck', 'export'], stdout=subprocess.PIPE)
    export = result.stdout.decode('utf-8')
    for line in export.split("\r\n"):
        if 'settings.arpa' in line:
            match = re.search('[?]preventUrls?=(.*)',line)
            if(match):
                g1 = match.group(1)
                preventDict[g1]=True
        elif line.startswith('#') and 'when' not in line:
            timeout = getSingleSetting('timeout')
            print(line)
            
            print(timeout)
            if timeout == NULL or timeout == '':
                exit(1)
            else:
                timestamp = parse_function(line)
                end = timestamp + timeOutToTimeDiff(timeout)
                url = re.search('[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} \+ allow (.*)',line).group(1)

                if url not in preventDict:
                    subprocess.run(['pluck','+', 'when',f'{timestamp}-{end} allow {url}'])
                else:
                    print('saved you')
                #rm old line
                print(url)
                subprocess.run(['pluck', '-','allow',url])

    print('--------------')
    time.sleep(10)



