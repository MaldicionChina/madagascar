[sfmodelcreate]
Cat:    RSF/user/jeff
Desc:   Create a dipping layer model for HTI testing purposes.  Has fixed velocity structure, but can change dip of layer and degree of anisotropy
DocCmd: sfmodelcreate | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fu data)
Port:   stdout rsf w req 	RSF standard output (containing Fc data)
Param:  a float  -  1 		Parameter in dipping plane: ax+by+cz+d=0 
Param:  allaniso enum-bool  -  n 		flag (y/N) whether entire model is anisotropic 
Param:  aniso enum-bool  -  n 		flag (y/N) for anisotropic layer #2 
Param:  b float  -  1 		Parameter in dipping plane: ax+by+cz+d=0 
Param:  d float  -   -  		Parameter in dipping plane: ax+by+cz+d=0 
LDesc:  (defaults to: n3/6.)
Param:  din float  -  .1 		delta anisotropy parameter 
Param:  ein float  -  .1 		epsilon anisotropy parameter 
Param:  gin float  -  .2 		gamma anisotropy parameter 
Param:  ompchunk int  -  1 		set the omp chunk size 
Param:  rho float  -  2. 		Background Density model 
Param:  verb enum-bool  -  y 		verbose or note (Y/n) 

