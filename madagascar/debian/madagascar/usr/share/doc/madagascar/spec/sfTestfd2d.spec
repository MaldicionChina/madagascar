[sfTestfd2d]
Cat:    RSF/user/pyang
Desc:   A demo of 2D FD test
DocCmd: sfTestfd2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fv data)
Port:   stdout rsf w req 	RSF standard output (containing Fw data)
Param:  dt float  -   -  		time sampling interval 
Param:  fm float  -  20.0 		dominant freq of Ricker wavelet 
Param:  ft int  -  0 		first recorded time 
Param:  jt int  -  1 		time interval 
Param:  nb int  -  30 		thickness of sponge ABC 
Param:  nt int  -   -  		number of time steps 

