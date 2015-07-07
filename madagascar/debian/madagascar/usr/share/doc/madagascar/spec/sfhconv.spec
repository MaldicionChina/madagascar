[sfhconv]
Cat:    RSF/user/gee
Desc:   Convolution of two helix filters
DocCmd: sfhconv | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   other rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  lag string  -   -  		
Param:  one enum-bool  -  y 		include leading one 

