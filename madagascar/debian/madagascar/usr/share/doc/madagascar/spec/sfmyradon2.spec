[sfmyradon2]
Cat:    RSF/user/pyang
Desc:   Linear/parabolic radon transform frequency domain implementation
DocCmd: sfmyradon2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  y 		if y, perform adjoint operation 
Param:  dp float  -   -  		p sampling (if adj=y) 
Param:  dx float  -   -  		sampling interval in x 
Param:  eps float  -  0.01 		regularization parameter 
Param:  inv enum-bool  -  n 		if y, perform inverse operation 
Param:  invmode string  -   -  		inverse method: 'ls' if least-squares; 'toeplitz' if use FFT 
Param:  niter int  -  100 		number of CGLS iterations 
Param:  np int  -   -  		number of p values (if adj=y) 
Param:  nx int  -   -  		number of offsets (if adj=n) 
Param:  ox float  -   -  		x origin 
Param:  p0 float  -   -  		p origin (if adj=y) 
Param:  parab enum-bool  -  n 		if y, parabolic Radon transform 
Param:  x0 float  -  1. 		reference offset 

