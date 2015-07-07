[sfmig3]
Cat:    RSF/user/fomels
Desc:   3-D Kirchhoff time migration with antialiasing
DocCmd: sfmig3 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing mig data)
Port:   hdr rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  antialias string  -   -  		antialiasing type [triangle,flat,steep,none] 
Param:  d2 float  -   -  		
Param:  d3 float  -   -  		
Param:  n1 int  -   -  		
Param:  n2 int  -   -  		
Param:  n3 int  -   -  		
Param:  o2 float  -   -  		
Param:  o3 float  -   -  		
Param:  vel float  -   -  		migration velocity 

