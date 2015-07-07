[sfkolmog]
Cat:    RSF/user/gee
Desc:   Kolmogoroff spectral factorization
DocCmd: sfkolmog | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  lag int  -  0 		lag for asymmetric part 
Param:  shift int  -  0 		time shift 
Param:  spec enum-bool  -  n 		if y, the input is spectrum squared; n, time-domain signal 

