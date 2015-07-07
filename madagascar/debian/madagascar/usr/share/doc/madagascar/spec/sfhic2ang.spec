[sfhic2ang]
Cat:    RSF/user/psava
Desc:   angle decomposition of CIPs
DocCmd: sfhic2ang | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fcip data)
Port:   stdout rsf w req 	RSF standard output (containing Fang data)
Port:   ani rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   nor rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   tlt rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  y 		adj flag 
Param:  anis enum-bool  -  n 		anisotropy flag 
Param:  dht float  -  1. 		
Param:  dhx float  -  1. 		
Param:  dhy float  -  1. 		
Param:  dph float  -  1. 		
Param:  dps float  -  0.2 		
Param:  dth float  -  1. 		
Param:  nht int  -  1 		
Param:  nhx int  -  1 		
Param:  nhy int  -  1 		
Param:  nph int  -  360 		
Param:  nps int  -  251 		
Param:  nth int  -  90 		
Param:  oht float  -  0. 		
Param:  ohx float  -  0 		
Param:  ohy float  -  0 		
Param:  oph float  -  -180 		
Param:  ops float  -  -25 		
Param:  oth float  -  0 		
Param:  verb enum-bool  -  n 		verbosity flag 

