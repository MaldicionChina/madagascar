[sftimefreq]
Cat:    RSF/user/fomels
Desc:   Time-frequency analysis using local attributes
DocCmd: sftimefreq | cat
Port:   stdin  rsf r req 	RSF standard input (containing time data)
Port:   stdout rsf w req 	RSF standard output (containing timefreq data)
Param:  dw float  -   -  		f	requency step 
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  100 		number of inversion iterations 
Param:  nw int  -   -  		number of frequencies 
Param:  phase enum-bool  -  n 		output phase instead of amplitude 
Param:  rect int  -  10 		smoothing radius 
Param:  w0 float  -  0. 		first frequency 

