[sflwefd2d]
Cat:    RSF/user/psava
Desc:   linearized acoustic time-domain FD modeling
DocCmd: sflwefd2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwav data)
Port:   stdout rsf w req 	RSF standard output (containing Fdat data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   lid rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   liw rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  expl enum-bool  -  n 		'exploding reflector' 
Param:  free enum-bool  -  n 		free surface flag 
Param:  jdata int  -  1 		
Param:  jsnap int  -   -  		
LDesc:  (defaults to: nt)
Param:  nqx int  -   -  		
LDesc:  (defaults to: sf_n(a2))
Param:  nqz int  -   -  		
LDesc:  (defaults to: sf_n(a1))
Param:  ompchunk int  -  1 		OpenMP data chunk size 
Param:  ompnth int  -  0 		OpenMP available threads 
Param:  oqx float  -   -  		
LDesc:  (defaults to: sf_o(a2))
Param:  oqz float  -   -  		
LDesc:  (defaults to: sf_o(a1))
Param:  snap enum-bool  -  n 		wavefield snapshots flag 
Param:  verb enum-bool  -  n 		verbosity flag 

