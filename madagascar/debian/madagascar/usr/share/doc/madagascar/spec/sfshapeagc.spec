[sfshapeagc]
Cat:    RSF/user/fomels
Desc:   Automatic gain control by shaping regularization
DocCmd: sfshapeagc | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eps float  -   -  		regularization 
LDesc:  (defaults to: 0.0f)
Param:  gain string  -   -  		output gain file (optional) (auxiliary output file name)
Param:  niter int  -  100 		number of iterations 
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (125,1,1,...))
Param:  verb enum-bool  -  n 		verbosity 

