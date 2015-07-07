[sftdconvert]
Cat:    RSF/user/llisiw
Desc:   Iterative time-to-depth velocity conversion
DocCmd: sftdconvert | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  cgiter int  -  200 		number of CG iterations 
Param:  cost string  -   -  		auxiliary output file name
Param:  dix string  -   -  		auxiliary input file name
Param:  eps float  -  0.1 		regularization parameter 
Param:  f0 string  -   -  		auxiliary output file name
Param:  grad string  -   -  		auxiliary output file name
Param:  mask string  -   -  		auxiliary input file name
Param:  mval string  -   -  		
Param:  niter int  -  1 		number of nonlinear updates 
Param:  nline int  -  0 		maximum number of line search (default turned-off) 
Param:  order int  -  1 		fastmarch accuracy order 
Param:  prec string  -   -  		auxiliary input file name
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  shape enum-bool  -  n 		regularization (default Tikhnov) 
Param:  t0 string  -   -  		auxiliary output file name
Param:  thres float  -  10. 		thresholding for caustics 
Param:  tol float  -  1.e-6 		tolerance for shaping regularization 
Param:  velocity enum-bool  -  y 		y, input is velocity / n, slowness-squared 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  x0 string  -   -  		auxiliary output file name

