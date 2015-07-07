[sflsprtm2d]
Cat:    RSF/user/pyang
Desc:   2-D prestack least-squares RTM using wavefield reconstruction
DocCmd: sflsprtm2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing shots data)
Port:   stdout rsf w req 	RSF standard output (containing imag data)
Port:   imgrtm rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  nb int  -  20 		number (thickness) of ABC on each side 
Param:  niter int  -  10 		totol number of least-squares iteration
Param:  verb enum-bool  -  y 		verbosity 

