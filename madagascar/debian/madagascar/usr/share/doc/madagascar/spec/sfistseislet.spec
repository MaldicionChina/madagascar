[sfistseislet]
Cat:    RSF/user/pyang
Desc:   Analysis-based IST interpolation using seislet (2d validation)
DocCmd: sfistseislet | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fin data)
Port:   stdout rsf w req 	RSF standard output (containing Fout data)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization 
Param:  mask string  -   -  		auxiliary input file name
Param:  mode string  -   -  		thresholding mode: 'hard', 'soft','pthresh','exp';
LDesc:  	'hard', hard thresholding;	'soft', soft thresholding; 
LDesc:  	'pthresh', generalized quasi-p; 'exp', exponential shrinkage 
Param:  niter int  -  10 		total number iterations 
Param:  order int  -  1 		accuracy order for seislet transform
Param:  p float  -  0.35 		norm=p, where 0<p<=1 
Param:  pclip float  -  99 		starting data clip percentile (default is 99)
Param:  pscale float  -  25 		percentile of small scale to be preserved (default is 25)
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is linear  
Param:  verb enum-bool  -  n 		verbosity 

