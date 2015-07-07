[sfmake]
Cat:    RSF/user/gee
Desc:   Simple 2-D synthetics with crossing plane waves
DocCmd: sfmake | cat
Port:   stdout rsf w req 	RSF standard output (containing mod data)
Param:  n int  -  3 		
Param:  n1 int  -  100 		
Param:  n2 int  -  14 		
Param:  n3 int  -  1 		dimensions 
Param:  p int  -  3 		
Param:  second enum-bool  -  y 		if n, only one plane wave is modeled 
Param:  t1 int  -  4 		triangle smoother for first wave 
Param:  t2 int  -  4 		triangle smoother for second wave 

