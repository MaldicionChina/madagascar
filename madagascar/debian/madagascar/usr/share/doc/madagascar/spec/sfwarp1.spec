[sfwarp1]
Cat:    RSF/user/fomels
Desc:   Multicomponent data registration by 1-D warping
DocCmd: sfwarp1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing warped data)
Port:   amplout rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   other rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   warpout rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  accuracy int  -   -  		interpolation accuracy 
Param:  niter int  -  100 		maximum number of linear iterations 
Param:  nliter int  -  10 		number of non-linear iterations 
Param:  noamp enum-bool  -  n 		if y, don't correct amplitudes 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  warpin string  -   -  		optional initial warp file (auxiliary input file name)

