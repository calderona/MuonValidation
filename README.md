# MuonValidation
Cfg files to run the muon validation code 

voms-proxy-init -voms cms -rfc --valid 168:0                                                                                         

### runSummary.py and HARVESTrunAssociation.py

For running only the muon validation (not the displaced muon validation, since for this you will need to run the full reco sequence)

```
cmsRun runSummary.py 
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
