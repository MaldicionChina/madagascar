[sflfdanc2_25]
Cat:    RSF/user/songxl
Desc:   2D high-order TTI Lowrank FD coefficient
DocCmd: sflfdanc2_25 | cat
Port:   stdin  rsf r req 	RSF standard input (containing velz data)
Port:   stdout rsf w req 	RSF standard output (containing outm data)
Param:  de   -   -  		stencil length
LDesc:  (defaults to: 1)
Param:  dt   -   -  		time step
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-6)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 50)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  size   -   -  		stencil length
LDesc:  (defaults to: 17)

