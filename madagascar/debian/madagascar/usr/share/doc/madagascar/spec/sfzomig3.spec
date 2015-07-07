[sfzomig3]
Cat:    RSF/user/psava
Desc:   3-D zero-offset modeling/migration with extended SSF
DocCmd: sfzomig3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fd data)
Port:   stdout rsf w req 	RSF standard output (containing Fw data)
Port:   slo rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  causal enum-bool  -  n 		y=causal; n=anti-causal 
Param:  dtmax float  -  0.004 		time error 
Param:  dw float  -   -  		
Param:  eps float  -  0.01 		stability parameter 
Param:  inv enum-bool  -  n 		y=modeling; n=migration 
Param:  mode string  -   -  		
Param:  nrmax int  -  1 		maximum references 
Param:  nw int  -   -  		
Param:  ompchunk int  -  1 		OpenMP data chunk size 
Param:  ompnth int  -  0 		OpenMP available threads 
Param:  ow float  -  0. 		
Param:  pmx int  -  0 		padding on x 
Param:  pmy int  -  0 		padding on y
Param:  tmx int  -  0 		taper on x
Param:  tmy int  -  0 		taper on y 
Param:  twoway enum-bool  -  y 		two-way traveltime 
Param:  verb enum-bool  -  n 		verbosity flag 

