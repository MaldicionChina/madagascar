[sfdecon]
Cat:    RSF/user/gee
Desc:   Deconvolution (N-dimensional)
DocCmd: sfdecon | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  lag string  -   -  		
Param:  predictive enum-bool  -  n 		if y, do predictive deconvolution 
Param:  rect1 int  -  0 		smoothing in the first axis 

