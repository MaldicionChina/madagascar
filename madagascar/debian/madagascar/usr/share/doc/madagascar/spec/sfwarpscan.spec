[sfwarpscan]
Cat:    RSF/user/fomels
Desc:   Multicomponent data registration analysis
DocCmd: sfwarpscan | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing warped data)
Port:   other rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  accuracy int  -   -  		interpolation accuracy 
Param:  dg float  -   -  		gamma sampling 
LDesc:  (defaults to: g0)
Param:  g0 float  -   -  		gamma origin 
Param:  ng int  -  1 		number of gamma values 
Param:  niter int  -  10 		number of iterations 
Param:  rect1 int  -  1 		vertical smoothing 
Param:  rect2 int  -  1 		gamma smoothing 
Param:  rect3 int  -  1 		in-line smoothing 
Param:  rect4 int  -  1 		cross-line smoothing 
Param:  verb enum-bool  -  y 		verbosity flag 

