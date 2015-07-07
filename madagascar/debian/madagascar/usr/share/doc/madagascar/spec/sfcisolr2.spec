[sfcisolr2]
Cat:    RSF/user/jsun
Desc:   Complex lowrank decomposition for 2-D isotropic wave propagation
DocCmd: sfcisolr2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (containing right data)
Port:   fft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   left rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt   -   -  		time step
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  lap   -   -  		
LDesc:  (defaults to: false)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  os   -   -  		
LDesc:  (defaults to: true)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  sub   -   -  		for twostep, default true
LDesc:  (defaults to: true)

