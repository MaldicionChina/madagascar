[sfconvolve2]
Cat:    RSF/user/jyan
Desc:   2D convolution with arbitrary filter
DocCmd: sfconvolve2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fx data)
Port:   stdout rsf w req 	RSF standard output (containing Fy data)
Port:   flt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  stat enum-bool  -  y 		stationary operator 
Param:  verb enum-bool  -  n 		verbosity flag 

