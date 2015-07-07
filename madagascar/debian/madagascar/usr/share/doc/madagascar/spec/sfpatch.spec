[sfpatch]
Cat:    RSF/user/fomels
Desc:   Patching (N-dimensional)
DocCmd: sfpatch | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dim int  -   -  		
LDesc:  (defaults to: dim0)
Param:  inv enum-bool  -  n 		inverse or forward operation 
Param:  n0 int-list  -   -  		data dimensions (for inv=y)  [dim]
Param:  p int-list  -   -  		number of windows  [dim]
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  w int-list  -   -  		window size  [dim]
Param:  weight enum-bool  -  n 		if y, apply weighting to each patch 

