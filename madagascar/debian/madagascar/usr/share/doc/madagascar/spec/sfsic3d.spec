[sfsic3d]
Cat:    RSF/user/psava
Desc:   Local slant stacks I.C
DocCmd: sfsic3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fs data)
Port:   stdout rsf w req 	RSF standard output (containing Fi data)
Port:   ur rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  danga float  -  1.0 		
Param:  dangb float  -  1.0 		
Param:  dl float  -  1. 		
Param:  nanga int  -  1 		
Param:  nangb int  -  1 		
Param:  nl int  -  1 		
Param:  oanga float  -  0.0 		
Param:  oangb float  -  0.0 		
Param:  ol float  -  0. 		
Param:  ompchunk int  -  1 		OpenMP data chunk size 
Param:  sig float  -  1.0 		
Param:  stack enum-bool  -  n 		
Param:  verb enum-bool  -  n 		verbosity flag 

