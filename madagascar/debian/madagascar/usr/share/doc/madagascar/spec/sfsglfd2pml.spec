[sfsglfd2pml]
Cat:    RSF/user/fangg
Desc:   2-D Lowrank Finite-difference wave extrapolation on staggered grid
DocCmd: sfsglfd2pml | cat
Port:   stdin  rsf r req 	RSF standard input (containing fsource data)
Port:   stdout rsf w req 	RSF standard output (containing fwf data)
Port:   Gx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gz rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   sxx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sxz rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   szx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   szz rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  decay int  -   -  		Flag of decay boundary condtion: 1 = use ; 0 = not use 
LDesc:  (defaults to: DECAY_FLAG)
Param:  decaybegin int  -   -  		Begin time of using decay boundary condition 
LDesc:  (defaults to: DECAY_BEGIN)
Param:  freesurface enum-bool  -  n 		free surface
Param:  gdep float  -  -1.0 		recorder depth on grid
Param:  gp int  -  0 		recorder depth on index
Param:  pmld0 int  -   -  		PML parameter 
LDesc:  (defaults to: PMLD0)
Param:  pmlsize int  -   -  		size of PML layer 
LDesc:  (defaults to: PMLOUT)
Param:  slx float  -  -1.0 		source location x 
Param:  slz float  -  -1.0 		source location z 
Param:  snapinter int  -  1 		snap interval 
Param:  spx int  -  -1 		source location x (index)
Param:  spz int  -  -1 		source location z (index)
Param:  srcdecay enum-bool  -  n 		source decay
Param:  srcrange int  -  10 		source decay range
Param:  srctrunc float  -  100 		trunc source after srctrunc time (s)
Param:  verb enum-bool  -  n 		verbosity

