[sfimospray]
Cat:    RSF/user/gee
Desc:   Inversion of constant-velocity nearest-neighbor inverse NMO
DocCmd: sfimospray | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  d2 float  -  200. 		offset sampling (if inv=n) 
Param:  n2 int  -  20 		number of offsets (if inv=n) 
Param:  o2 float  -  0. 		offset origin (if inv=n) 
Param:  v float  -  1000. 		velocity 

