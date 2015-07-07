[sfshapefill]
Cat:    RSF/user/fomels
Desc:   Missing data interpolation in 2-D by Laplacian regularization
DocCmd: sfshapefill | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dim int  -   -  		dimensionality 
LDesc:  (defaults to: dim)
Param:  mask string  -   -  		optional mask file with zeroes for missing data locations (auxiliary input file name)
Param:  niter int  -  200 		number of iterations 
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  verb enum-bool  -  n 		verbosity flag 

