[sffactorn]
Cat:    RSF/user/gee
Desc:   Missing data interpolation with 3-D plane-wave filter
DocCmd: sffactorn | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   mask rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.001 		
Param:  miter int  -  10 		number of interpolation iterations 
Param:  niter int  -  10 		number of factorization iterations 
Param:  npx int  -  100 		
Param:  npy int  -  100 		
Param:  nt int  -   -  		
Param:  nx int  -   -  		

