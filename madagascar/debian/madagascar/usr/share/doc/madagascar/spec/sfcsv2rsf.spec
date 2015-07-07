[sfcsv2rsf]
Cat:    RSF/user/ivlad
Desc:   Convert a delimited-text ASCII file to RSF binary floating point or int
DocCmd: sfcsv2rsf | cat
Param:  d1 float  -  1. 		
Param:  d2 float  -  1. 		
Param:  debug enum-bool  -  n 		Extra verbosity for debugging
Param:  delimiter string  -   -  		Separator between values in input file
LDesc:  (defaults to: ,)
Param:  dtype string  -   -  		Input type
LDesc:  (defaults to: float)
Param:  label1 string  -   -  		
LDesc:  (defaults to: unknown)
Param:  label2 string  -   -  		
LDesc:  (defaults to: unknown)
Param:  o1 float  -  0. 		
Param:  o2 float  -  0. 		
Param:  trunc enum-bool  -  n 		Truncate or add zeros if nr elems in rows differs
Param:  unit1 string  -   -  		
LDesc:  (defaults to: unknown)
Param:  unit2 string  -   -  		
LDesc:  (defaults to: unknown)
Param:  verb enum-bool  -  n 		Whether to echo n1, n2, infill/truncation

