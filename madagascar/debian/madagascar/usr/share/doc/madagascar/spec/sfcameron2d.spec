[sfcameron2d]
Cat:    RSF/user/kourkina
Desc:   Convert Dix velocity to interval velocity
DocCmd: sfcameron2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing fv data)
Port:   stdout rsf w req 	RSF standard output (containing fv2 data)
Port:   t0 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   x0 rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dz float  -   -  		
Param:  method string  -   -  		method (chebyshev,lax-friedrichs) 
Param:  nc int  -  100 		number of chebyshev coefficients 
Param:  neval int  -  20 		numvber of used chebyshev coefficients 
Param:  nz int  -   -  		

