[sfinvrec1]
Cat:    RSF/user/gee
Desc:   1-D inverse interpolation with recursive filtering
DocCmd: sfinvrec1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dx float  -   -  		grid sampling 
Param:  eps float  -  0.2 		regularization parameter 
Param:  head string  -   -  		
Param:  lag string  -   -  		optional input file with filter lags (auxiliary input file name)
Param:  movie enum-bool  -  n 		verbosity flag 
Param:  niter int  -   -  		number of conjugate-gradient iterations 
LDesc:  (defaults to: nx)
Param:  nw int  -  2 		interpolator size 
Param:  nx int  -   -  		number of bins 
Param:  spline enum-bool  -  n 		if use spline interpolation 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  x0 float  -   -  		grid origin 
LDesc:  (defaults to: xmin)
Param:  xmax float  -   -  		
Param:  xmin float  -   -  		grid size 

