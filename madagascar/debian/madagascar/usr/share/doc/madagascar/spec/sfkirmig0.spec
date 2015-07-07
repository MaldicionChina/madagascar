[sfkirmig0]
Cat:    RSF/user/llisiw
Desc:   2-D Post-stack Kirchhoff depth migration
DocCmd: sfkirmig0 | cat
Port:   stdin  rsf r req 	RSF standard input (containing dat data)
Port:   stdout rsf w req 	RSF standard output (containing mig data)
Port:   deriv rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   table rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  y 		y for migration, n for modeling 
Param:  antialias float  -  1.0 		antialiasing 
Param:  aperture float  -  90. 		migration aperture (in degree) 
Param:  ds float  -   -  		midpoint sampling 
Param:  dt float  -   -  		time sampling 
Param:  ns int  -   -  		midpoint samples 
Param:  nt int  -   -  		time samples 
Param:  s0 float  -  0.0 		midpoint origin 
Param:  t0 float  -  0.0 		time origin 
Param:  type string  -   -  		type of interpolation (default Hermit) 

