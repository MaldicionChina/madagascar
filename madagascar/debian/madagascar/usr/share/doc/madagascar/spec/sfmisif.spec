[sfmisif]
Cat:    RSF/user/gee
Desc:   Find MISSing Input values and Filter in 1-D
DocCmd: sfmisif | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filtout rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  lag int  -  1 		filter lag 
Param:  na int  -  3 		filter size 
Param:  nmiss int  -   -  		number of iterations 
LDesc:  (defaults to: n1)

