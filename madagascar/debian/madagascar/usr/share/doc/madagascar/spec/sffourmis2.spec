[sffourmis2]
Cat:    RSF/user/yliu
Desc:   Missing data interpolation in 2-D using Fourier transform and compressive sensing
DocCmd: sffourmis2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  cut enum-bool  -  n 		cutting verbosity flag, the default is soft-thresholding 
Param:  error enum-bool  -  n 		error verbosity flag 
Param:  f0 float  -  0. 		initial cutting frequency 
Param:  k0 float  -  0. 		initial cutting wavenumber 
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  20 		number of iterations 
Param:  oper string  -   -  		[shaping,pocs,bregman] method, the default is shaping 
Param:  orderf float  -  1. 		Curve order for frequency window, default is linear 
Param:  ordert float  -  1. 		Curve order for thresholding parameter, default is linear 
Param:  orderw float  -  1. 		Curve order for frequency window, default is linear 
Param:  parf float  -  0. 		Ajustable parameter for frequency window, default is fixed window 
Param:  parw float  -  0. 		Ajustable parameter for wavenumber window, default is fixed window 
Param:  perc float  -  99. 		percentage for soft-thresholding 
Param:  res string  -   -  		auxiliary output file name
Param:  verb enum-bool  -  n 		verbosity flag 

