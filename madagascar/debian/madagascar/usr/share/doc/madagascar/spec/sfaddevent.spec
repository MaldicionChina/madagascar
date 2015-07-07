[sfaddevent]
Cat:    RSF/user/chen
Desc:   Add a dispersive event to a seismic profile
DocCmd: sfaddevent | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  a0 float  -  1.0 		event amplitude at t=a0ref (x=0) 
Param:  a0ref int  -  0 		reference point for a0: 0 - t0; 1 - a0 
Param:  event int  -  2 		0: linear; 1: parabolic; 2:hyperbolic 
Param:  f0 float  -   -  		reference frequency for velocity dispersion and amplitude attenuation 
LDesc:  (defaults to: w0)
Param:  nfft int  -   -  		fft length 
Param:  qa float  -   -  		Q factor for amplitude attenuation 
LDesc:  (defaults to: qv)
Param:  qv float  -  -1.0 		Q factor for velocity dispersion 
Param:  t0 float  -  0.3 		event travel time at x=0 
Param:  v0 float  -  1500.0 		event velocity at x=0, for reference frequency f0 
Param:  w0 float  -  35.0 		central frequency of Ricker wavelet or bandwidth of sinc wavelet 
Param:  wvtype int  -  0 		0: ricker; 1: sinc; x: not support 

