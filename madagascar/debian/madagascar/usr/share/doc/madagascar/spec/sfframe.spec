[sfframe]
Cat:    RSF/user/gee
Desc:   Create a frame for binning
DocCmd: sfframe | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   xyz rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  base float  -  0. 		base to be subtracted from z 

