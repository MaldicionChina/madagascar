[sfdip2]
Cat:    RSF/user/pwd
Desc:   2-D dip estimation by plane wave destruction
DocCmd: sfdip2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eps float  -   -  		regularization 
LDesc:  (defaults to: 0.0f)
Param:  idip string  -   -  		initial in-line dip (auxiliary input file name)
Param:  liter int  -  20 		number of linear iterations 
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  5 		number of iterations 
Param:  nj1 int  -  1 		antialiasing 
Param:  order int  -  1 		accuracy order 
Param:  p0 float  -  0. 		initial dip 
Param:  pmax float  -   -  		maximum dip 
LDesc:  (defaults to: +FLT_MAX)
Param:  pmin float  -   -  		minimum dip 
LDesc:  (defaults to: -FLT_MAX)
Param:  rect1 int  -  1 		dip smoothness on 1st axis 
Param:  rect2 int  -  1 		dip smoothness on 2nd axis 
Param:  verb enum-bool  -  n 		verbosity flag 

