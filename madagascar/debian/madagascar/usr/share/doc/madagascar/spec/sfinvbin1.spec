[sfinvbin1]
Cat:    RSF/user/gee
Desc:   1-D inverse interpolation
DocCmd: sfinvbin1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dx float  -   -  		grid sampling 
Param:  eps float  -  0.2 		regularization parameter 
Param:  filter int  -  1 		filter type 
Param:  head string  -   -  		
Param:  niter int  -   -  		number of conjugate-gradient iterations 
LDesc:  (defaults to: nx)
Param:  nx int  -   -  		number of bins 
Param:  pef enum-bool  -  n 		if y, use PEF for regularization 
Param:  prec enum-bool  -  y 		if y, use preconditioning 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  x0 float  -   -  		grid origin 
LDesc:  (defaults to: xmin)
Param:  xmax float  -   -  		
Param:  xmin float  -   -  		grid size 

