[sfbspvel2]
Cat:    RSF/user/cram
Desc:   B-spline coefficients for a 2-D (an)isotropic velocity model
DocCmd: sfbspvel2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing velz data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eta string  -   -  		Anellipticity (auxiliary input file name)
Param:  theta string  -   -  		Tilt angle (auxiliary input file name)
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  vx string  -   -  		Horizontal velocity (auxiliary input file name)

