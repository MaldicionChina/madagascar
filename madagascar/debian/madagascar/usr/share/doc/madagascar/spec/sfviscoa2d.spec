[sfviscoa2d]
Cat:    RSF/user/pyang
Desc:   2D visco-acoustic modeling with 8th order staggered-grid FD
DocCmd: sfviscoa2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fv data)
Port:   stdout rsf w req 	RSF standard output (containing Fw data)
Port:   px rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   pz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   rho rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   tau rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   tauo rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -   -  		time sampling interval 
Param:  fm float  -  20.0 		dominant freq of Ricker wavelet 
Param:  ft int  -  0 		first recorded time 
Param:  jt int  -  1 		time interval 
Param:  kt int  -   -  		output px and pz component at kt 
Param:  nb int  -  30 		thickness of PML ABC 
Param:  nt int  -   -  		number of time steps 
Param:  verb enum-bool  -  n 		verbosity, if y, output px and pz 

