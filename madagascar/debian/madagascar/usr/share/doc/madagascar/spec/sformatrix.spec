[sformatrix]
Cat:    RSF/user/songxl
Desc:   Lowrank decomposition for 3-D orthorhombic wave propagation
DocCmd: sformatrix | cat
Port:   stdin  rsf r req 	RSF standard input (containing velz data)
Port:   stdout rsf w req 	RSF standard output (containing middle data)
Port:   app rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   fft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   real rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt   -   -  		time step
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  xx1   -   -  		x location
Param:  xx2   -   -  		x location
Param:  xx3   -   -  		x location

