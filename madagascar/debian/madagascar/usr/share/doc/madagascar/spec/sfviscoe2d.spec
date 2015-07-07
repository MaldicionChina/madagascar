[sfviscoe2d]
Cat:    RSF/user/pyang
Desc:   2D 4-th order visco-elastic wave propagation using sponge ABC
DocCmd: sfviscoe2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fvp data)
Port:   stdout rsf w req 	RSF standard output (containing Fwavz data)
Port:   rho rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   tauo rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   taup rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   taus rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vs rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wavx rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt float  -   -  		time sampling interval 
Param:  fm float  -  20.0 		dominant freq of Ricker wavelet 
Param:  ft int  -  0 		first recorded time 
Param:  jt int  -  1 		time interval 
Param:  kt int  -   -  		record wavefield at time kt 
Param:  nb int  -  30 		thickness of sponge ABC 
Param:  nt int  -   -  		number of time steps 
Param:  verb enum-bool  -  n 		verbosity 

