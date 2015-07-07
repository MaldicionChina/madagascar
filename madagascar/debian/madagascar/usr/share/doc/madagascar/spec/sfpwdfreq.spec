[sfpwdfreq]
Cat:    RSF/user/chen
Desc:   frequency response of PWD operator
DocCmd: sfpwdfreq | cat
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  d3 float  -  30 		dip angle increment 
Param:  iir enum-bool  -  n 		y: iir; n: fir 
Param:  interp string  -   -  		interpolation method: maxflat lagrange bspline 
Param:  n1 int  -  50 		samples in frequency domain between (0:f_c] 
Param:  n3 int  -  1 		number dip angle 
Param:  o3 float  -  20 		first dip angle 
Param:  opwd enum-bool  -  y 		y: circle interpolating pwd; n: line interpolating pwd 
Param:  order int  -  1 		order of PWD 
Param:  radius float  -  1.0 		radius for circle interpolating pwd 

