[sfsglr2]
Cat:    RSF/user/fangg
Desc:   Simple 2-D wave propagation on staggered grid
DocCmd: sfsglr2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fsrc data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   fft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  cmplx enum-bool  -  n 		use complex FFT 
Param:  gdep float  -  -1.0 		recorder depth on grid
Param:  gp int  -  0 		recorder depth on index
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  slx float  -  -1.0 		source location x 
Param:  slz float  -  -1.0 		source location z 
Param:  spx int  -  -1 		source location x (index)
Param:  spz int  -  -1 		source location z (index)
Param:  srcdecay enum-bool  -  n 		source decay
Param:  srcrange int  -  10 		source decay range
Param:  srctrunc float  -  100 		trunc source after srctrunc time (s)
Param:  verb enum-bool  -  n 		verbosity 

