[sflsrtm2d]
Cat:    RSF/user/pyang
Desc:   2-D zero-offset least-squares reverse time migration (LSRTM)
DocCmd: sflsrtm2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing imag data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  n0 int  -  0 		shot depth in the grid 
Param:  niter int  -  10 		totol number of least-squares iteration
Param:  tol float  -  1.e-12 		tolerance of inversion 
Param:  verb enum-bool  -  n 		verbosity 

