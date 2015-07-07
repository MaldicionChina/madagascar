[sfphaserot]
Cat:    RSF/user/fomels
Desc:   Non-stationary phase rotation
DocCmd: sfphaserot | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   phase rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  a0 float  -  -360. 		first angle 
Param:  da float  -  1.0 		angle increment 
Param:  na int  -  721 		number of angles 
Param:  order int  -  100 		Hilbert transformer order 
Param:  ref float  -  1. 		Hilbert transformer reference (0.5 < ref <= 1) 

