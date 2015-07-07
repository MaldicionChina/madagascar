[sflrmatrix]
Cat:    RSF/user/lexing
Desc:   Lowrank matrix decomposition
DocCmd: sflrmatrix | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   name rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  outputs   -   -  		number of outputs (2 or 3)
LDesc:  (defaults to: 2)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)

