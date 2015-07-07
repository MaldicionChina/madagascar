[sfdip]
Cat:    RSF/user/pwd
Desc:   3-D dip estimation by plane wave destruction
DocCmd: sfdip | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  both enum-bool  -  n 		if y, compute both left and right predictions 
Param:  eps float  -   -  		regularization 
LDesc:  (defaults to: 0.0f)
Param:  idip string  -   -  		initial in-line dip (auxiliary input file name)
Param:  liter int  -  20 		number of linear iterations 
Param:  mask string  -   -  		auxiliary input file name
Param:  n4 int  -  2 		what to compute in 3-D. 0: in-line, 1: cross-line, 2: both 
Param:  niter int  -  5 		number of iterations 
Param:  nj1 int  -  1 		in-line antialiasing 
Param:  nj2 int  -  1 		cross-line antialiasing 
Param:  order int  -  1 		accuracy order 
Param:  p0 float  -  0. 		initial in-line dip 
Param:  pmax float  -   -  		maximum inline dip 
LDesc:  (defaults to: +FLT_MAX)
Param:  pmin float  -   -  		minimum inline dip 
LDesc:  (defaults to: -FLT_MAX)
Param:  q0 float  -  0. 		initial cross-line dip 
Param:  qmax float  -   -  		maximum cross-line dip 
LDesc:  (defaults to: +FLT_MAX)
Param:  qmin float  -   -  		minimum cross-line dip 
LDesc:  (defaults to: -FLT_MAX)
Param:  rect1 int  -  1 		dip smoothness on 1st axis 
Param:  rect2 int  -  1 		dip smoothness on 2nd axis 
Param:  rect3 int  -  1 		dip smoothness on 3rd axuis 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  xdip string  -   -  		initial cross-line dip (auxiliary input file name)

