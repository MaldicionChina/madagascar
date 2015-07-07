[sftwodip2]
Cat:    RSF/user/pwd
Desc:   2-D two dip estimation by plane wave destruction
DocCmd: sftwodip2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  both enum-bool  -  y 		if y, estimate both dips 
Param:  dip1 string  -   -  		auxiliary input file name
Param:  dip2 string  -   -  		auxiliary input file name
Param:  eps float  -  1 		vertical smoothness 
Param:  gauss enum-bool  -  n 		if y, use exact Gaussian for smoothing 
Param:  lam float  -  1 		horizontal smoothness 
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  5 		number of iterations 
Param:  nj1 int  -  1 		antialiasing for first dip 
Param:  nj2 int  -  1 		antialiasing for second dip 
Param:  order int  -  1 		accuracy order 
Param:  p0 float  -  1. 		initial first dip 
Param:  q0 float  -  0. 		initial second dip 
Param:  sign enum-bool  -  n 		if y, keep dip sign constant 
Param:  verb enum-bool  -  n 		verbosity flag 

