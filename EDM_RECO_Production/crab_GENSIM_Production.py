import CRABClient
from CRABClient.UserUtilities import config 

config = config()

config.General.requestName = 'HardQCD_02Feb_2022_GEN_SIM'
config.General.workArea = 'crab_projects_02Feb_2022_GEN_SIM'
config.General.transferOutputs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'QCD_Pt_600_800_14TeV_TuneCUETP8M1_cfi_py_GEN_SIM.py'

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob  = 250
NJobs = 3500
config.Data.totalUnits = config.Data.unitsPerJob * NJobs
config.Data.publication = True
config.Data.outputDatasetTag = 'generation_simulation-stage'#
config.Data.outputPrimaryDataset = 'Spring_HardQCD_50_800_PAT_14TeV_TuneCUETP8M1_GEN_SIM'#

config.Site.storageSite = 'T2_TW_NCHC'

