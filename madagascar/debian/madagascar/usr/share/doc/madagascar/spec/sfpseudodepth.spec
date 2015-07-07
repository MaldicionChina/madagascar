[sfpseudodepth]
Cat:    RSF/user/xuxin
Desc:   depth to vertical-time interpolation
DocCmd: sfpseudodepth | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fin data)
Port:   stdout rsf w req 	RSF standard output (containing Fout data)
Port:   tau rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  d float  -   -  		tau d (>0) 
Param:  inv enum-bool  -  n 		if y, tau to z; if n, tau to z 
Param:  linear enum-bool  -  y 		if y, linear spline; if n, cubic spline (buggy) 
Param:  n int  -   -  		tau n 
Param:  o float  -  0. 		tau o 

