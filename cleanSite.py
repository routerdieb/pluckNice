import subprocess
import sys

#return true if something was returned
def clean_site(name):
    result = subprocess.run(['pluck', 'export'], stdout=subprocess.PIPE)
    export = result.stdout.decode('utf-8')
    is_removed = False
    for line in export.split("\r\n"):
        if (line.startswith('#') or line.startswith('flee') or line.startswith('block')):
            continue
        if(name in line):
            print(line)
            x = input("Delete? y/n:")
            if (x.startswith("y")):
                subprocess.run(['pluck', '-',line])
                is_removed = True
    return is_removed

if __name__ == "__main__":
    result = subprocess.run(['pluck', 'version'], stdout=subprocess.PIPE)
    print("pluckeye version: " + result.stdout.decode('utf-8'))

    has_removed_smth = False
    for i in range(1,len(sys.argv)):
        if clean_site(sys.argv[i]):
            has_removed_smth = True

    if has_removed_smth:
        print("above decision were applied")
    else:
        print("no change applied")
