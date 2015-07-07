[sfmig2]
Cat:    RSF/user/yliu
Desc:   2-D Prestack Kirchhoff time migration with antialiasing
DocCmd: sfmig2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (containing mig data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  angle float  -  90.0 		angle aperture 
Param:  antialias float  -  1.0 		antialiasing 
Param:  apt int  -   -  		integral aperture 
LDesc:  (defaults to: nx)
Param:  gather string  -   -  		auxiliary output file name
Param:  half enum-bool  -  y 		if y, the third axis is half-offset instead of full offset 
Param:  offset string  -   -  		auxiliary input file name
Param:  rho float  -   -  		Leaky integration constant 
LDesc:  (defaults to: 1.-1./nt)
Param:  verb enum-bool  -  y 		verbosity flag 

