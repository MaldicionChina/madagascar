[sfsimidenoise]
Cat:    RSF/user/chenyk
Desc:   Random noise attenuation using local similarity
DocCmd: sfsimidenoise | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   similarity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  thr float  -   -  		thresholding level 

