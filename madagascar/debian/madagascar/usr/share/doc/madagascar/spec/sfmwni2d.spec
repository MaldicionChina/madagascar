[sfmwni2d]
Cat:    RSF/user/pyang
Desc:   2-D bandlimited minimum weighted-norm interpolation (MWNI)
DocCmd: sfmwni2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fin data)
Port:   stdout rsf w req 	RSF standard output (containing Fout data)
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  100 		total number iterations 
Param:  tol float  -  1.0e-6 		iteration tolerance 
Param:  verb enum-bool  -  n 		verbosity 

