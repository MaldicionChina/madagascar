[sfpwsmooth]
Cat:    RSF/user/pwd
Desc:   2-D structure-enhancing filtering
DocCmd: sfpwsmooth | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  eps float  -  0.01 		regularization 
Param:  ns int  -  0 		smoothing radius 
Param:  order int  -  1 		accuracy order 
Param:  verb enum-bool  -  n 		verbosity flag 

