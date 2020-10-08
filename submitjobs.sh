#!/bin/bash
#$ -N mkShapes__ggH2016_v6__ALL__VZ.12
#export X509_USER_PROXY=/afs/cern.ch/user/c/calderon/.proxy
export X509_USER_PROXY=/afs/cern.ch/user/c/calderon/x509up_u15250
voms-proxy-info
export SCRAM_ARCH=slc7_amd64_gcc820
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
cd /afs/cern.ch/work/c/calderon/private/CMSSW_11_2_0_pre1/
eval `scramv1 ru -sh`
ulimit -c 0 
cd '/afs/cern.ch/work/c/calderon/private/CMSSW_11_2_0_pre1/src/runDQM'

pwd 

pycfg="/afs/cern.ch/work/c/calderon/private/CMSSW_11_2_0_pre1/src/runDQM/runAssociation_1.py"

cmsRun $pycfg
