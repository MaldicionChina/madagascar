[sfcamig3]
Cat:    RSF/user/psava
Desc:   3-D common-azimuth modeling/migration with extended SSF
DocCmd: sfcamig3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fd data)
Port:   stdout rsf w req 	RSF standard output (containing Fw data)
Port:   slo rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dtmax float  -  0.004 		time error 
Param:  dw float  -   -  		
Param:  eps float  -  0.01 		stability parameter 
Param:  inv enum-bool  -  n 		y=modeling; n=migration 
Param:  mode string  -   -  		
Param:  nrmax int  -  1 		maximum number of refs 
Param:  nw int  -   -  		
Param:  ompchunk int  -  1 		OpenMP data chunk size 
Param:  ompnth int  -  0 		OpenMP available threads 
Param:  ow float  -  0. 		
Param:  phx int  -  0 		padding hx
Param:  pmx int  -  0 		padding mx
Param:  pmy int  -  0 		padding my
Param:  thx int  -  0 		taper hx 
Param:  tmx int  -  0 		taper mx 
Param:  tmy int  -  0 		taper my 
Param:  twoway enum-bool  -  n 		two-way traveltime 
Param:  verb enum-bool  -  n 		verbosity flag 

