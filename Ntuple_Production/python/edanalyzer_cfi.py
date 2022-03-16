from HardQCD_Generation_HGCal.Ntuple_Production.template_cff import * 
import FWCore.ParameterSet.VarParsing as opts

part = 6
with open(f'./data/000{part}.txt','r') as f :
    lines = f.readlines()

FileIn = [filename.split('/cms')[-1] for filename in lines]


process.source.fileNames = cms.untracked.vstring(*FileIn)
#process.source.fileNames = cms.untracked.vstring(*FileIn[0:10])
#process.source.fileNames = cms.untracked.vstring('file:/eos/user/z/zhenggan/JetTaggingwithHGCal/test/0001.root')
process.analyzer = cms.EDAnalyzer('Ntuple_Analyzer',
        LC_src = cms.InputTag('hgcalLayerClusters'),
        Jet_src = cms.InputTag('selectedPatJets'))

process.TFileService.fileName = cms.string(f"/eos/user/z/zhenggan/JetTaggingwithHGCal/HardQCD/woPileUp/pt50_800_part{part}.root")
#process.TFileService.fileName = cms.string(f"pt50_800_part{part}.root")

process.p = cms.Path(process.analyzer)

