[sfewefd2dtti]
Cat:    RSF/user/jyan
Desc:   elastic time-domain FD modeling
DocCmd: sfewefd2dtti | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwav data)
Port:   stdout rsf w req 	RSF standard output (containing Fdat data)
Port:   ccc rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  free enum-bool  -  n 		free surface flag 
Param:  jdata int  -  1 		
Param:  jsnap int  -   -  		
LDesc:  (defaults to: nt)
Param:  nbell int  -  1 		bell size 
Param:  nq1 int  -   -  		
LDesc:  (defaults to: sf_n(az))
Param:  nq2 int  -   -  		
LDesc:  (defaults to: sf_n(ax))
Param:  ompchunk int  -  1 		OpenMP data chunk size 
Param:  ompnth int  -  0 		OpenMP available threads 
Param:  opot enum-bool  -  n 		output potential 
Param:  oq1 float  -   -  		
LDesc:  (defaults to: sf_o(az))
Param:  oq2 float  -   -  		
LDesc:  (defaults to: sf_o(ax))
Param:  snap enum-bool  -  n 		wavefield snapshots flag 
Param:  ssou enum-bool  -  n 		stress source 
Param:  verb enum-bool  -  n 		verbosity flag 

