[sfrtm2d]
Cat:    RSF/user/pyang
Desc:   2-D zero-offset reverse-time migration
DocCmd: sfrtm2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing imag data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		if y, migration; else, modeling 
Param:  dt float  -   -  		time sampling interval: dt 
Param:  n0 int  -  0 		shot depth in the grid 
Param:  nt int  -   -  		number of time steps 

