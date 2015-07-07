[sfdsrtomo]
Cat:    RSF/user/llisiw
Desc:   Prestack first-arrival traveltime tomography (DSR)
DocCmd: sfdsrtomo | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		adjoint flag (for what=linear) 
Param:  causal enum-bool  -  y 		if y, neglect non-causal branches of DSR 
Param:  cgiter int  -  10 		number of conjugate-gradient iterations 
Param:  eps float  -  0. 		regularization parameter 
Param:  flag string  -   -  		auxiliary input file name
Param:  grad string  -   -  		auxiliary input file name
Param:  liter int  -  5 		number of line-search iterations 
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  5 		number of inversion iterations 
Param:  nloop int  -  10 		number of bisection root-search 
Param:  prec string  -   -  		auxiliary input file name
Param:  reco string  -   -  		auxiliary input file name
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  scale enum-bool  -  n 		if y, scale gradient before line-search 
Param:  scale0 float  -  0.5 		gradient scale max ratio (if scale=y) 
Param:  shape enum-bool  -  n 		shaping regularization (default no) 
Param:  thres float  -  5.e-5 		threshold (percentage) 
Param:  time string  -   -  		auxiliary input file name
Param:  tol float  -  1.e-3 		tolerance for bisection root-search 
Param:  velocity enum-bool  -  y 		if y, the input is velocity; n, slowness-squared 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  what string  -   -  		what to compute (default tomography) 

