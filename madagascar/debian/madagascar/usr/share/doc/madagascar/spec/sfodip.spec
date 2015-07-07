[sfodip]
Cat:    RSF/user/chen
Desc:   omnidirectional dip estimation
DocCmd: sfodip | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dip0 float  -  0.0 		starting dip 
Param:  eta float  -  0.5 		steps for iteration 
Param:  interp string  -   -  		interpolation method: maxflat lagrange bspline 
Param:  liter int  -  20 		number of linear iterations 
Param:  m int  -  1 		b[-m, ... ,n] 
Param:  n int  -  1 		b[-m, ... ,n] 
Param:  niter int  -  5 		number of iterations 
Param:  radius float  -  1.0 		interpolating radius for opwd 
Param:  rect1 int  -  0 		dip smoothness on 1st axis 
Param:  rect2 int  -  0 		dip smoothness on 2nd axis 
Param:  slope enum-bool  -  n 		slope (y) or dip (n) estimation 
Param:  verb enum-bool  -  n 		verbosity flag 

