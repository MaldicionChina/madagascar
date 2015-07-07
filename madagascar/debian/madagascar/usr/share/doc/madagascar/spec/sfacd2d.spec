[sfacd2d]
Cat:    RSF/user/hpcss
Desc:   time-domain acoustic FD modeling
DocCmd: sfacd2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fw data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  verb enum-bool  -  n 		setup I/O files 

