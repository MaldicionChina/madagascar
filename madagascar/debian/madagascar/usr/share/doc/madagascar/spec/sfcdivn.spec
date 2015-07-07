[sfcdivn]
Cat:    RSF/user/fomels
Desc:   Smooth division for complex data
DocCmd: sfcdivn | cat
Port:   stdin  rsf r req 	RSF standard input (containing fnum data)
Port:   stdout rsf w req 	RSF standard output (containing frat data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  niter int  -  100 		number of iterations 
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  verb enum-bool  -  y 		verbosity 

