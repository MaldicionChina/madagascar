[sfmffit]
Cat:    RSF/user/fomels
Desc:   Fitting multi-focusing approximations
DocCmd: sfmffit | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   coef rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   fit rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  type string  -   -  		Type of approximation (crs,mf,nonhyperbolic) 
Param:  x0 float  -   -  		central midpoint 
LDesc:  (defaults to: m0)

