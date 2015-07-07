[sfsort]
Cat:    RSF/user/slim
Desc:   Sort a float/complex vector by absolute values
DocCmd: sfsort | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  ascmode enum-bool  -  n 		y=ascending; n=descending 
Param:  dim int  -   -  		maximum dimension 
LDesc:  (defaults to: dim)
Param:  memsize int  -   -  		Max amount of RAM (in Mb) to be used 
LDesc:  (defaults to: sf_memsize())

