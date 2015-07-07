[sflum]
Cat:    RSF/user/yliu
Desc:   1D LUM filter
DocCmd: sflum | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  boundary enum-bool  -  n 		if y, boundary is data, whereas zero
Param:  nfw int  -   -  		filter-window length (positive and odd integer)
Param:  shnclip int  -   -  		sharpener tuning parameter (1 <= shnclip <= (nfw+1)/2, the default is (nfw+1)/2)
LDesc:  (defaults to: (nfw+1)/2)
Param:  smnclip int  -   -  		smoother tuning parameter (1 <= smnclip <= (nfw+1)/2, the default is (nfw+1)/2)
LDesc:  (defaults to: (nfw+1)/2)

