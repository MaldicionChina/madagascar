[sfhelicon]
Cat:    RSF/user/gee
Desc:   Multidimensional convolution and deconvolution by helix transform
DocCmd: sfhelicon | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		if y, do adjoint operation 
Param:  div enum-bool  -  n 		if y, do inverse operation (deconvolution) 
Param:  lag string  -   -  		file with filter lags
Param:  n int-list  -   -  		 [dim]

