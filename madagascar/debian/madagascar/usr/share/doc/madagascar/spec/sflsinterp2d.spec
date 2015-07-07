[sflsinterp2d]
Cat:    RSF/user/pyang
Desc:   Least-squares interpolation for 2D validition
DocCmd: sflsinterp2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fin data)
Port:   stdout rsf w req 	RSF standard output (containing Fout data)
Param:  eps float  -  1.e-2 		regularization parameter 
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  100 		inner iterations 
Param:  nouter int  -  5 		outer iterations 
Param:  verb enum-bool  -  n 		verbosity 

