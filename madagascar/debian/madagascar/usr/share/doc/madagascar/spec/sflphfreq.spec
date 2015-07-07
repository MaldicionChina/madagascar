[sflphfreq]
Cat:    RSF/user/chen
Desc:   frequency response of linear phase approximators
DocCmd: sflphfreq | cat
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  d2 float  -  0.3 		phase shift increment 
Param:  iir enum-bool  -  y 		y:iir,  n:fir 
Param:  interp string  -   -  		interpolation method: maxflat lagrange bspline 
Param:  m int  -  1 		b[-m, ... ,n] 
Param:  n int  -  1 		b[-m, ... ,n] 
Param:  n1 int  -  50 		samples in frequency domain between (0:f_c] 
Param:  n2 int  -  1 		number of phase shift 
Param:  o2 float  -  0.1 		first phase shift 

