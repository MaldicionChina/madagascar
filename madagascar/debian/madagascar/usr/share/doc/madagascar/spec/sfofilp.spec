[sfofilp]
Cat:    RSF/user/fomels
Desc:   2-D missing data interpolation by differential offset continuation
DocCmd: sfofilp | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   known rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  niter int  -  10 		number of iterations 
Param:  simple enum-bool  -  n 		if y, use simple h derivative for regularization 

