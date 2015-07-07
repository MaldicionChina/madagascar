[sfpredict]
Cat:    RSF/user/pwd
Desc:   2-D plane-wave prediction
DocCmd: sfpredict | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		
Param:  order int  -  1 		accuracy order 

