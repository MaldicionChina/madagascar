[sfpwspray3]
Cat:    RSF/user/pwd
Desc:   Plane-wave spray in 3-D
DocCmd: sfpwspray3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization 
Param:  ns2 int  -   -  		
Param:  ns3 int  -   -  		spray radius 
Param:  order int  -  1 		accuracy order 
Param:  verb enum-bool  -  n 		verbosity 

