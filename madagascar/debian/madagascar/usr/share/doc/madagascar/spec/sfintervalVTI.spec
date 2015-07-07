[sfintervalVTI]
Cat:    RSF/user/lcasasan
Desc:   Interval/Effective VTI parameters from Effective/Interval profiles
DocCmd: sfintervalVTI | cat
Port:   stdin  rsf r req 	RSF standard input (containing vn data)
Port:   stdout rsf w req 	RSF standard output (containing vn_out data)
Param:  eta string  -   -  		input eta(auxiliary input file name)
Param:  eta_out string  -   -  		output eta(auxiliary output file name)
Param:  interval enum-bool  -  y 		output are interval [y] or effective [n] profiles 
Param:  vH_out string  -   -  		output HOR vel(auxiliary output file name)

