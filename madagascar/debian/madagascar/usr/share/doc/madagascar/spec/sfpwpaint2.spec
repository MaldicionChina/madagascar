[sfpwpaint2]
Cat:    RSF/user/pwd
Desc:   3-D painting by plane-wave construction
DocCmd: sfpwpaint2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing dip data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   cost rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization 
Param:  order int  -  1 		accuracy order 
Param:  seed string  -   -  		auxiliary input file name
Param:  verb enum-bool  -  n 		

