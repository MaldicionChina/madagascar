[sfcltft]
Cat:    RSF/user/fomels
Desc:   Complex local time-frequency transform
DocCmd: sfcltft | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  basis string  -   -  		auxiliary output file name
Param:  dip enum-bool  -  n 		if y, do dip decomposition 
Param:  dp float  -   -  		slope step 
Param:  dw float  -   -  		frequency step 
LDesc:  (defaults to: 1./(nw*d1))
Param:  inv enum-bool  -  n 		if y, do inverse transform 
Param:  niter int  -  100 		number of inversion iterations 
Param:  np int  -   -  		number of slopes 
Param:  nw int  -   -  		number of frequencies 
LDesc:  (defaults to: kiss_fft_next_fast_size(n1))
Param:  p0 float  -   -  		first slope 
Param:  rect int  -  10 		smoothing radius (in time, samples) 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  w0 float  -   -  		first frequency 
LDesc:  (defaults to: -0.5/d1)

