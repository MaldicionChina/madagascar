[sfseisigk]
Cat:    RSF/user/pwd
Desc:   Signal component separation using seislet transforms
DocCmd: sfseisigk | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dips rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0. 		regularization parameter 
Param:  eps0 float  -  0.01 		regularization for seislet 
Param:  niter int  -  50 		maximum number of iterations 
Param:  nliter int  -  1 		number of reweighting iterations 
Param:  order int  -  1 		accuracy order 
Param:  type string  -   -  		wavelet type (haar,linear) 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  weight string  -   -  		auxiliary output file name

