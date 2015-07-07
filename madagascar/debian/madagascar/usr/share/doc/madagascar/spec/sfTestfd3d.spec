[sfTestfd3d]
Cat:    RSF/user/pyang
Desc:   3D acoustic time-domain FD modeling
DocCmd: sfTestfd3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fv data)
Port:   stdout rsf w req 	RSF standard output (containing Fw data)
Param:  dt float  -   -  		
Param:  fm float  -  20 		
Param:  frsf enum-bool  -  n 		free surface or not 
Param:  kt int  -   -  		record wavefield at time kt 
Param:  nb int  -  30 		
Param:  ns int  -  1 		
Param:  nt int  -   -  		
Param:  verb enum-bool  -  n 		verbosity 

