# HardQCD_Generation_HGCal
Generate Hard QCD Process with CLUE and TICL Algorithm
xrdfs se01.grid.nchc.org.tw ls /cms/store/user/zhenggan/path/to/data | cat > XXXX.txt
記得調整OutputDir
```
cmsRun ./python/edanalyzer_cfi.py  part=0
```


# Segmentation violation in Ntuple part.
Be careful, the array size might be too small.
