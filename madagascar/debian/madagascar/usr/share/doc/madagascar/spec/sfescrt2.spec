[sfescrt2]
Cat:    RSF/user/cram
Desc:   Escape tables by ray tracing with escape equations in 2-D
DocCmd: sfescrt2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing spdom data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  aper float  -   -  		Maximum aperture in x and y directions from current point (default - up to model boundaries) 
LDesc:  (defaults to: SF_HUGE)
Param:  df float  -  0.25 		< Maximum distance to travel per step (fraction of the cell size) >
Param:  dt float  -  0.001 		Time sampling 
Param:  md float  -   -  		Maximum distance for a ray to travel (default - up to model boundaries) 
LDesc:  (defaults to: SF_HUGE)
Param:  na int  -  360 		Number of phase angles 
Param:  nc int  -  0 		Number of threads to use for ray tracing (OMP_NUM_THREADS by default) 
Param:  nt int  -  1001 		Number of time samples for each trajectory 
Param:  parab enum-bool  -  y 		y - use parabolic approximation of trajectories, n - straight line 
Param:  traj string  -   -  		Trajectory output (auxiliary output file name)
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  vspl string  -   -  		Spline coefficients for velocity model (auxiliary input file name)

