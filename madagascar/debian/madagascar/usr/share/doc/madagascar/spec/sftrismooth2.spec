[sftrismooth2]
Cat:    RSF/user/pwd
Desc:   2-D smoothing by triangle directional shaping
DocCmd: sftrismooth2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		
Param:  rect1 int  -  3 		
Param:  rect2 int  -  3 		smoothing radius 

