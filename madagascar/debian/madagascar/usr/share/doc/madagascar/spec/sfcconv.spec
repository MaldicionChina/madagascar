[sfcconv]
Cat:    RSF/user/gee
Desc:   1-D convolution with complex numbers
DocCmd: sfcconv | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  lag int  -  1 		lag for internal convolution 
Param:  single enum-bool  -  y 		single channel or multichannel 

