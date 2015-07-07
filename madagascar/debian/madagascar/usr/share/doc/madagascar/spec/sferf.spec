[sferf]
Cat:    RSF/user/fomels
Desc:   Bandpass filtering using erf function
DocCmd: sferf | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  der enum-bool  -  n 		compute derivative 
Param:  fhi float  -  -1. 		high frequency in band 
Param:  flo float  -  -1. 		low frequency in band 
Param:  rect float  -  1 		filter sharpness 
Param:  spline enum-bool  -  n 		if use B-spline erf 

