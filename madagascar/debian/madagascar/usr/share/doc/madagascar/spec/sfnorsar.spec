[sfnorsar]
Cat:    RSF/user/urdaneta
Desc:   Traveltime and amplitude estimation using wavefront construction
DocCmd: sfnorsar | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   ampl rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   time rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  DSmax float  -  5 		Maximum distance between contiguos points of a wavefront 
Param:  N int  -  3 		Number of control points 
Param:  TETAMAX float  -  1.5 		Truncation parameter 
Param:  alpha2 float  -  4.0 		Width of gaussian weighting function 
Param:  depth float  -   -  		Depth location of sources 
LDesc:  (defaults to: dz)
Param:  ds float  -  1. 		interval between sources 
Param:  dt float  -  0.0005 		time step 
Param:  first int  -  1 		Obtain first arrivals only 
Param:  freq float  -  100. 		Pseudo-frequency of waverays 
Param:  gap int  -  1 		Draw wavefronts every gap intervals 
Param:  gdx float  -   -  		
LDesc:  (defaults to: dx)
Param:  gdz float  -   -  		
LDesc:  (defaults to: dz)
Param:  gnx int  -   -  		Coordinates of output grid 
LDesc:  (defaults to: nx)
Param:  gnz int  -   -  		
LDesc:  (defaults to: nz)
Param:  gox float  -   -  		
LDesc:  (defaults to: ox)
Param:  goz float  -   -  		GET LOMAX SPECIFIC PARAMETERS 
LDesc:  (defaults to: oz)
Param:  inter int  -  1 		If use linear interpolation 
Param:  lomx int  -  1 		Use Lomax's waveray method 
Param:  nang int  -  10 		Number of take-off angles 
Param:  nou int  -  6 		GET GRIDDING PARAMETERS 
Param:  nrmax int  -  2000 		Maximum number of points that define a wavefront 
Param:  nt int  -  5 		Number of time steps between wavefronts 
Param:  os float  -  0. 		first source location 
Param:  pr int  -  0 		For debugging porpouses 
Param:  prcube int  -  0 		For debugging porpouses 
Param:  rays int  -  0 		If draw rays 
Param:  wfront int  -  0 		If draw wavefronts 

