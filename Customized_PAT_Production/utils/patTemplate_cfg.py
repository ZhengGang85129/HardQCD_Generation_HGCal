import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.tools.helpers import getPatAlgosToolsTask
from Configuration.Eras.Era_Phase_Phase2C11I13M9_cff import Phase2C11M9

process = cms.Process("PAT",Phase2C11M9)

process.load('FWCore.MessengeLogger.MessageLogger_cfi')
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

process.source = cms.Source('PoolSource',fileNames = cms.untracked.vstring('/eos/user/z/zhenggan/JetTaggingwithHGCal/test/0001.root'))

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

## Geometry and Detector Conditions (needed for a few patTuple production steps)
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')
process.load("Configuration.StandardSequences.MagneticField_cff")

## Output Module Configuration (expects a path 'p')
from patEventContent_cff import customized_EventContent


process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('/eos/user/z/zhenggan/JetTaggingwithHGCal/test/patTuple.root'),
    ## save only events passing the full path
    #SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    ## save PAT output; you need a '*' to unpack the list of commands
    ## 'patEventContent'
    outputCommands = cms.untracked.vstring('drop *', *customized_EventContent )
                                                                                                                                                                                                                                 )

patAlgosToolsTask = getPatAlgosToolsTask(process)
process.outpath = cms.EndPath(process.out, patAlgosToolsTask)
