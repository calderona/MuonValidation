# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions auto:phase2_realistic_T15 -n 10 --era Phase2C9 --eventcontent FEVTDEBUGHLT,DQM -s RAW2DIGI,L1Reco,RECO,RECOSIM,PAT,VALIDATION:@phase2Validation --datatier GEN-SIM-RECO,DQMIO --geometry Extended2026D49 --io RecoFullGlobalPU_2026D49PU.io --python RecoFullGlobalPU_2026D49PU.py --no_exec --filein file:step2.root --fileout file:step3.root


## CODE RUNNING ON 11_2_0_pre1 and Phase II samples 
## Code for running only the validation muon code. 
## If you include the full sequence (including displaced muon related code) you need to do te full reconstruction. 


import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9



#process = cms.Process('RECO',Phase2C9)

process = cms.Process('VALIDATION',Phase2C9)  

# import of standard configurations

process.load('Configuration.StandardSequences.Services_cff')                                                                        
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')                                                                             
process.load('FWCore.MessageService.MessageLogger_cfi')                                                                             
process.load('Configuration.EventContent.EventContent_cff')                                                                         
process.load('SimGeneral.MixingModule.mixNoPU_cfi')                                                                                 
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')                                                              
process.load('Configuration.StandardSequences.MagneticField_cff')                                                                   
process.load('Configuration.StandardSequences.Validation_cff')                                                                      
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')                                                     

from Validation.RecoMuon.muonValidation_cff import *

from Validation.RecoMuon.track_selectors_cff import *


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(300),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
            fileNames = cms.untracked.vstring('root://cmsxrootd.fnal.gov//store/relval/CMSSW_11_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200_rsb-v1/10000/23D6DCDB-1E8A-3540-B8B0-AA53945B56E1.root')
)



# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:/eos/cms/store/group/phys_muon/calderon/Phase2/gemcheck_2.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)


# Additional output definition

# Other statements
process.mix.playback = True
process.mix.digitizers = cms.PSet()
for a in process.aliases: delattr(process, a)
process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')



# Modules always needed 
process.prevalidation_step = cms.Path(process.baseCommonPreValidation)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)


## Full validation sequence 
#process.MuonVal = cms.EndPath(process.recoMuonValidation)

## Only gem Muon sequence
process.gemMuonValidation = cms.EndPath(extractGemMuonsTracks_seq + tpToGEMMuonMuonAssociation + gemMuonTrackVMuonAssoc)

## Only muonReco Track sequence. 
process.val_recoMuon = cms.EndPath(process.recoMuonTracks_seq)
process.val_tpProducer = cms.EndPath(process.tpTorecoMuonMuonAssociation)
process.muonVal = cms.EndPath(process.recomuMuonTrackVMuonAssoc)    




#process.MessageLogger = cms.Service(
#    "MessageLogger",
#    destinations = cms.untracked.vstring(
#        'detailedInfo'
#         ),
#    detailedInfo = cms.untracked.PSet(
#       threshold = cms.untracked.string('DEBUG')
 #        ),
#   debugModules = cms.untracked.vstring(
#        'recomuMuonTrackVMuonAssoc'
#        )
#    )


# Schedule definition


process.schedule = cms.Schedule(process.prevalidation_step, process.gemMuonValidation, process.val_recoMuon, process.val_tpProducer,process.muonVal,process.DQMoutput_step)       

from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from SimGeneral.MixingModule.fullMixCustomize_cff
from SimGeneral.MixingModule.fullMixCustomize_cff import setCrossingFrameOn 

#call to customisation function setCrossingFrameOn imported from SimGeneral.MixingModule.fullMixCustomize_cff
process = setCrossingFrameOn(process)

# End of customisation functions

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
#from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC 

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
#process = miniAOD_customizeAllMC(process)

# End of customisation functions

# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
