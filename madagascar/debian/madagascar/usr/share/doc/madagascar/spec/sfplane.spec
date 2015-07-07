[sfplane]
Cat:    RSF/user/fomels
Desc:   Generating plane waves with steering filters
DocCmd: sfplane | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  a1 int  -  2 		filter length 
Param:  b1 int  -  1 		denominator length 
Param:  hyp enum-bool  -  n 		generate hyperbolas 
Param:  lag string  -   -  		
Param:  p float  -  0.7 		plane wave slope 

