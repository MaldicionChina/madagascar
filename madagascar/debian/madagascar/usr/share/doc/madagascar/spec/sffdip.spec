[sffdip]
Cat:    RSF/user/pwd
Desc:   3D fast dip estimation by plane wave destruction
DocCmd: sffdip | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  liter int  -  20 		number of linear iterations 
Param:  mask string  -   -  		auxiliary input file name
Param:  n4 int  -  2 		what to compute in 3-D. 0: in-line, 1: cross-line, 2: both 
Param:  rect1 int  -  1 		dip smoothness on 1st axis 
Param:  rect2 int  -  1 		dip smoothness on 2nd axis 
Param:  rect3 int  -  1 		dip smoothness on 3rd axuis 
Param:  verb enum-bool  -  n 		verbosity flag 

