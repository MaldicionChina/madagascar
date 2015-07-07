[sftspline]
Cat:    RSF/user/gee
Desc:   Helix filters for spline in tension
DocCmd: sftspline | cat
Port:   stdout rsf w req 	RSF standard output (containing flt data)
Param:  eps float  -   -  		tolerance for filter compressing 
LDesc:  (defaults to: FLT_EPSILON)
Param:  lag string  -   -  		
Param:  niter int  -  20 		number of iterations 
Param:  tension float  -  0. 		spline tension 

