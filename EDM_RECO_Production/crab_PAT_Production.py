import CRABClient
from CRABClient.UserUtilities import config 

config = config()

config.General.requestName = 'HardQCD_02Feb_2022_PAT'
config.General.workArea = 'crab_projects_02Feb_2022_PAT'
config.General.transferOutputs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'pat_workflow_cfi.py'

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob  = 450
NJobs = 1800
config.Data.totalUnits = config.Data.unitsPerJob * NJobs
config.Data.publication = True
config.Data.outputDatasetTag = 'generation_simulation-stage'#
config.Data.outputPrimaryDataset = 'Spring_HardQCD_50_800_PAT_14TeV_TuneCUETP8M1'#

config.Site.storageSite = 'T2_TW_NCHC'

