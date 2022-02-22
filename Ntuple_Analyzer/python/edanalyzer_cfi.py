from template_cff import * 

process.source.fileNames = cms.untracked.vstring('/eos/user/z/zhenggan/JetTaggingwithHGCal/test/0001_patTuple.root')
process.analyzer = cms.EDAnalyzer('Ntuple_Analyzer',
        LC_src = cms.InputTag('hgcalLayerClusters'),
        Jet_src = cms.InputTag('selectedPatJets'))

process.TFileService.fileName = cms.string("ntuple.root")

process.p = cms.Path(process.analyzer)

