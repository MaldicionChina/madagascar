[sfsp]
Cat:    RSF/user/songxl
Desc:   2-D Pseudo-spectral wave extrapolation
DocCmd: sfsp | cat
Port:   stdin  rsf r req 	RSF standard input (containing source data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  ax float  -  5.0 		suppress HF parameter
Param:  az float  -  5.0 		suppress HF parameter
Param:  c float  -  0.01 		decaying parameter
Param:  dt float  -   -  		
Param:  factor float  -  5.0/6.0 		suppress HF parameter
Param:  isx int  -   -  		
Param:  isz int  -   -  		
Param:  nb int  -  30 		
Param:  nt int  -   -  		
Param:  opt enum-bool  -  y 		if y, determine optimal size for efficiency 

