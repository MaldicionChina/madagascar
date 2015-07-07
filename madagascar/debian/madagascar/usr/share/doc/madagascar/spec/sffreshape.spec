[sffreshape]
Cat:    RSF/user/yliu
Desc:   Nonstationary spectral balancing in frequency domain
DocCmd: sffreshape | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   ma rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ma2 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   out2 rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dim int  -  1 		data dimensionality 
Param:  in2 string  -   -  		optional second input file (auxiliary input file name)

