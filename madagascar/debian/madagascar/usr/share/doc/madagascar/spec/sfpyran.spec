[sfpyran]
Cat:    RSF/user/chenyk
Desc:   Add random noise using python
DocCmd: sfpyran | cat
Port:   stdin  rsf r req 	RSF standard input (containing pi data)
Port:   stdout rsf w req 	RSF standard output (containing po data)
Param:  axis int  -  2 		
Param:  mean float  -  0 		noise mean (default=0)
Param:  range float  -  1 		noise range (default=1)
Param:  rep enum-bool  -  n 		if y, replace data with noise
Param:  seed int  -   -  		random seed (default=n2)
LDesc:  (defaults to: n2)
Param:  type string  -   -  		noise type, y: normal, n: uniform
LDesc:  (defaults to: y)
Param:  var float  -  1 		noise variance (default=1)

