[sffactorm]
Cat:    RSF/user/gee
Desc:   Plane-wave destruction with 3-D plane-wave filter
DocCmd: sffactorm | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.001 		
Param:  niter int  -  10 		number of iterations 
Param:  npx int  -  100 		
Param:  npy int  -  100 		np = npx *npy; 
Param:  nt int  -   -  		
Param:  nx int  -   -  		

