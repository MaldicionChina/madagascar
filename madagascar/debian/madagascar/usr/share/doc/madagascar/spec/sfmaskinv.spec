[sfmaskinv]
Cat:    RSF/user/gee
Desc:   Missing data interpolation using one or two prediction-error filters
DocCmd: sfmaskinv | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   mask rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  a int-list  -   -  		first filter dimensions  [dim]
Param:  b int-list  -   -  		second filter dimensions  [dim]
Param:  center int-list  -   -  		filter center  [dim]
Param:  niter int  -  80 		number of iterations 

