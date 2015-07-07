[sfirays]
Cat:    RSF/user/llisiw
Desc:   Fast marching for image rays
DocCmd: sfirays | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  f0 string  -   -  		auxiliary output file name
Param:  order int  -  1 		fastmarching accuracy order 
Param:  t0 string  -   -  		auxiliary output file name
Param:  thres float  -  10. 		thresholding for caustics 
Param:  velocity enum-bool  -  y 		y, inputs are velocity / n, slowness-squared 
Param:  x0 string  -   -  		output upwind neighbor (auxiliary output file name)

