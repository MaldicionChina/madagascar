[sfTestaniso]
Cat:    RSF/user/pyang
Desc:   A 2D demo of elliptically-anisotropic wave propagation (4th order)
DocCmd: sfTestaniso | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fvz data)
Port:   stdout rsf w req 	RSF standard output (containing Fw data)
Port:   vx rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -   -  		time sampling interval 
Param:  fm float  -  20.0 		dominant freq of Ricker wavelet 
Param:  ft int  -  0 		first recorded time 
Param:  jt int  -  1 		time interval 
Param:  nb int  -  30 		thickness of sponge ABC 
Param:  nt int  -   -  		number of time steps 
Param:  verb enum-bool  -  n 		verbosity 

