[sfvelcon]
Cat:    RSF/user/fomels
Desc:   Post-stack velocity continuation by implicit finite differences
DocCmd: sfvelcon | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  add enum-bool  -  n 		addition flag 
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  inv int  -  0 		amplitude type 
Param:  nv int  -   -  		number of steps 
LDesc:  (defaults to: n1)
Param:  v0 float  -  0. 		starting velocity 
Param:  vel float  -  0.75 		final velocity 

