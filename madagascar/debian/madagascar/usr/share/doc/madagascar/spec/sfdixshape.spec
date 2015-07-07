[sfdixshape]
Cat:    RSF/user/pwd
Desc:   Convert RMS to interval velocity using LS and shaping regularization
DocCmd: sfdixshape | cat
Port:   stdin  rsf r req 	RSF standard input (containing vrms data)
Port:   stdout rsf w req 	RSF standard output (containing vint data)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   weight rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  lam float  -  1. 		operator scaling for inversion 
Param:  niter int  -  100 		maximum number of iterations 
Param:  order int  -  1 		accuracy order 
Param:  rect1 int  -  3 		
Param:  rect2 int  -  3 		smoothing radius 
Param:  vrmsout string  -   -  		optionally, output predicted vrms (auxiliary output file name)

