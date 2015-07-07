[sffatomoomp]
Cat:    RSF/user/llisiw
Desc:   First-arrival Traveltime Tomography (OMP)
DocCmd: sffatomoomp | cat
Port:   stdin  rsf r req 	RSF standard input (containing sinp data)
Port:   stdout rsf w req 	RSF standard output (containing sout data)
Param:  eps float  -  0. 		regularization parameter (for both Ticknov and Shaping) 
Param:  grad string  -   -  		auxiliary output file name
Param:  misnorm string  -   -  		auxiliary output file name
Param:  niter int  -  1 		number of slowness inversion iterations 
Param:  nstep int  -  10 		number of linesearch 
Param:  order int  -  2 		fast marching accuracy order 
Param:  pow float  -  2. 		power raised for data weighting 
Param:  prec string  -   -  		auxiliary input file name
Param:  rayd string  -   -  		auxiliary output file name
Param:  reco string  -   -  		auxiliary input file name
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  recv string  -   -  		auxiliary input file name
Param:  seg int  -  3 		maximum number of segments of topography 
Param:  shape enum-bool  -  n 		regularization (default Tikhnov) 
Param:  shot string  -   -  		auxiliary input file name
Param:  stiter int  -  100 		number of inner CG iterations (for both Ticknov and Shaping) 
Param:  time string  -   -  		auxiliary output file name
Param:  tol float  -  1.e-6 		tolerance for shaping regularization 
Param:  topo string  -   -  		auxiliary input file name
Param:  velocity enum-bool  -  y 		if y, the input is velocity; n, slowness squared 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  weight enum-bool  -  n 		data weighting 
Param:  what string  -   -  		what to compute (default tomography) 

