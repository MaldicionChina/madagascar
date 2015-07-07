[sfinvbin]
Cat:    RSF/user/gee
Desc:   Data interpolation in 2-D slices using helix preconditioning
DocCmd: sfinvbin | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   pch rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  der enum-bool  -  n 		if y, apply derivative filter on the residual 
Param:  dx float  -   -  		bin size in x 
Param:  dy float  -   -  		bin size in y 
Param:  eps float  -  0.01 		regularization parameter 
Param:  head string  -   -  		
Param:  interp int  -  2 		interpolation length 
Param:  lag string  -   -  		
Param:  n int-list  -   -  		 [2]
Param:  nh string  -   -  		
Param:  niter int  -  20 		number of iterations 
Param:  nx int  -   -  		Number of bins in x 
LDesc:  (defaults to: (int) (xmax - xmin + 1.))
Param:  ny int  -   -  		Number of bins in y 
LDesc:  (defaults to: (int) (ymax - ymin + 1.))
Param:  stat enum-bool  -  y 		stationary or nonstationary filter 
Param:  x0 float  -   -  		
LDesc:  (defaults to: xmin)
Param:  xkey int  -   -  		x key number 
Param:  xmax float  -   -  		
Param:  xmin float  -   -  		
Param:  y0 float  -   -  		grid origin 
LDesc:  (defaults to: ymin)
Param:  ykey int  -   -  		y key number 
Param:  ymax float  -   -  		
Param:  ymin float  -   -  		Grid dimensions 

