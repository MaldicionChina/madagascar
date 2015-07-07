[sftti2dpseudoplrsep]
Cat:    RSF/user/chengjb
Desc:   None
DocCmd: sftti2dpseudoplrsep | cat
Port:   stdin  rsf r req 	RSF standard input (containing vp0 data)
Port:   stdout rsf w req 	RSF standard output (containing PseudoPurePx data)
Port:   PseudoPureP rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   PseudoPureSepPx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   PseudoPureSepPz rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt   -   -  		
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-6)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  ns   -   -  		
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)

