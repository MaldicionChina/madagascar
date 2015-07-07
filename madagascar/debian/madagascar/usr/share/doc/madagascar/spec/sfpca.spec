[sfpca]
Cat:    RSF/user/chen
Desc:   KL transform
DocCmd: sfpca | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eta float  -  0.9 		energy ratio for signal subspace [ 0 eta < 1 ]
Param:  nc int  -   -  		number of components [ 0 < nc < n1 ] 
LDesc:  (defaults to: n1)
Param:  verb enum-bool  -  y 		verbosity 

