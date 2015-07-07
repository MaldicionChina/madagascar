[sfwei]
Cat:    RSF/user/psava
Desc:   3-D modeling/migration with extended SSF
DocCmd: sfwei | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fsou data)
Port:   stdout rsf w req 	RSF standard output (containing Fcic data)
Port:   cip rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   coo rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   dat rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   slo rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  causal enum-bool  -  n 		causality 
Param:  irun string  -   -  		
Param:  verb enum-bool  -  n 		verbosity flag 

