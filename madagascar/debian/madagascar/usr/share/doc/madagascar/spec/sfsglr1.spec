[sfsglr1]
Cat:    RSF/user/fangg
Desc:   1-D lowrank wave propagation on staggered grid
DocCmd: sfsglr1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fsrc data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   fft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ic rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   preinit rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   presrc rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   velinit rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   velsrc rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  cmplx enum-bool  -  n 		use complex FFT 
Param:  gdep float  -  0.0 		depth of geophone (meter)
Param:  inject enum-bool  -  y 		=y inject source; =n initial condition
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  slx float  -   -  		source location in x 
Param:  srcdecay enum-bool  -  y 		source decay
Param:  srcmms enum-bool  -  n 		use MMS source 
Param:  srcrange int  -  10 		source decay range
Param:  srctrunc float  -  100 		trunc source after srctrunc time (s)
Param:  verb enum-bool  -  n 		verbosity 

