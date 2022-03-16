from os import listdir

from os.path import isfile, join

with open('./data/Spring_HardQCD_50_800_PAT_14TeV_TuneCUETP8M1_RECO_DIR.txt','r') as f :
    for dirname in f:
        onlyfiles = [f for f in listdir(dirname) if isfile(f)]
        print(onlyfiles)
