// -*- C++ -*-
//
// Package:    HardQCD_Generation_HGCal/Ntuple_Analyzer
// Class:      Ntuple_Analyzer
//
/**\class Ntuple_Analyzer Ntuple_Analyzer.cc HardQCD_Generation_HGCal/Ntuple_Analyzer/plugins/Ntuple_Analyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Zheng-Gang Chen
//         Created:  Tue, 22 Feb 2022 05:38:12 GMT
//
//

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include <iostream>
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/CaloRecHit/interface/CaloClusterFwd.h"
#include "RecoLocalCalo/HGCalRecAlgos/interface/ClusterTools.h"
#include <TTree.h>
#include <TMath.h>
#include "DataFormats/HGCalReco/interface/TICLCandidate.h"
//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<>
// This will improve performance in multithreaded jobs.

const int ksize = 150;
const int ksize2 = 15000;
int cnt = 0 ;



class Ntuple_Analyzer : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit Ntuple_Analyzer(const edm::ParameterSet&);
  ~Ntuple_Analyzer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginJob() override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override;

  TTree *tree = new TTree("Events","Events");
  double jet_pt;
  double jet_eta;
  float jet_charge;
  double jet_phi;
  double jet_px;
  double jet_py;
  double jet_pz;
  double jet_energy;
  int jet_neutralMultiplicity;
  int jet_chargedMultiplicity;
  int jet_partonFlavour;
  int jet_hadronFlavour;
  //int jet_key[ksize];

  int constituent_number;
  double constituent_pt[ksize];
  double constituent_eta[ksize];
  double constituent_phi[ksize];
  double constituent_px[ksize];
  double constituent_py[ksize];
  double constituent_pz[ksize];
  double constituent_energy[ksize];
  int constituent_charge[ksize]; 
   
  int cluster_number;
  int cluster_Layer[ksize2];
  double cluster_energy[ksize2];
  double cluster_eta[ksize2];
  double cluster_phi[ksize2];
  double cluster_z[ksize2];
  size_t cluster_size[ksize2];
  
  hgcal::ClusterTools *tool = new hgcal::ClusterTools();
  edm::EDGetTokenT<edm::View<pat::Jet>> jet_token;
  edm::EDGetTokenT<edm::View<reco::CaloCluster>> cluster_token;
  const edm::EDGetTokenT<edm::View<TICLCandidate>> ticl_candidates_;
  // ----------member data ---------------------------
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
  edm::ESGetToken<SetupData, SetupRecord> setupToken_;
#endif
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
Ntuple_Analyzer::Ntuple_Analyzer(const edm::ParameterSet& iConfig)
    : jet_token(consumes<edm::View<pat::Jet>>(iConfig.getParameter<edm::InputTag>("Jet_src"))),
    cluster_token(consumes<edm::View<reco::CaloCluster>>(iConfig.getParameter<edm::InputTag>("LC_src")))
{
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
  setupDataToken_ = esConsumes<SetupData, SetupRecord>();
#endif
  //now do what ever initialization is needed
}

Ntuple_Analyzer::~Ntuple_Analyzer() {
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
  //
  // please remove this method altogether if it would be left empty
}

//
// member functions
//

// ------------ method called for each event  ------------
void Ntuple_Analyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
    
    edm::Handle<edm::View<pat::Jet>> jets;
    iEvent.getByToken(jet_token,jets);
    //Finding Leading Jet
    int Leading_Jet = -200;
    double max_pt = -100;
    int jet_index = 0 ;
    for(edm::View<pat::Jet>::const_iterator Jet = jets->begin();Jet != jets->end();++Jet)
    {
        const pat::Jet * jet = &(jets->at(jet_index));
        int partonFlavour = TMath::Abs(jet->partonFlavour()); 
        if(jet->pt() > max_pt && jet->isPFJet())
        {
            Leading_Jet = jet_index;
            max_pt = jet->pt();
            
        }
        jet_index++;
    }

    bool FLAG_Leading_Jet = true;
    if(Leading_Jet <0){
        FLAG_Leading_Jet = false;
    }
    if(FLAG_Leading_Jet){
        bool FLAG_On_PartonFlavour = false;
        const pat::Jet * jet = &(jets->at(Leading_Jet));
        int partonFlavour = TMath::Abs(jet->partonFlavour());
        if(partonFlavour ==21 ||(partonFlavour<=3)){
           FLAG_On_PartonFlavour =  true; 
        }
        if (FLAG_On_PartonFlavour){
            jet_px = jet->px();
            jet_py = jet->py();
            jet_pz = jet->pz();
            jet_energy = jet->energy();
            jet_eta = jet->eta();
            jet_phi = jet->phi();
            jet_pt = jet->pt();
            jet_partonFlavour = partonFlavour;
            jet_hadronFlavour = jet->hadronFlavour();
            jet_neutralMultiplicity = jet->neutralMultiplicity();
            jet_chargedMultiplicity = jet->chargedMultiplicity();
            jet_charge = jet->jetCharge();
            unsigned dn = jet->numberOfDaughters();
            constituent_number = 0 ; 
            for(unsigned idx = 0 ; idx < dn ; idx++)
            {
                const reco::Candidate *cand  = (jet->daughter(idx));
                constituent_px[idx] = cand->px();
                constituent_py[idx] = cand->py();
                constituent_pz[idx] = cand->pz();
                constituent_energy[idx] = cand->energy();
                constituent_pt[idx] = cand->pt();
                constituent_eta[idx] = cand->eta();
                constituent_phi[idx] = cand->phi();
                constituent_charge[idx] = cand->charge();
                constituent_number+=1;
            }
            cluster_number= 0;
            edm::Handle<edm::View<reco::CaloCluster>> clusters;
            iEvent.getByToken(cluster_token,clusters);
            for(auto cluster = clusters->begin() ; cluster != clusters->end(); cluster++)
            {
                //double deta = cluster->eta() - jet_eta;
                //double dphi = cluster->phi() - jet_phi;
    //            double dR = TMath::Sqrt(deta*deta + dphi*dphi);
                    cluster_energy[cluster_number] = cluster->energy();
                    cluster_eta[cluster_number] = cluster->eta();
                    cluster_phi[cluster_number] = cluster->phi();
                    cluster_z[cluster_number] = cluster->z();
                    cluster_size[cluster_number] = cluster->size();
                    
                    if(TMath::Abs(cluster->z())>367.699 && tool->getLayer(cluster->seed()) <28 )
                    {
                        cluster_Layer[cluster_number] = tool->getLayer(cluster->seed())+28;
                    }
                    else{
                        cluster_Layer[cluster_number] = tool->getLayer(cluster->seed());
                    }
                    cluster_number++;
            }
            tree->Fill();
        }
//    double eta = TMath::Abs(jets->at(Leading_Jet).eta()) ;
    }
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
  // if the SetupData is always needed
  auto setup = iSetup.getData(setupToken_);
  // if need the ESHandle to check if the SetupData was there or not
  auto pSetup = iSetup.getHandle(setupToken_);
#endif
}

// ------------ method called once each job just before starting event loop  ------------
void Ntuple_Analyzer::beginJob() {
  // please remove this method if not needed
  tree->Branch("jet_eta",&jet_eta,"jet_eta/D");
  tree->Branch("jet_phi",&jet_phi,"jet_phi/D");
  tree->Branch("jet_pt",&jet_pt,"jet_pt/D");
  tree->Branch("jet_px",&jet_px,"jet_px/D");
  tree->Branch("jet_py",&jet_py,"jet_py/D");
  tree->Branch("jet_pz",&jet_pz,"jet_pz/D");
  tree->Branch("jet_charge",&jet_charge,"jet_charge/F");
  tree->Branch("jet_energy",&jet_energy,"jet_energy/D");
  tree->Branch("jet_partonFlavour",&jet_partonFlavour,"jet_partonFlavour/I");
  tree->Branch("jet_hadronFlavour",&jet_hadronFlavour,"jet_hadronFlavour/I");
  tree->Branch("jet_neutralMultiplicity",&jet_neutralMultiplicity,"jet_neutralMultiplicity/I");
  tree->Branch("jet_chargedMultiplicity",&jet_chargedMultiplicity,"jet_chargedMultiplicity/I");
  
  tree->Branch("constituent_number",&constituent_number,"constituent_number/I");
  tree->Branch("constituent_eta",constituent_eta,"constituent_eta[constituent_number]/D");
  tree->Branch("constituent_phi",constituent_phi,"constituent_phi[constituent_number]/D");
  tree->Branch("constituent_pt",constituent_pt,"constituent_pt[constituent_number]/D");
  tree->Branch("constituent_px",constituent_px,"constituent_px[constituent_number]/D");
  tree->Branch("constituent_py",constituent_py,"constituent_py[constituent_number]/D");
  tree->Branch("constituent_pz",constituent_pz,"constituent_pz[constituent_number]/D");
  tree->Branch("constituent_energy",constituent_energy,"constituent_energy[constituent_number]/D");
  tree->Branch("constituent_charge",constituent_charge,"constituent_charge[constituent_number]/I");
   
  tree->Branch("cluster_number",&cluster_number,"cluster_number/I");
  tree->Branch("cluster_eta",cluster_eta,"cluster_eta[cluster_number]/D");
  tree->Branch("cluster_phi",cluster_phi,"cluster_phi[cluster_number]/D");
  tree->Branch("cluster_energy",cluster_energy,"cluster_energy[cluster_number]/D");
  tree->Branch("cluster_z",cluster_z,"cluster_z[cluster_number]/D");
  tree->Branch("cluster_Layer",cluster_Layer,"cluster_Layer[cluster_number]/I");
}

// ------------ method called once each job just after ending the event loop  ------------
void Ntuple_Analyzer::endJob() {
  // please remove this method if not needed
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void Ntuple_Analyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

  //Specify that only 'tracks' is allowed
  //To use, remove the default given above and uncomment below
  //ParameterSetDescription desc;
  //desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
  //descriptions.addWithDefaultLabel(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(Ntuple_Analyzer);
