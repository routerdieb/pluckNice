import subprocess
import sys


def clean_site(name):
    result = subprocess.run(['pluck', 'export'], stdout=subprocess.PIPE)
    export = result.stdout.decode('utf-8')
    for line in export.split("\r\n"):
        if (line.startswith('#') or line.startswith('flee') or line.startswith('block')):
            continue
        if(name in line):
            print(line)
            subprocess.run(['pluck', '-',line])

if __name__ == "__main__":
    result = subprocess.run(['pluck', 'version'], stdout=subprocess.PIPE)
    print("pluckeye version: " + result.stdout.decode('utf-8'))

    for i in range(1,len(sys.argv)):
        clean_site(sys.argv[i])

    print("the lines above have been removed")
