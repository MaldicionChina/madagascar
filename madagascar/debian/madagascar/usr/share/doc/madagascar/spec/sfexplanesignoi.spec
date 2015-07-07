[sfexplanesignoi]
Cat:    RSF/user/pwd
Desc:   Signal and noise separation using both frequency components and dips
DocCmd: sfexplanesignoi | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   freq rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ndip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sdip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  1. 		regularization parameter 
Param:  niter int  -  50 		maximum number of iterations 
Param:  nj1 int  -  1 		antialiasing for first dip 
Param:  nj2 int  -  1 		antialiasing for second dip 
Param:  order int  -  1 		accuracy order 
Param:  verb enum-bool  -  n 		verbosity flag 

