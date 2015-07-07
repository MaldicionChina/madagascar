[sfmpipsp]
Cat:    RSF/user/poulsonj
Desc:   Parallel Sweeping Preconditioner (PSP) for solving 3D Helmholtz equations.

DocCmd: sfmpipsp | cat
Port:   solution rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   source rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  freq   -   -  		frequency in HZ
Param:  n1   -   -  		
LDesc:  (defaults to: origNx)
Param:  n2   -   -  		
LDesc:  (defaults to: origNy)
Param:  n3   -   -  		
LDesc:  (defaults to: origNz)
Param:  pmlSize   -   -  		number of grid points of PML
LDesc:  (defaults to: 5 )
Param:  sigma   -   -  		magnitude of PML stretching
LDesc:  (defaults to: 1.5 )

