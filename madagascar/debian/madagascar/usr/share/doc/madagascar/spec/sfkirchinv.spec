[sfkirchinv]
Cat:    RSF/system/seismic
Desc:   Kirchhoff 2-D post-stack least-squares time migration with antialiasing
DocCmd: sfkirchinv | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  err string  -   -  		output file for error 
Param:  hd enum-bool  -  y 		if y, apply half-derivative filter 
Param:  niter int  -  10 		number of iterations 
Param:  ps enum-bool  -  y 		if y, apply pseudo-unitary weighting 
Param:  sw int  -  0 		if > 0, select a branch of the antialiasing operation 

