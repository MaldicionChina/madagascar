[sffpocs3d]
Cat:    RSF/user/pyang
Desc:   3-D Two-step POCS interpolation using a general Lp-norm optimization
DocCmd: sffpocs3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fin data)
Port:   stdout rsf w req 	RSF standard output (containing Fout data)
Param:  mask string  -   -  		auxiliary input file name
Param:  mode string  -   -  		thresholding mode: 'hard', 'soft','pthresh','exp';
LDesc:  	'hard', hard thresholding;	'soft', soft thresholding; 
LDesc:  	'pthresh', generalized quasi-p; 'exp', exponential shrinkage 
Param:  niter int  -  100 		total number iterations 
Param:  p float  -  0.35 		norm=p, where 0<p<=1 
Param:  pclip float  -  99. 		starting data clip percentile (default is 99)
Param:  tol float  -  1.0e-6 		iteration tolerance 
Param:  verb enum-bool  -  n 		verbosity 

