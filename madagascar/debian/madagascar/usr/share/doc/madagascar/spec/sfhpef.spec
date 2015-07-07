[sfhpef]
Cat:    RSF/user/gee
Desc:   Multi-dimensional PEF (prediction error filter) estimation on a helix
DocCmd: sfhpef | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing filt data)
Param:  a int-list  -   -  		 [dim]
Param:  center int-list  -   -  		 [dim]
Param:  gap int-list  -   -  		 [dim]
Param:  lag string  -   -  		output file for filter lags 
Param:  maskin string  -   -  		optional input mask file (auxiliary input file name)
Param:  maskout string  -   -  		optional output mask file 
Param:  n int-list  -   -  		 [dim]
Param:  na int  -  0 		filter size 
Param:  niter int  -   -  		number of iterations 
LDesc:  (defaults to: 2*(aa->nh))
Param:  tol float  -  1.e-6 		tolerance for filter compression 

