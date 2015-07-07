[sfmkrcv]
Cat:    RSF/user/llisiw
Desc:   Make topography mask / receiver list / record list for first-arrival traveltime tomography
DocCmd: sfmkrcv | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   reco rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  air float  -  0.5 		air velocity for thresholding topography 
Param:  dp float  -  1. 		ray-parameter increment 
Param:  fix enum-bool  -  n 		if y, fixed-spread; n, moving acquisition 
Param:  np int  -  1 		ray-parameter number 
Param:  offset1 int  -  0 		receiver offset inline 
Param:  offset2 int  -  0 		receiver offset crossline 
Param:  order int  -  2 		fast marching accuracy order 
Param:  p0 float  -  0. 		ray-parameter start 
Param:  plane enum-bool  -  n 		if y, plane-wave source; n, point source 
Param:  shot string  -   -  		auxiliary input file name
Param:  time string  -   -  		auxiliary output file name
Param:  topo string  -   -  		auxiliary output file name
Param:  velocity enum-bool  -  y 		if y, the input is velocity; n, slowness squared 

