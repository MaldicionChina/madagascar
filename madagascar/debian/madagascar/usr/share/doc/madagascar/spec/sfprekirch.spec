[sfprekirch]
Cat:    RSF/user/chenyk
Desc:   2-D Prestack Kirchhoff time migration with antialiasing
DocCmd: sfprekirch | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (containing mig data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  antialias float  -  1.0 		antialiasing 
Param:  dz float  -   -  		
LDesc:  (defaults to: dt)
Param:  nz int  -   -  		
LDesc:  (defaults to: nt)
Param:  z0 float  -   -  		
LDesc:  (defaults to: t0)

