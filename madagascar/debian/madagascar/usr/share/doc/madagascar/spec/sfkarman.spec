[sfkarman]
Cat:    RSF/user/browaeys
Desc:   Estimation of von Karman autocorrelation 1D spectrum
DocCmd: sfkarman | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  niter int  -  100 		number of iterations 
Param:  nliter int  -  1 		number of reweighting iterations 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  x0 float  -  1. 		initial squared length scale 

