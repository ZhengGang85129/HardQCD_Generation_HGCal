import FWCore.ParameterSet.Config as cms
customized_event_content=cms.PSet(
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_hgcalLayerClusters_*_*',
        'keep *_ak4PFJets_*_*',
        'keep *_ak4PFJetsCHS_*_*',
        'keep *_pfTICL_*_*',
        'keep *_genParticles_*_*',
        'keep *_ticlTrackstersMerge_*_*'),
    splitLevel = cms.untracked.int32(0),
)
