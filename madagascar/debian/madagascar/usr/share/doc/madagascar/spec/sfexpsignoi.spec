[sfexpsignoi]
Cat:    RSF/user/pwd
Desc:   Signal and noise separation using frequency components
DocCmd: sfexpsignoi | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   freq rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  1. 		regularization parameter 
Param:  niter int  -  50 		maximum number of iterations 
Param:  verb enum-bool  -  n 		verbosity flag 

