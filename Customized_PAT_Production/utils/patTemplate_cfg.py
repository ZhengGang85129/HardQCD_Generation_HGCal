import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.tools.helpers import getPatAlgosToolsTask
from Configuration.Eras.Era_Phase2C11I13M9_cff import Phase2C11I13M9

process = cms.Process("PAT",Phase2C11I13M9)

process.source = cms.Source('PoolSource',fileNames = cms.untracked.vstring(''))

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True),SkipEvent = cms.untracked.vstring('ProductNotFound'))
## Geometry and Detector Conditions (needed for a few patTuple production steps)
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")

## Output Module Configuration (expects a path 'p')


process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string(''),
    ## save only events passing the full path
    #SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    ## save PAT output; you need a '*' to unpack the list of commands
    ## 'patEventContent'
    )

patAlgosToolsTask = getPatAlgosToolsTask(process)
process.outpath = cms.EndPath(process.out, patAlgosToolsTask)
