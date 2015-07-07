[sfxcor2d]
Cat:    RSF/user/psava
Desc:   OpenMP time- or freq-domain cross-correlation on axes 1,2,3
DocCmd: sfxcor2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fs data)
Port:   stdout rsf w req 	RSF standard output (containing Fi data)
Port:   uu rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  axis int  -  2 		stack axis 
Param:  nbuf int  -  1 		buffer size 
Param:  verb enum-bool  -  n 		verbosity flag 

