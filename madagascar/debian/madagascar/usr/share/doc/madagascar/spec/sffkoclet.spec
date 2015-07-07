[sffkoclet]
Cat:    RSF/user/yliu
Desc:   1-D seislet transform using omega-wavenumber offset continuation
DocCmd: sffkoclet | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		if y, do adjoint transform 
Param:  dwt enum-bool  -  n 		if y, do wavelet transform 
Param:  eps float  -  0.01 		regularization 
Param:  inv enum-bool  -  n 		if y, do inverse transform 
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is biorthogonal  
Param:  verb enum-bool  -  y 		verbosity flag 

