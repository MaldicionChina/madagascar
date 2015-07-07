[sfthreshold2]
Cat:    RSF/user/yliu
Desc:   2-D Soft thresholding
DocCmd: sfthreshold2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  pclip float  -  99. 		
Param:  thr string  -   -  		auxiliary input file name
Param:  verb enum-bool  -  n 		verbosity flag 

