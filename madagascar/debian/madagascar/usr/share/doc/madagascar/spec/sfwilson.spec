[sfwilson]
Cat:    RSF/user/gee
Desc:   Wilson-Burg spectral factorization
DocCmd: sfwilson | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  a0 float  -  1. 		
Param:  eps float  -  1.e-6 		truncation tolerance 
Param:  filtin string  -   -  		
Param:  lag string  -   -  		optional input file with filter lags (auxiliary input file name)
Param:  lagin string  -   -  		optional input file with output filter lags 
Param:  lagout string  -   -  		auxiliary output file name
Param:  maxlag int  -   -  		maximum lag 
Param:  n1 int  -   -  		output filter length 
LDesc:  (defaults to: maxlag)
Param:  niter int  -  20 		number of iterations 
Param:  stable enum-bool  -  n 		stability flag 
Param:  verb enum-bool  -  y 		verbosity flag 

