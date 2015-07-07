[sfsrmod3]
Cat:    RSF/user/psava
Desc:   3-D S/R modeling with extended split-step
DocCmd: sfsrmod3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fw_s data)
Port:   stdout rsf w req 	RSF standard output (containing Fw_r data)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   slo rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dtmax float  -  0.004 		time error 
Param:  eps float  -  0.01 		stability parameter 
Param:  nrmax int  -  1 		maximum number of refs 
Param:  ompchunk int  -  1 		OpenMP data chunk size 
Param:  ompnth int  -  0 		OpenMP available threads 
Param:  pmx int  -  0 		padding on x 
Param:  pmy int  -  0 		padding on y 
Param:  sls string  -   -  		auxiliary input file name
Param:  tmx int  -  0 		taper on x   
Param:  tmy int  -  0 		taper on y   
Param:  twoway enum-bool  -  n 		two-way traveltime 
Param:  verb enum-bool  -  y 		verbosity flag 

