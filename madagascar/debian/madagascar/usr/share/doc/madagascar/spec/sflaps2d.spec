[sflaps2d]
Cat:    RSF/user/psava
Desc:   OpenMP lagged-products in the time-domain
DocCmd: sflaps2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fs data)
Port:   stdout rsf w req 	RSF standard output (containing Fi data)
Port:   cc rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ur rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  buf enum-bool  -  n 		
Param:  nht int  -  0 		number of lags on the t axis 
Param:  nhx int  -  0 		number of lags on the x axis 
Param:  nhz int  -  0 		number of lags on the z axis 
Param:  verb enum-bool  -  n 		verbosity flag 

