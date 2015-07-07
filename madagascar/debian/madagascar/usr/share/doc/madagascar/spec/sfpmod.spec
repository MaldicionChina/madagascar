[sfpmod]
Cat:    RSF/user/rickettj
Desc:   Random plane wave modeling
DocCmd: sfpmod | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  ampmax float  -  1. 		
Param:  gauss int  -  0 		
Param:  h1 float  -  200. 		
Param:  h2 float  -  150. 		
Param:  np int  -  1 		
Param:  phi float  -  0.1 		
Param:  pmax float  -  0.000332 		
Param:  rc1 float  -  0.2 		
Param:  rc2 float  -  0.2 		
Param:  seed int  -   -  		random seed 
LDesc:  (defaults to: time(NULL))
Param:  type int  -  1 		1 single plane layer
LDesc:         2 two plane layers
LDesc:         3 point diffractor 
Param:  v1 float  -  2000. 		
Param:  v2 float  -  3000. 		
Param:  xloc float  -  200. 		

