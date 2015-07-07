[sfsplineplane]
Cat:    RSF/user/gee
Desc:   B-spline plane-wave filter
DocCmd: sfsplineplane | cat
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eps float  -   -  		
LDesc:  (defaults to: SF_EPS)
Param:  lag string  -   -  		auxiliary output file name
Param:  niter int  -  20 		number of spectral decomposition iterations 
Param:  nw int  -  2 		filter size 
Param:  p float  -  0. 		plane-wave slope 

