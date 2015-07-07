[sfpocs]
Cat:    RSF/user/pyang
Desc:   n-D POCS interpolation using a hard thresholding
DocCmd: sfpocs | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  mask string  -   -  		auxiliary input file name
Param:  n# int  -   -  		size of #-th axis 
Param:  niter int  -  100 		total number iterations 
Param:  pclip float  -  10. 		starting data clip percentile (default is 99)
Param:  verb enum-bool  -  n 		verbosity 

