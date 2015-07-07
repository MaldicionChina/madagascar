[sfst]
Cat:    RSF/user/yliu
Desc:   S transform
DocCmd: sfst | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  fhi float  -   -  		High frequency in band, default is Nyquist 
Param:  flo float  -   -  		Low frequency in band, default is 0 
Param:  inv enum-bool  -  n 		if y, do inverse transform 

