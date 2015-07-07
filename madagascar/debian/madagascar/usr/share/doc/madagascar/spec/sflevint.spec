[sflevint]
Cat:    RSF/user/gee
Desc:   Leveler inverse interpolation in 1-D
DocCmd: sflevint | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dx float  -   -  		grid sampling 
Param:  eps float  -  0.2 		regularization parameter 
Param:  head string  -   -  		
Param:  na int  -  3 		
Param:  niter int  -   -  		
LDesc:  (defaults to: 1+m1*3/2)
Param:  nx int  -   -  		number of bins 
Param:  x0 float  -   -  		grid origin 

