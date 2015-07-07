[sfederiv2d]
Cat:    RSF/user/jyan
Desc:   
DocCmd: sfederiv2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fspk data)
Port:   ccc rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   xdel rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   zdel rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  domain string  -   -  		
Param:  order int  -  8 		order 
Param:  sig float  -  1.5 		sigma 
Param:  stat enum-bool  -  y 		stationary operator 
Param:  tapertype string  -   -  		
Param:  verb enum-bool  -  n 		verbosity flag 

