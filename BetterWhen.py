import subprocess
import sys
from datetime import date
import time


#example: 2022-12-31 10:30 or 2022-12-31 10 or 31.12.2022 10:30
def getTimestamp(date,daytime):
    formats = ['%Y-%m-%d %H:%M','%Y-%m-%d %H','%d.%m.%YY %H:%M','%d.%m.%YY %H']
    for format in formats:
        try:
            return int(time.mktime(time.strptime(f'{date} {daytime}', format)))
        except ValueError:
            pass
    raise Error('your Momma')




if __name__ == "__main__":
    result = subprocess.run(['pluck', 'version'], stdout=subprocess.PIPE)
    print("pluckeye version: " + result.stdout.decode('utf-8'))

    if (len(sys.argv) == 1 or sys.argv[2] == "--help" ):
        print('day time day2 time2 "rule to apply" ')
    day1  = sys.argv[1]
    time1 = sys.argv[2]
    day2  = sys.argv[3]
    time2 = sys.argv[4]
    
    timestamp = getTimestamp(day1,time1);
    timestamp2 = getTimestamp(day2,time2);
    line = f'when {timestamp}-{timestamp2} allow youtube.com'
    print(line)
    s = f"pluck when {timestamp}-{timestamp2} {sys.argv[5]}"
    subprocess.run(s.split())



