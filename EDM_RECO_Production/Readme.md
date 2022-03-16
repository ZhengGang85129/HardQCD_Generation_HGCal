#General Setting For MC Production
- Era:Phase2C11I13M9
- geometry: Extended2026D77
- pileup: NoPileUp
- beamspot: HLLHC
- conditions: auto:phase2_realistic_T21
- EventGenerator: Configuration/Generator/python/QCD_Pt_600_800_14TeV_TuneCUETP8M1_cfi.py
#EventGenerator Setting
- pt: 50 < pt < 800
#WorkFlow

- crab submit -c crab_GENSIM_Production.py
- crab submit -c crab_PAT_Production.py

After this, jump to Ntuple directory.
