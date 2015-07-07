[sftvmf]
Cat:    RSF/user/yliu
Desc:   1D Time-varying median filtering
DocCmd: sftvmf | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  alpha int  -  2 		time-varying window parameter 'alpha' (default=2)
Param:  beta int  -  0 		time-varying window parameter 'beta' (default=0)
Param:  boundary enum-bool  -  n 		if y, boundary is data, whereas zero
Param:  delta int  -  4 		time-varying window parameter 'delta' (default=4)
Param:  gamma int  -  2 		time-varying window parameter 'gamma' (default=2)
Param:  nfw int  -   -  		reference filter-window length (>delta, positive and odd integer)

