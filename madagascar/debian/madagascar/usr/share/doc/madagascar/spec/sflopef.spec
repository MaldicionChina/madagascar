[sflopef]
Cat:    RSF/user/gee
Desc:   Local Prediction-Error Filter (1-D, 2-D, and 3-D)
DocCmd: sflopef | cat
Port:   stdin  rsf r req 	RSF standard input (containing dat data)
Port:   stdout rsf w req 	RSF standard output (containing pef data)
Param:  a int-list  -   -  		filter size  [dim1]
Param:  center int-list  -   -  		filter center  [dim1]
Param:  dim int  -   -  		PEF dimensionality 
LDesc:  (defaults to: dim)
Param:  gap int-list  -   -  		filter gap  [dim1]
Param:  k int-list  -   -  		number of windows  [dim1]
Param:  lag string  -   -  		output file for filter lags 
Param:  mask string  -   -  		auxiliary input file name
Param:  steepdip enum-bool  -  n 		if y, do steep-dip PEF estimation 
Param:  tgap float  -  0.030 		time gap for steep-dip decon 
Param:  vel float  -  1.7 		velocity for steep-dip decon 
Param:  w int-list  -   -  		window size  [dim1]

