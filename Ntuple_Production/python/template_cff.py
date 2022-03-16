import FWCore.ParameterSet.Config as cms

process = cms.Process("ntuple")
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(100) 
#process.MessageLogger.cerr.threshold = 'INFO'
#process.MessageLogger.cerr.INFO = cms.untracked.PSet(limit = cms.untracked.int32(-1))
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True),SkipEvent = cms.untracked.vstring('ProductNotFound'))
process.source = cms.Source("PoolSource",
                fileNames = cms.untracked.vstring()
                            )
process.TFileService = cms.Service("TFileService", fileName = cms.string("ntuple.root"))

