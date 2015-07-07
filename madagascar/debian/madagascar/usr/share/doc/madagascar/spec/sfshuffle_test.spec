[sfshuffle_test]
Cat:    RSF/user/pyang
Desc:   shuffle the data
DocCmd: sfshuffle_test | cat
Port:   stdin  rsf r req 	RSF standard input (containing pi data)
Port:   stdout rsf w req 	RSF standard output (containing po data)
Param:  axis int  -  2 		
Param:  inv enum-bool  -  n 		
Param:  seed int  -   -  		
LDesc:  (defaults to: n2)

