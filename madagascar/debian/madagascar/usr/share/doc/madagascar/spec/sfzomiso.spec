[sfzomiso]
Cat:    RSF/user/xuxin
Desc:   zero-offset isotropic reverse-time migration
DocCmd: sfzomiso | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fimag data)
Port:   stdout rsf w req 	RSF standard output (containing Fdata data)
Port:   cr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sigm rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   velo rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vmap rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wave rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  bxh int  -  0 		
Param:  bxl int  -  0 		
Param:  bzh int  -  0 		
Param:  bzl int  -  0 		
Param:  cxh float  -  1. 		
Param:  cxl float  -  1. 		
Param:  czh float  -  1. 		
Param:  czl float  -  1. 		
Param:  dt float  -  1. 		time d (if inv=y) 
Param:  eps float  -  1 		regularize sigma 
Param:  inv enum-bool  -  n 		if y, modeling; if n, migration 
Param:  n3 int  -   -  		wave time n 
LDesc:  (defaults to: nt)
Param:  nt int  -  1 		time n (if inv=y) 
Param:  opt enum-bool  -  n 		optimze fft size 
Param:  tau enum-bool  -  n 		if y, tau domain; if n, cartesian 
Param:  verb enum-bool  -  n 		verbosity 

