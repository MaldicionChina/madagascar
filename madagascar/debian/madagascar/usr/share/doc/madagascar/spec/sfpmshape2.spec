[sfpmshape2]
Cat:    RSF/user/pwd
Desc:   Missing data interpolation in 2-D using plane-wave destruction and shaping regularization
DocCmd: sfpmshape2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  100 		number of iterations 
Param:  order int  -  1 		accuracy order 
Param:  rect1 int  -  3 		
Param:  rect2 int  -  3 		smoothing radius 

