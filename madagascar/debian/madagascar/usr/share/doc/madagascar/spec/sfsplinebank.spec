[sfsplinebank]
Cat:    RSF/user/gee
Desc:   Prepare a filter bank for B-spline plane wave filters
DocCmd: sfsplinebank | cat
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eps float  -   -  		tolerance 
LDesc:  (defaults to: FLT_EPSILON)
Param:  lag string  -   -  		
Param:  nh string  -   -  		
Param:  niter int  -  20 		number of iterations 
Param:  np int  -   -  		number of dips 
Param:  nt int  -  40 		length of the fast axis 
Param:  pmax float  -  2. 		maximum dip 

