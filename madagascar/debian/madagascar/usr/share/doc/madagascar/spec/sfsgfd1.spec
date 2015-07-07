[sfsgfd1]
Cat:    RSF/user/fangg
Desc:   1-D staggered Grid Finite-difference wave extrapolation
DocCmd: sfsgfd1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fsrc data)
Port:   stdout rsf w req 	RSF standard output (containing Fwf data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ic rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   preinit rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   presrc rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   velinit rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   velsrc rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  decay int  -   -  		Flag of decay boundary condtion: 1 = use ; 0 = not use 
LDesc:  (defaults to: DECAY_FLAG)
Param:  decaybegin int  -   -  		Begin time of using decay boundary condition 
LDesc:  (defaults to: DECAY_BEGIN)
Param:  freesurface enum-bool  -  n 		free surface
Param:  gdep float  -  0 		recorder depth 
Param:  inject enum-bool  -  y 		inject = y use inject source; inject =n use initial condition
Param:  pmld0 int  -   -  		PML parameter 
LDesc:  (defaults to: PMLD0)
Param:  pmlsize int  -   -  		size of PML layer 
LDesc:  (defaults to: PMLOUT)
Param:  size int  -  4 		FD half order
Param:  slx float  -   -  		source location in x 
Param:  snapinter int  -  1 		snap interval 
Param:  srcdecay enum-bool  -  n 		source decay y=use
Param:  srcmms enum-bool  -  n 		source type: if y, use point source 
Param:  srctrunc float  -  1000 		source trunc time (s)
Param:  verb enum-bool  -  n 		verbosity

