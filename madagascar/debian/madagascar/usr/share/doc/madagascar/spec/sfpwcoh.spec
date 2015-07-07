[sfpwcoh]
Cat:    RSF/user/pwd
Desc:   Coherency by plane-wave construction
DocCmd: sfpwcoh | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   a2 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   b2 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization 
Param:  order int  -  1 		accuracy order 
Param:  rect int  -  2 		spread 
Param:  verb enum-bool  -  n 		

