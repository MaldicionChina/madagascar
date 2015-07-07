[sft2diter]
Cat:    RSF/user/llisiw
Desc:   Time-to-depth conversion (linear operator)
DocCmd: sft2diter | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  cgiter int  -  200 		number of CG iterations 
Param:  dix string  -   -  		auxiliary input file name
Param:  eps float  -  0.1 		regularization parameter 
Param:  f0 string  -   -  		auxiliary input file name
Param:  mask string  -   -  		auxiliary input file name
Param:  prec string  -   -  		auxiliary input file name
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  s0 string  -   -  		auxiliary input file name
Param:  shape enum-bool  -  n 		regularization (default Tikhnov) 
Param:  t0 string  -   -  		auxiliary input file name
Param:  tol float  -  1.e-6 		tolerance for shaping regularization 
Param:  velocity enum-bool  -  y 		y, inputs are velocity / n, slowness-squared 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  what string  -   -  		what to compute (default inversion) 
Param:  x0 string  -   -  		auxiliary input file name

