[sfsmstack]
Cat:    RSF/user/gchliu
Desc:   Stack a dataset over the second dimensions by smart stacking
DocCmd: sfsmstack | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  esp float  -  1e-10 		
Param:  ifwt enum-bool  -  y 		
Param:  l int  -  0 		parameter for alpha-trimmed mean 
Param:  s int  -  1 		exponent

