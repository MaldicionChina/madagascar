[sfconv]
Cat:    RSF/user/gee
Desc:   1-D convolution
DocCmd: sfconv | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  each enum-bool  -  n 		if y, new filter for each trace 
Param:  lag int  -  1 		lag for internal convolution 
Param:  trans enum-bool  -  n 		if y, transient convolution; if n, internal 

