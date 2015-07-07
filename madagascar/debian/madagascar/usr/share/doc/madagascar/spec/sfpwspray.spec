[sfpwspray]
Cat:    RSF/user/pwd
Desc:   Plane-wave spray
DocCmd: sfpwspray | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization 
Param:  ns int  -   -  		spray radius 
Param:  order int  -  1 		accuracy order 
Param:  rect int  -  2 		radius for predictive coherence (reduce=coherence) 
Param:  reduce string  -   -  		reduction method (none,stack,median,triangle,gaussian,predict,coherence) 
Param:  verb enum-bool  -  n 		verbosity 

