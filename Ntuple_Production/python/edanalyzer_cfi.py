from HardQCD_Generation_HGCal.Ntuple_Production.template_cff import * 
import FWCore.ParameterSet.VarParsing as VarParsing

options = VarParsing.VarParsing('analysis')

options.register('nevents',
-1, # default value
VarParsing.VarParsing.multiplicity.singleton, # singleton or list
VarParsing.VarParsing.varType.int,          # string, int, or float
"Number of events to process (-1 for all)")
options.register('part',
1,
VarParsing.VarParsing.multiplicity.singleton, # singleton or list
VarParsing.VarParsing.varType.int,          # string, int, or float
"postfix of filesname")

options.parseArguments()

print(f'part: {options.part}')
with open(f'./data/000{options.part}.txt','r') as f :
    lines = f.readlines()

FileIn = [filename.split('/cms')[-1] for filename in lines]


process.source.fileNames = cms.untracked.vstring(*FileIn)
#process.source.fileNames = cms.untracked.vstring(*FileIn[0:10])
#process.source.fileNames = cms.untracked.vstring('file:/eos/user/z/zhenggan/JetTaggingwithHGCal/test/0001.root')
#process.maxevnets
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.nevents) )
process.analyzer = cms.EDAnalyzer('Ntuple_Analyzer',
        LC_src = cms.InputTag('hgcalLayerClusters'),
        Jet_src = cms.InputTag('selectedPatJets'),
        TICLCand_src = cms.InputTag('TICLTrackstersMerge'))

process.TFileService.fileName = cms.string(f"/eos/user/z/zhenggan/JetTaggingwithHGCal/HardQCD/woPileUp/April/pt50_800_part{options.part}.root")
#process.TFileService.fileName = cms.string(f"pt50_800_part{part}.root")

process.p = cms.Path(process.analyzer)

