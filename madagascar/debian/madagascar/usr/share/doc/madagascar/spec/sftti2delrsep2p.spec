[sftti2delrsep2p]
Cat:    RSF/user/chengjb
Desc:   None
DocCmd: sftti2delrsep2p | cat
Port:   stdin  rsf r req 	RSF standard input (containing vp0 data)
Port:   stdout rsf w req 	RSF standard output (containing Elasticx data)
Port:   ElasticSepP rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   ElasticSepSV rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Errpolxp1 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Errpolxp2 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Errpolzp1 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Errpolzp2 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Polxp1 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Polxp2 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Polzp1 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Polzp2 rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt   -   -  		
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-6)
Param:  ireconstruct   -   -  		
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  ns   -   -  		
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  xrec1   -   -  		
Param:  xrec2   -   -  		
Param:  zrec1   -   -  		
Param:  zrec2   -   -  		

