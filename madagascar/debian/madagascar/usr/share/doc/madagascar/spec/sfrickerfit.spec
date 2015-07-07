[sfrickerfit]
Cat:    RSF/user/tsai
Desc:   Model wavelet spectrum by fitting spectral components of ricker wavelet
DocCmd: sfrickerfit | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   ma1 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   ma2 rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  m float-list  -   -  		 [n]
Param:  n int  -   -  		
Param:  niter int  -  100 		
Param:  verb enum-bool  -  n 		

