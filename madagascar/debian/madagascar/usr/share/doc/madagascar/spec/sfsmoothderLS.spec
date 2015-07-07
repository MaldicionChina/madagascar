[sfsmoothderLS]
Cat:    RSF/user/lcasasan
Desc:   Convert input to its derivative using LS and shaping regularization
DocCmd: sfsmoothderLS | cat
Port:   stdin  rsf r req 	RSF standard input (containing DATA data)
Port:   stdout rsf w req 	RSF standard output (containing MODEL data)
Param:  dataout string  -   -  		optionally, output predicted data (auxiliary output file name)
Param:  niter int  -  100 		maximum number of iterations 
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))

