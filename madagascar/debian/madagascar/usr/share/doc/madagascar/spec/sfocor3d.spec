[sfocor3d]
Cat:    RSF/user/psava
Desc:   
DocCmd: sfocor3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwfl data)
Port:   stdout rsf w req 	RSF standard output (containing Fcor data)
Port:   opr rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag
Param:  ntlag int  -  100 		
Param:  nxlag int  -  0 		
Param:  nylag int  -  0 		
Param:  nzlag int  -  0 		
Param:  ocox float  -  0.0 		
Param:  ocoy float  -  0.0 		
Param:  ocoz float  -  0.0 		
Param:  verb enum-bool  -  n 		verbosity flag

