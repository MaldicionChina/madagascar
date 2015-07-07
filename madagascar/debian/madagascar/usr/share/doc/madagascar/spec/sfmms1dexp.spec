[sfmms1dexp]
Cat:    RSF/user/fangg
Desc:   1D method of manufactured solution using Gaussian pulsa
DocCmd: sfmms1dexp | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fvel data)
Port:   stdout rsf w req 	RSF standard output (containing Fmms data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   denhf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   dvel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   dvelhf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   preinit rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   presrc rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   velhf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   velinit rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   velsrc rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  alpha float  -  1.0e-2 		source parameter
Param:  dt float  -   -  		time step
Param:  nt int  -   -  		number of time step
Param:  slx float  -   -  		center of source location: x
LDesc:  (defaults to: nx*dx*0.5)

