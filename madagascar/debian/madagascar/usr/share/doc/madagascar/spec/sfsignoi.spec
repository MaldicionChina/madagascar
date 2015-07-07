[sfsignoi]
Cat:    RSF/user/gee
Desc:   Signal and noise separation (N-dimensional)
DocCmd: sfsignoi | cat
Port:   stdin  rsf r req 	RSF standard input (containing dat data)
Port:   stdout rsf w req 	RSF standard output (containing signoi data)
Port:   nfilt rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sfilt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  epsilon float  -   -  		regularization parameter 
Param:  niter int  -  20 		number of iterations 
Param:  nlag string  -   -  		
Param:  slag string  -   -  		
Param:  spitz enum-bool  -  n 		if use Spitz method 
Param:  verb enum-bool  -  n 		verbosity flag 

