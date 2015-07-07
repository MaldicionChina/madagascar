[sfkirmod_newton]
Cat:    RSF/user/zone
Desc:   Kirchhoff 2-D/2.5-D modeling in layered media with bending ray tracing
DocCmd: sfkirmod_newton | cat
Port:   stdin  rsf r req 	RSF standard input (containing modl data)
Port:   stdout rsf w req 	RSF standard output (containing data data)
Port:   aniso rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   curv rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  absoff enum-bool  -  n 		y - h0 is not in shot coordinate system 
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  cmp enum-bool  -  n 		compute CMP instead of shot gathers 
Param:  debug enum-bool  -  n 		debug flag 
Param:  dh float  -   -  		offset increment 
LDesc:  (defaults to: dx)
Param:  dip string  -   -  		reflector dip file 
Param:  ds float  -   -  		shot/midpoint increment 
LDesc:  (defaults to: dx)
Param:  dt float  -  0.004 		time sampling 
Param:  freq float  -   -  		peak frequency for Ricker wavelet 
LDesc:  (defaults to: 0.2/dt)
Param:  fwdxini enum-bool  -  n 		use the result of previous iteration to be the xinitial of the next one 
Param:  h0 float  -  0. 		first offset 
Param:  lin enum-bool  -  n 		if linear operator 
Param:  nh int  -   -  		number of offsets 
LDesc:  (defaults to: nx)
Param:  niter int  -  500 		The number of iterations
Param:  ns int  -   -  		number of shots (midpoints if cmp=y) 
LDesc:  (defaults to: nx)
Param:  nt int  -   -  		time samples 
Param:  order int  -  3 		Interpolation order
Param:  picks string  -   -  		auxiliary output file name
Param:  r0 float  -  1. 		normal reflectivity (if constant) 
Param:  refl string  -   -  		auxiliary input file name
Param:  rgrad string  -   -  		AVO gradient file (B/A) 
Param:  s0 float  -   -  		first shot (midpoint if cmp=y) 
LDesc:  (defaults to: x0)
Param:  slopes string  -   -  		auxiliary output file name
Param:  t0 float  -  0. 		time origin 
Param:  tol double  -   -  		Assign a default value for tolerance
LDesc:  (defaults to: 0.00001)
Param:  velocity float-list  -   -  		Assign velocity km/s [nc]
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  vstatus int  -   -  		Velocity status (0 for constant v,1 for gradient v, and 2 for vti)
Param:  xgradient float-list  -   -  		 [nc]
Param:  xref float-list  -   -  		Assign x-reference point [nc]
Param:  zgradient float-list  -   -  		 [nc]
Param:  zref float-list  -   -  		Assign z-reference point [nc]

