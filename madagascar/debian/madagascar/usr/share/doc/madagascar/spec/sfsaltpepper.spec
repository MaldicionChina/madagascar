[sfsaltpepper]
Cat:    RSF/user/yliu
Desc:   Add salt and pepper noise to the data
DocCmd: sfsaltpepper | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  allpos enum-bool  -  n 		if y, assume positive noise 
Param:  den float  -  10. 		noise density (percent, default=10, Min=0, Max=100) 
Param:  inten float  -  0.1 		noise intensity (multiple peak value of data, default=0.1) 
Param:  noise enum-bool  -  n 		if y, output noise only 
Param:  rep enum-bool  -  n 		if y, replace data with noise 
Param:  seed int  -   -  		random seed 
LDesc:  (defaults to: time(NULL))

