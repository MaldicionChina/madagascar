[sfstackn]
Cat:    RSF/user/saragiotis
Desc:   Stack prespecified values
DocCmd: sfstackn | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  max string  -   -  		file determining up to which value to stack (auxiliary input file name)
Param:  mean enum-bool  -  y 		if n, sum; if y, average 
Param:  min string  -   -  		file determining from which value to stack (auxiliary input file name)
Param:  thres float  -  0. 		threshold (percentage of maxabs) 

