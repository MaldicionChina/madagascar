[sfvelcon3]
Cat:    RSF/user/gee
Desc:   3-D finite-difference velocity continuation on a helix
DocCmd: sfvelcon3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  y 		forward or backward continuation 
Param:  inv int  -  1 		inversion type 
Param:  nv int  -   -  		velocity steps 
LDesc:  (defaults to: nt)
Param:  vel float  -  1. 		initial velocity 

