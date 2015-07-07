[sfemd]
Cat:    RSF/user/chenyk
Desc:   Empirical Mode Decomposition
DocCmd: sfemd | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (containing outp data)
Param:  mimf int  -  0 		Maximum number of IMFs, the default is as many as possible. 
Param:  miter int  -   -  		Maximum number of iterations during sifting, the default is 1000. 
LDesc:  (defaults to: MAX_ITERATIONS)
Param:  threshold float  -   -  		Sifting stoping parameter: threshold, the default is 0.05. 
LDesc:  (defaults to: DEFAULT_THRESHOLD)
Param:  tolerance float  -   -  		Sifting stoping parameter: tolerance, the default is 0.05. 
LDesc:  (defaults to: DEFAULT_TOLERANCE)

