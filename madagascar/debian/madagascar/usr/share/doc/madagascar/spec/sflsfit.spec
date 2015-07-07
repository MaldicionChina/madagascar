[sflsfit]
Cat:    RSF/user/fomels
Desc:   Simple least-squares regression
DocCmd: sflsfit | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   fit rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  coef string  -   -  		auxiliary output file name
Param:  dim int  -   -  		number of dimensions 
LDesc:  (defaults to: dim)
Param:  eps float  -   -  		regularization parameter 
LDesc:  (defaults to: 0.0f)
Param:  linear enum-bool  -  y 		if linear LS 
Param:  weight string  -   -  		auxiliary input file name

