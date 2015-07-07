[sfpwpaint3]
Cat:    RSF/user/pwd
Desc:   3-D painting by plane-wave construction
DocCmd: sfpwpaint3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing dip data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   cost rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   seed rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization 
Param:  order int  -  1 		accuracy order 
Param:  ref2 int  -  0 		
Param:  ref3 int  -  0 		reference trace 
Param:  verb enum-bool  -  n 		

