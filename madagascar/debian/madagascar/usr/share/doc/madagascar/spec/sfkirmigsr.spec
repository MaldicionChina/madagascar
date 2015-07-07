[sfkirmigsr]
Cat:    RSF/user/llisiw
Desc:   2-D Prestack Kirchhoff depth migration
DocCmd: sfkirmigsr | cat
Port:   stdin  rsf r req 	RSF standard input (containing dat data)
Port:   stdout rsf w req 	RSF standard output (containing mig data)
Port:   rderiv rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rtable rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sderiv rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   stable rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  y 		y for migration, n for modeling 
Param:  antialias float  -  1.0 		antialiasing 
Param:  aperture float  -  90. 		migration aperture (in degree) 
Param:  cig enum-bool  -  n 		y - output common offset gathers 
Param:  cmp enum-bool  -  y 		y for CMP gather, n for shot gather 
Param:  dh float  -   -  		offset sampling 
Param:  ds float  -   -  		shot sampling 
Param:  dt float  -   -  		time sampling 
Param:  h0 float  -  0.0 		offset origin 
Param:  nh int  -  1 		offset samples 
Param:  ns int  -  1 		shot samples 
Param:  nt int  -   -  		time samples 
Param:  s0 float  -  0.0 		shot origin 
Param:  t0 float  -  0.0 		time origin 
Param:  tau float  -  0. 		static time-shift (in second) 
Param:  type string  -   -  		type of interpolation (default Hermit) 

