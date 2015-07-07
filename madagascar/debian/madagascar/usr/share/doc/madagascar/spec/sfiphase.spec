[sfiphase]
Cat:    RSF/user/fomels
Desc:   Smooth estimate of instantaneous frequency
DocCmd: sfiphase | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  band enum-bool  -  n 		if y, compute instantaneous bandwidth 
Param:  complex enum-bool  -  n 		if y, use complex-valued computations 
Param:  hertz enum-bool  -  n 		if y, convert output to Hertz 
Param:  niter int  -  100 		number of iterations 
Param:  order int  -  100 		Hilbert transformer order 
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  ref float  -  1. 		Hilbert transformer reference (0.5 < ref <= 1) 
Param:  verb enum-bool  -  n 		verbosity 

