# MuonValidation
Cfg files to run the muon validation code 

voms-proxy-init -voms cms -rfc --valid 168:0                                                                                         

### Download the needed packages 

git-cms-addpkg Validation/RecoMuon 

scramv1 b -j 10

### Run muon only validation code (not full sequence)

For running only the muon validation (not the displaced muon validation, since for this you will need to run the full reco sequence)

```
cmsRun runAssociation.py 
```

``` 
cmsRun HARVESTrunAssociation.py
``` 

### RECO and full sequence of the muon only validation code

```                                                                                                                                 
cmsRun RecoFullGlobalPU_2026D49PU.py
```   

```
cmsRun HARVESTrunAssociation.py
```


### Sent jobs to condor

voms-proxy-init -voms cms -rfc --valid 168:0

cp /tmp/x509up_u15250  /afs/cern.ch/user/c/calderon/. 


```
condor_submit submitjobs.jds      
```
