[sfseekwin]
Cat:    RSF/user/ivlad
Desc:   Cannot take input from a pipe because stdin cannot be seeked through
DocCmd: sfseekwin | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  nread   -   -  		
LDesc:  (defaults to: 10         )
Param:  nseek   -   -  		
LDesc:  (defaults to: 10         )
Param:  whence   -   -  		
LDesc:  (defaults to: sf_seek_set)

