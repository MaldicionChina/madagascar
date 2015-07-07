[sfcrssemb]
Cat:    RSF/user/aklokov
Desc:   CRS-based semblance
DocCmd: sfcrssemb | cat
Port:   stdin  rsf r req 	RSF standard input (containing inDags_ data)
Port:   stdout rsf w req 	RSF standard output (containing sembFile_ data)
Port:   dataSq rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  coher int  -  11 		height of a vertical window for semblance calculation 
Param:  dipapp int  -  11 		number of traces in the x-dip direction processed simultaneously 
Param:  s1 float  -   -  		
Param:  s2 float  -   -  		
Param:  scatnum int  -  1 		shows how many traces were stacked in the scattering angle direction; 
LDesc:         if the stack was normalized use the default value 
LDesc:      
Param:  xapp int  -  1 		number of CIGs in the inline-direction processed simultaneously 

