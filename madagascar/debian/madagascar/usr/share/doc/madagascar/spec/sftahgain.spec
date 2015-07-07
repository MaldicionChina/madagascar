[sftahgain]
Cat:    RSF/user/karl
Desc:   Read Trace And Header (tah) from standard input and apply GAIN
DocCmd: sftahgain | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  agc float  -  0.0 		Length of agc window in seconds.  0.0 means no agc 
Param:  epow float  -  0.0 		multiply data by exp(epow*t) 
Param:  scale float  -  1.0 		multiply data by this float 
Param:  tpow float  -  0.0 		multiply data by t^tpow 
Param:  tstart float-list  -   -  		 [numtstart]
Param:  verbose int  -  1 		
LDesc:  
LDesc:         flag to control amount of print
LDesc:         0 terse, 1 informative, 2 chatty, 3 debug
LDesc:      
Param:  xxstart float-list  -   -  		 [numxstart]

