[sfsimilarity]
Cat:    RSF/user/fomels
Desc:   Local similarity measure between two datasets
DocCmd: sfsimilarity | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   other rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -   -  		regularization 
LDesc:  (defaults to: 0.0f)
Param:  niter int  -  20 		maximum number of iterations 
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  verb enum-bool  -  y 		verbosity 

