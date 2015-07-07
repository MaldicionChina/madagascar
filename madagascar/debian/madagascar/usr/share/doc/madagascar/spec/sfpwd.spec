[sfpwd]
Cat:    RSF/user/pwd
Desc:   3-D plane wave destruction
DocCmd: sfpwd | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  both enum-bool  -  n 		if y, compute both left and right predictions 
Param:  n4 int  -  2 		what to compute in 3-D. 0: in-line, 1: cross-line, 2: both 
Param:  nj1 int  -  1 		in-line aliasing 
Param:  nj2 int  -  1 		cross-line aliasing 
Param:  order int  -  1 		accuracy 

