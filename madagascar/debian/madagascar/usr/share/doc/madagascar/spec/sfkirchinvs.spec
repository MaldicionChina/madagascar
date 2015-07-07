[sfkirchinvs]
Cat:    RSF/user/seisinv
Desc:   Kirchhoff 2-D post-stack least-squares time migration with sparse constrains
DocCmd: sfkirchinvs | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0. 		regularization parameters 
Param:  err string  -   -  		output file for error 
Param:  hd enum-bool  -  y 		if y, apply half-derivative filter 
Param:  liter int  -  5 		number of linear iterations 
Param:  niter int  -  5 		number of non-linear iterations, when niter=1, it's linear 
Param:  ps enum-bool  -  y 		if y, apply pseudo-unitary weighting 
Param:  sw int  -  0 		if > 0, select a branch of the antialiasing operation 
Param:  verb enum-bool  -  n 		verbosity flag 

