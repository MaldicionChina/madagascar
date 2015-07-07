[sfpick]
Cat:    RSF/user/fomels
Desc:   Automatic picking  from semblance-like panels
DocCmd: sfpick | cat
Port:   stdin  rsf r req 	RSF standard input (containing scn data)
Port:   stdout rsf w req 	RSF standard output (containing pik data)
Param:  an float  -  1. 		axes anisotropy 
Param:  gate int  -  3 		picking gate 
Param:  niter int  -  100 		number of iterations 
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  smooth enum-bool  -  y 		if apply smoothing 
Param:  vel0 float  -   -  		surface velocity 
LDesc:  (defaults to: o2)

