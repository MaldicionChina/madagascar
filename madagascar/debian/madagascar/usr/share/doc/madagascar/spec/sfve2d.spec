[sfve2d]
Cat:    RSF/user/kourkina
Desc:   Convert interval velocity to Dix velocity
DocCmd: sfve2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing fsc data)
Port:   stdout rsf w req 	RSF standard output (containing fid data)
Port:   x rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   z rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt float  -   -  		
Param:  nt int  -   -  		
Param:  order int  -  4 		interpolation order 

