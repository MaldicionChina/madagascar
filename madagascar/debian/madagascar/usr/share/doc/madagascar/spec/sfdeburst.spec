[sfdeburst]
Cat:    RSF/user/gee
Desc:   Remove bursty noise by IRLS
DocCmd: sfdeburst | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eps float  -  1. 		regularization parameter 
Param:  niter int  -  10 		number of iterations 
Param:  norm string  -   -  		norm to use in IRLS (cauchy,l1) 

