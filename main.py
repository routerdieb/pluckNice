import sys
from hideSettings import *
# set timeout => 10h => 1d => 1w => 1m
# prevent (all forms, that should be blocked)
if __name__ == "__main__":
    if sys.argv[1] == 'setTimeout':
        setSettingClean('timeout',sys.argv[2])
    if sys.argv[1] == 'preventUrl':
        appendSetting('preventUrl',sys.argv[2])
    if sys.argv[1] == 'preventRegex':
        pass#coming soon