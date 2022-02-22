import sys
import os 
CURRENT_WORKDIR = os.getcwd()
sys.path.append(CURRENT_WORKDIR)

import FWCore.ParameterSet.Config as cms
from QCD_Pt_600_800_14TeV_TuneCUETP8M1_cfi_py_GEN_SIM_DIGI_L1TrackTrigger_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO import *

#process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("PhysicsTools.PatAlgos.producersLayer1.jetProducer_cff")
process.load("PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi")
from Configuration.AlCa.GlobalTag import GlobalTag

process.options.wantSummary = cms.untracked.bool(True)
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T21')

patAlgosToolsTask.add(process.makePatJetsTask)
process.patJets.embedPFCandidates = cms.bool(True)



process.selectedPatJets.cut ='abs(eta) < 2.8 & abs(eta) > 1.7 &((abs(partonFlavour) > 0 && abs(partonFlavour) <= 3) || partonFlavour == 21)'
patAlgosToolsTask.add(process.selectedPatJets)



#process.source.fileNames = cms.untracked.vstring('file:/eos/user/z/zhenggan/JetTaggingwithHGCal/test/0001.root')

#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))

from utils.patEventContent_cff import customized_EventContent

process.out.fileName = cms.untracked.string('/eos/user/z/zhenggan/JetTaggingwithHGCal/test/0001_patTuple.root')
process.out.outputCommands = cms.untracked.vstring('drop *', *customized_EventContent)
