[sftsmf]
Cat:    RSF/user/chenyk
Desc:   Two-step space varying median filtering
DocCmd: sftsmf | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  L string  -   -  		auxiliary output file name
Param:  N int  -   -  		average energy level (AEL) computing number 
LDesc:  (defaults to: (f2-f1+1)*n1)
Param:  ael float  -  0.0 		get the average energy level (AEL) empirically defined 
Param:  boundary enum-bool  -  n 		if y, boundary is data, whereas zero
Param:  l1 int  -  2 		space-varying window parameter 'l1' (default=2)
Param:  l2 int  -  0 		space-varying window parameter 'l2' (default=0)
Param:  l3 int  -  2 		space-varying window parameter 'l3' (default=2)
Param:  l4 int  -  4 		space-varying window parameter 'l4' (default=4)
Param:  ne int  -   -  		processing window ending point, corresponding to the temporal axis, n2 means transposed first-axis dimension. 
LDesc:  (defaults to: n2-1)
Param:  nfw int  -   -  		reference filter-window length (>l4, positive and odd integer)
Param:  ns int  -  0 		processing window starting point, corresponding to the temporal axis 
Param:  verb enum-bool  -  n 		if print the computed average energy level (AEL) 

