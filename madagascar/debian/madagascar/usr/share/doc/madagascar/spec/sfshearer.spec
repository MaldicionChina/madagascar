[sfshearer]
Cat:    RSF/user/fomels
Desc:   Preconditioning for traveltime picking
DocCmd: sfshearer | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  long int  -  10 		long smoothing radius 
Param:  niter int  -  100 		number of iterations 
Param:  order int  -  10 		Hilbert transformer order 
Param:  ref float  -  1. 		Hilbert transformer reference (0.5 < ref <= 1) 
Param:  short int  -  1 		short smoothing radius 

