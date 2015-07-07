[sfrays2a]
Cat:    RSF/system/seismic
Desc:   Ray tracing in VTI media by a Runge-Kutta integrator
DocCmd: sfrays2a | cat
Port:   stdin  rsf r req 	RSF standard input (containing vz data)
Port:   stdout rsf w req 	RSF standard output (containing rays data)
Param:  a0 float  -  0. 		minimum angle (if no anglefile) 
Param:  amax float  -  360. 		maximum angle (if no anglefile) 
Param:  anglefile string  -   -  		file with initial angles (auxiliary input file name)
Param:  dt float  -   -  		Sampling in time 
Param:  escvar enum-bool  -  n 		If y - output escape values, n - trajectories 
Param:  eta string  -   -  		eta parameter 
Param:  nr int  -   -  		number of angles (if no anglefile) 
Param:  nt int  -   -  		Number of time steps 
Param:  order int  -  4 		Interpolation order 
Param:  shotfile string  -   -  		file with shot locations (auxiliary input file name)
Param:  vel enum-bool  -  y 		If y, input is velocity; if n, slowness 
Param:  verb enum-bool  -  y 		Verbosity flag 
Param:  vx string  -   -  		horizontal velocity or slowness 
Param:  yshot float  -   -  		
LDesc:  (defaults to: o[1] + 0.5*(n[1]-1)*d[1])
Param:  zshot float  -  0. 		shot coordinates (if no shotfile) 

