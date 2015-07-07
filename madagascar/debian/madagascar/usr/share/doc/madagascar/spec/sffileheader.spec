[sffileheader]
Cat:    RSF/user/slim
Desc:   dumps header information to the standard output
DocCmd: sffileheader | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Param:  all enum-bool  -  n 		If y, print all values, icluding singleton dimensions.
LDesc:         If n, drop trailing singleteon dimensions.
Param:  large enum-bool  -  n 		if y, file with large dimensions. 
Param:  parform enum-bool  -  y 		If y, print out parameter=value. If n, print out value. 

