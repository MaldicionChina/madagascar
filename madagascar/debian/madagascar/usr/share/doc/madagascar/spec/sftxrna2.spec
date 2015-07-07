[sftxrna2]
Cat:    RSF/user/yliu
Desc:   2D space-noncausal t-x nonstationary regularized autoregression
DocCmd: sftxrna2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing mat data)
Port:   stdout rsf w req 	RSF standard output (containing pre data)
Param:  a int-list  -   -  		 [mdim]
Param:  niter int  -  20 		number of iterations 
Param:  verb enum-bool  -  n 		verbosity flag 

