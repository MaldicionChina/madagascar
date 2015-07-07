[sfclpf]
Cat:    RSF/user/fomels
Desc:   Local prediction filter for complex numbers (n-dimensional)
DocCmd: sfclpf | cat
Port:   stdin  rsf r req 	RSF standard input (containing dat data)
Port:   stdout rsf w req 	RSF standard output (containing flt data)
Port:   match rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  niter int  -  100 		number of iterations 
Param:  pred string  -   -  		auxiliary output file name
Param:  verb enum-bool  -  y 		verbosity flag 

