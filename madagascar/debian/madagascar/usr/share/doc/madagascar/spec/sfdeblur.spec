[sfdeblur]
Cat:    RSF/user/fomels
Desc:   Non-stationary debluring by inversion
DocCmd: sfdeblur | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   rect rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0. 		regularization parameter 
Param:  niter int  -  100 		number of iterations 
Param:  nliter int  -  1 		number of nonlinear iterations 
Param:  verb enum-bool  -  n 		verbosity flag 

