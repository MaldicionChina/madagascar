[sfsrmig3]
Cat:    RSF/user/psava
Desc:   3-D S/R migration with extended SSF
DocCmd: sfsrmig3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fw_s data)
Port:   stdout rsf w req 	RSF standard output (containing Fi data)
Port:   cig rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   rwf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   slo rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dha float  -  2.0 		
Param:  dhb float  -  2.0 		
Param:  dhh float  -  0.1 		
Param:  dht float  -  0.1 		
Param:  dtmax float  -  0.004 		max time error 
Param:  eps float  -  0.01 		stability parameter 
Param:  hsym enum-bool  -  n 		
Param:  itype string  -   -  		imaging condition type
LDesc:         o = zero lag (default)
LDesc:         e = extended
LDesc:         x = space-lags
LDesc:         h = space-lags magnitude
LDesc:         t = time-lag
LDesc:      
Param:  nha int  -  180 		
Param:  nhb int  -  180 		
Param:  nhh int  -  1 		
Param:  nht int  -  1 		
Param:  nrmax int  -  1 		max number of refs 
Param:  oha float  -  0 		
Param:  ohb float  -  0 		
Param:  ohh float  -  0 		
Param:  oht float  -  0 		
Param:  ompchunk int  -  1 		OpenMP data chunk size 
Param:  ompnth int  -  0 		OpenMP available threads 
Param:  pmx int  -  0 		padding on x 
Param:  pmy int  -  0 		padding on y 
Param:  sls string  -   -  		auxiliary input file name
Param:  tmx int  -  0 		taper on x   
Param:  tmy int  -  0 		taper on y   
Param:  twoway enum-bool  -  n 		two-way traveltime 
Param:  verb enum-bool  -  y 		verbosity flag 
Param:  vpvs float  -  1. 		Vp/Vs ratio 

