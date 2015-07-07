[sfmspef]
Cat:    RSF/user/gee
Desc:   Multi-scale PEF estimation
DocCmd: sfmspef | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing pef data)
Param:  a int-list  -   -  		 [dim]
Param:  center int-list  -   -  		 [dim]
Param:  gap int-list  -   -  		 [dim]
Param:  jump int-list  -   -  		 [ns]
Param:  lag string  -   -  		output file for filter lags 
Param:  maskin string  -   -  		optional input mask file (auxiliary input file name)
Param:  maskout string  -   -  		optional output mask file 
Param:  niter int  -   -  		
LDesc:  (defaults to: nh*2)
Param:  ns int  -   -  		number of scales 

