[sfpscefd]
Cat:    RSF/user/chen
Desc:   EFD phase shift wave extrapolation
DocCmd: sfpscefd | cat
Port:   stdin  rsf r req 	RSF standard input (containing modl data)
Port:   stdout rsf w req 	RSF standard output (containing imag data)
Port:   data rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wave rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  jt int  -  40 		time step for wave data 
Param:  nz int  -   -  		depth number 
LDesc:  (defaults to: nz0)

