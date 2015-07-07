[sfeikods]
Cat:    RSF/user/llisiw
Desc:   Fast marching with source perturbation
DocCmd: sfeikods | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (containing time data)
Param:  b1 int  -   -  		
LDesc:  (defaults to: plane[2]? n1: (int) (br1/d1+0.5))
Param:  b2 int  -   -  		
LDesc:  (defaults to: plane[1]? n2: (int) (br2/d2+0.5))
Param:  b3 int  -   -  		Constant-velocity box around the source (in samples) 
LDesc:  (defaults to: plane[0]? n3: (int) (br3/d3+0.5))
Param:  br1 float  -   -  		
LDesc:  (defaults to: d1)
Param:  br2 float  -   -  		
LDesc:  (defaults to: d2)
Param:  br3 float  -   -  		Constant-velocity box around the source (in physical dimensions) 
LDesc:  (defaults to: d3)
Param:  l int  -  1 		source perturbation direction 
Param:  order int  -  2 		Accuracy order 
Param:  plane1 enum-bool  -  n 		
Param:  plane2 enum-bool  -  n 		
Param:  plane3 enum-bool  -  n 		plane-wave source 
Param:  shotfile string  -   -  		File with shot locations (n2=number of shots, n1=3) (auxiliary input file name)
Param:  sweep enum-bool  -  n 		if y, use fast sweeping instead of fast marching 
Param:  tdl1 string  -   -  		auxiliary output file name
Param:  tdl2 string  -   -  		auxiliary output file name
Param:  tds1 string  -   -  		auxiliary output file name
Param:  tds2 string  -   -  		auxiliary output file name
Param:  vel enum-bool  -  y 		if y, the input is velocity; n, slowness squared 
Param:  xshot float  -   -  		
LDesc:  (defaults to: o3 + 0.5*(n3-1)*d3)
Param:  yshot float  -   -  		
LDesc:  (defaults to: o2 + 0.5*(n2-1)*d2)
Param:  zshot float  -  0. 		Shot location (used if no shotfile) 

