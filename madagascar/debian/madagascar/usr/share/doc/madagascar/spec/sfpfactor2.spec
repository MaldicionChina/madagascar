[sfpfactor2]
Cat:    RSF/user/gee
Desc:   Plane prediction filter on a helix
DocCmd: sfpfactor2 | cat
Port:   stdout rsf w req 	RSF standard output (containing filt data)
Param:  eps float  -   -  		compression tolerance 
LDesc:  (defaults to: FLT_EPSILON)
Param:  fixed enum-bool  -  y 		if fixed size 
Param:  lag string  -   -  		
Param:  na int  -  25 		filter size 
Param:  niter int  -  20 		number of factorization iterations 
Param:  nt int  -   -  		
Param:  nx int  -   -  		
Param:  p float  -   -  		
Param:  q float  -   -  		

