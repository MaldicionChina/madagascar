[sfconvf]
Cat:    RSF/user/gee
Desc:   1-D convolution, adjoint is the filter
DocCmd: sfconvf | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   other rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  lag int  -  1 		lag for internal convolution 
Param:  nf int  -   -  		filter size 

