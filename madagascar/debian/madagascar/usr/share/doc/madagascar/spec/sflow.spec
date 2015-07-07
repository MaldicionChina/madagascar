[sflow]
Cat:    RSF/user/chenyk
Desc:   Calculating local (signal-and-noise) orthogonalization weight (LOW)
DocCmd: sflow | cat
Port:   stdin  rsf r req 	RSF standard input (containing fnoi data)
Port:   stdout rsf w req 	RSF standard output (containing flow data)
Port:   sig rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -   -  		regularization 
LDesc:  (defaults to: 0.0f)
Param:  niter int  -  100 		number of iterations 
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  verb enum-bool  -  y 		verbosity 

