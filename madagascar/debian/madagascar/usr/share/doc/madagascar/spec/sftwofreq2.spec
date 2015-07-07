[sftwofreq2]
Cat:    RSF/user/fomels
Desc:   2-D two spectral component estimation
DocCmd: sftwofreq2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eps float  -  1 		vertical smoothness 
Param:  lam float  -  1 		horizontal smoothness 
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  5 		number of iterations 
Param:  p0 float  -  1. 		initial first component 
Param:  p1 float  -  -1. 		initial second component 
Param:  q0 float  -  1. 		initial first component 
Param:  q1 float  -  1. 		initial second component 
Param:  verb enum-bool  -  n 		verbosity flag 

