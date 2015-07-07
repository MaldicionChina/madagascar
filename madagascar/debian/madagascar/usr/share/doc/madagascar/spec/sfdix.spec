[sfdix]
Cat:    RSF/user/fomels
Desc:   Convert RMS to interval velocity using LS and shaping regularization
DocCmd: sfdix | cat
Port:   stdin  rsf r req 	RSF standard input (containing vrms data)
Port:   stdout rsf w req 	RSF standard output (containing vint data)
Param:  niter int  -  100 		maximum number of iterations 
Param:  rect# string  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  vrmsout string  -   -  		optionally, output predicted vrms (auxiliary output file name)
Param:  weight string  -   -  		auxiliary input file name

