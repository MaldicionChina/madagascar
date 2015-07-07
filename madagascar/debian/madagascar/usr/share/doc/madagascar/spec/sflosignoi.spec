[sflosignoi]
Cat:    RSF/user/gee
Desc:   Local signal and noise separation (N-dimensional)
DocCmd: sflosignoi | cat
Port:   stdin  rsf r req 	RSF standard input (containing dat data)
Port:   stdout rsf w req 	RSF standard output (containing signal data)
Port:   nfilt rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sfilt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -   -  		regularization parameter 
Param:  niter int  -  20 		number of iterations 
Param:  nlag string  -   -  		
Param:  slag string  -   -  		

