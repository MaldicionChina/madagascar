[sflpef]
Cat:    RSF/user/gee
Desc:   Find PEF on aliased traces
DocCmd: sflpef | cat
Port:   stdin  rsf r req 	RSF standard input (containing dat data)
Port:   stdout rsf w req 	RSF standard output (containing pef data)
Param:  a int-list  -   -  		 [dim]
Param:  center int-list  -   -  		 [dim]
Param:  gap int-list  -   -  		 [dim]
Param:  jump int  -  2 		
Param:  lag string  -   -  		output file for filter lags 

