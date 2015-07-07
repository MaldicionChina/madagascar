[sfltft]
Cat:    RSF/user/yliu
Desc:   Local time-frequency transform (LTFT)
DocCmd: sfltft | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  alpha float  -  0. 		frequency adaptivity 
Param:  basis string  -   -  		auxiliary output file name
Param:  dw float  -   -  		frequency step 
Param:  inv enum-bool  -  n 		if y, do inverse transform 
Param:  mask string  -   -  		data weight (auxiliary input file name)
Param:  niter int  -  100 		number of inversion iterations 
Param:  nw int  -   -  		number of frequencies 
Param:  rect int  -  10 		smoothing radius (in time, samples) 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  w0 float  -  0. 		first frequency 
Param:  weight string  -   -  		model weight (auxiliary input file name)

