import os 

with open('./file.txt','rb') as f:
    lines = f.readlines()
    for line in lines:
        os.system(f'xrdcp root://cmsxrootd.fnal.gov/{line} /eos/user/z/zhenggan/JetTaggingwithHGCal/HardQCD/woPileUp')
