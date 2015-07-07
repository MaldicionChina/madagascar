[sfpwpaint]
Cat:    RSF/user/pwd
Desc:   Painting by plane-wave construction
DocCmd: sfpwpaint | cat
Port:   stdin  rsf r req 	RSF standard input (containing dip data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eps float  -  0.01 		regularization 
Param:  i0 int  -  0 		reference trace 
Param:  order int  -  1 		accuracy order 
Param:  seed string  -   -  		auxiliary input file name
Param:  verb enum-bool  -  n 		

