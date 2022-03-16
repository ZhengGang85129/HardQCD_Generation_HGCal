from CRABClient.UserUtilities import config

config = config()

config.General.requestName = 'HardQCD_24Feb_2022_RECO_PAT'#
config.General.workArea = 'crab_project_24Feb_2022_RECO_PAT'#
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'pat_workflow_cfi.py'#
config.JobType.maxMemoryMB = 3500

config.Data.inputDataset ='/Spring_HardQCD_50_800_PAT_14TeV_TuneCUETP8M1_GEN_SIM/zhenggan-generation_simulation-stage-aefed920e224c5a41ef91c9cfd58dfef/USER'# 
config.Data.inputDBS = 'phys03'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob  = 1
config.Data.publication = True
config.Data.outputDatasetTag = 'reconstruction_physiscsanalysistuple-stage'#
config.Data.ignoreLocality = True

config.Site.ignoreGlobalBlacklist=True
config.Site.storageSite = 'T2_TW_NCHC'
config.Site.whitelist = ['T2_TW_NCHC']


#/outputPrimaryDataset/outputDatasetTag


