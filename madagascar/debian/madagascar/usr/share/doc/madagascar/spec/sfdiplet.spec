[sfdiplet]
Cat:    RSF/user/pwd
Desc:   2-D Seislet frame
DocCmd: sfdiplet | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dips rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  decomp enum-bool  -  n 		do decomposition 
Param:  eps float  -  0.01 		regularization 
Param:  inv enum-bool  -  n 		if y, do inverse transform 
Param:  mask string  -   -  		(optional) data mask file (auxiliary input file name)
Param:  ncycle int  -  0 		number of iterations 
Param:  niter int  -  1 		number of Bregman iterations 
Param:  order int  -  1 		accuracy order 
Param:  perc float  -  50.0 		percentage for sharpening 
Param:  twhole enum-bool  -  y 		threshold flag, if y, whole model, otherwise, each component 
Param:  type string  -   -  		wavelet type (haar,linear,biorthogonal), default is linear 
Param:  verb enum-bool  -  y 		verbosity flag 

