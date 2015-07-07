[sfsimidenoise1]
Cat:    RSF/user/chenyk
Desc:   Random noise attenuation using local similarity (different weighting approach)
DocCmd: sfsimidenoise1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   similarity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  s1 float  -   -  		thresholding level 1 
Param:  s2 float  -   -  		thresholding level 2 

