[sfdlct]
Cat:    RSF/user/pyang
Desc:   discrete linear chirp transfrom (DLCT)
DocCmd: sfdlct | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  C float  -  0.005 		C=2*Lambda/L, unit slice 
Param:  L int  -   -  		
Param:  inv enum-bool  -  n 		if y, do inverse transform (Here adjoint is the same as inverse!) 
Param:  verb enum-bool  -  n 		verbosity flag 

