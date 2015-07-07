[sfcorop]
Cat:    RSF/user/psava
Desc:   
DocCmd: sfcorop | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fcor data)
Port:   stdout rsf w req 	RSF standard output (containing Fwfl data)
Port:   opr rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag
Param:  ncor int  -  100 		
Param:  verb enum-bool  -  n 		verbosity flag

