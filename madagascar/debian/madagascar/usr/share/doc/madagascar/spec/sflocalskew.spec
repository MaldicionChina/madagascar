[sflocalskew]
Cat:    RSF/user/fomels
Desc:   Rotate phase and compute local skewness
DocCmd: sflocalskew | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (containing sim data)
Param:  a0 float  -  -180. 		first angle 
Param:  const enum-bool  -  n 		if y, compute inverse varimax 
Param:  da float  -  1.0 		angle increment 
Param:  eps float  -   -  		regularization 
LDesc:  (defaults to: 0.0f)
Param:  inv enum-bool  -  y 		inverse similarity 
Param:  na int  -  360 		number of angles 
Param:  niter int  -  20 		maximum number of iterations 
Param:  order int  -  100 		Hilbert transformer order 
Param:  rect int  -  3 		smoothing radius 
Param:  ref float  -  1. 		Hilbert transformer reference (0.5 < ref <= 1) 
Param:  verb enum-bool  -  y 		verbosity 

