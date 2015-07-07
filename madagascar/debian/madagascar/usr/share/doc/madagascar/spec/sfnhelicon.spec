[sfnhelicon]
Cat:    RSF/user/gee
Desc:   Non-stationary helix convolution and deconvolution
DocCmd: sfnhelicon | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		if y, do adjoint operation 
Param:  div enum-bool  -  n 		if y, do inverse operation (deconvolution) 
Param:  lag string  -   -  		
Param:  nh string  -   -  		auxiliary input file name
Param:  pch string  -   -  		auxiliary input file name

