[sfsglfdcp1]
Cat:    RSF/user/fangg
Desc:   Relative error of phase velocity of 16-th order 1D SG Lowrank FD and 1D FD coefficient
DocCmd: sfsglfdcp1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing velf data)
Port:   stdout rsf w req 	RSF standard output (containing outm data)
Port:   Mfd rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Mlr rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt   -   -  		time step
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  size   -   -  		stencil length
LDesc:  (defaults to: 16)

