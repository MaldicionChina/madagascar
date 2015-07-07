[sffftwave1]
Cat:    RSF/user/fomels
Desc:   1-D FFT wave extrapolation
DocCmd: sffftwave1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   prop rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -   -  		
Param:  nsps enum-bool  -  n 		if using NSPS 
Param:  nt int  -   -  		
Param:  right string  -   -  		auxiliary input file name
Param:  step enum-bool  -  y 		if two-step propagation 
Param:  sub enum-bool  -  y 		if -1 is included in the matrix 

