[sfmiss1]
Cat:    RSF/user/gee
Desc:   Missing data interpolation in 1-D
DocCmd: sfmiss1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  diter int  -   -  		iteration step 
LDesc:  (defaults to: niter)
Param:  filtin string  -   -  		auxiliary input file name
Param:  niter int  -   -  		number of iterations 
LDesc:  (defaults to: n1)
Param:  step string  -   -  		linear solver type 

