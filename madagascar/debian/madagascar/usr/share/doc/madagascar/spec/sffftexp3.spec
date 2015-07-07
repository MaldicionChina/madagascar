[sffftexp3]
Cat:    RSF/user/fomels
Desc:   3-D FFT-based zero-offset exploding reflector modeling/migration
DocCmd: sffftexp3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing image data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -   -  		time sampling (if modeling) 
Param:  dz float  -   -  		time sampling (if migration) 
Param:  mig enum-bool  -  n 		if n, modeling; if y, migration 
Param:  nt int  -   -  		time samples (if modeling) 
Param:  nz int  -   -  		time samples (if migration) 
Param:  ompchunk int  -  1 		OpenMP data chunk size 

