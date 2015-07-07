[sfplanemis3]
Cat:    RSF/user/pwd
Desc:   Missing data interpolation in 3-D using plane-wave destruction
DocCmd: sfplanemis3 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  100 		number of iterations 
Param:  nj1 int  -  1 		
Param:  nj2 int  -  1 		antialiasing 
Param:  order int  -  1 		accuracy order 
Param:  seed int  -   -  		random seed 
LDesc:  (defaults to: time(NULL))
Param:  var float  -  0. 		noise variance 
Param:  verb enum-bool  -  n 		verbosity flag 

