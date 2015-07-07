[sffxdecon]
Cat:    RSF/user/chenyk
Desc:   Random noise attenuation using f-x deconvolution
DocCmd: sffxdecon | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  fmax float  -   -  		maximum frequency to process in Hz 
LDesc:  (defaults to: 1./(2*dt))
Param:  fmin float  -  1. 		minimum frequency to process in Hz 
Param:  lenf int  -  4 		number of traces for filter 
Param:  n2w int  -  10 		number of traces in window 
Param:  taper float  -  .1 		length of taper 
Param:  twlen float  -   -  		time window length 
LDesc:  (defaults to: (float)(n1-1)*dt)
Param:  verb enum-bool  -  n 		flag to get advisory messages 

