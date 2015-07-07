[sfic]
Cat:    RSF/user/psava
Desc:   Imaging condition
DocCmd: sfic | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fs data)
Port:   stdout rsf w req 	RSF standard output (containing Fi data)
Port:   ur rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  1e-6 		epsilon 
Param:  nbuf int  -  1 		buffer size 
Param:  ompchunk int  -  1 		OpenMP data chunk size 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  version int  -  0 		I.C. version (see paper) 

