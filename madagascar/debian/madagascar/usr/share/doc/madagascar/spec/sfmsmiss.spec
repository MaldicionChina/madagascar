[sfmsmiss]
Cat:    RSF/user/gee
Desc:   Multiscale missing data interpolation (N-dimensional)
DocCmd: sfmsmiss | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  lag string  -   -  		optional input file with filter lags 
Param:  mask string  -   -  		optional input mask file for known data (auxiliary input file name)
Param:  niter int  -  100 		Number of iterations 

