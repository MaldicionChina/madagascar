[sfldip]
Cat:    RSF/user/chen
Desc:   dip estimation by line interpolating pwd
DocCmd: sfldip | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eta float  -  1.0 		steps for iteration 
Param:  idip string  -   -  		auxiliary input file name
Param:  interp string  -   -  		interpolation method: maxflat lagrange bspline 
Param:  liter int  -  20 		number of linear iterations 
Param:  m int  -  1 		b[-m, ... ,n] 
Param:  n int  -  1 		b[-m, ... ,n] 
Param:  niter int  -  5 		number of iterations 
Param:  rect1 int  -  0 		dip smoothness on 1st axis 
Param:  rect2 int  -  0 		dip smoothness on 2nd axis 
Param:  verb enum-bool  -  n 		verbosity flag 

