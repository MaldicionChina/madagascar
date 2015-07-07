[sfplanesignoi]
Cat:    RSF/user/pwd
Desc:   Signal and noise separation using plane-wave destruction filters
DocCmd: sfplanesignoi | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   ndip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sdip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  1. 		regularization parameter 
Param:  niter int  -  50 		maximum number of iterations 
Param:  nj1 int  -  1 		antialiasing for noise dip 
Param:  nj2 int  -  1 		antialiasing for signal dip 
Param:  order int  -  1 		accuracy order 
Param:  verb enum-bool  -  n 		verbosity flag 

