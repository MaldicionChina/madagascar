[sfwavedoc]
Cat:    RSF/user/hpcss
Desc:   Rice HPCSS seismic modeling and migration
DocCmd: sfwavedoc | cat
Port:   stdin  rsf r req 	RSF standard input (containing vfile data)
Port:   stdout rsf w req 	RSF standard output (containing tfile data)
Param:  dt float  -   -  		step in t 
Param:  fpeak float  -  0.01 		center frequency of Ricker wavelet 
Param:  igxbeg int  -  1 		far left receiver x coord in units of dx 
Param:  igxend int  -  0 		far right receiver x coord in units of dx 
Param:  igz int  -  1 		recvr depth, in units of dz 
Param:  ihmax int  -  0 		offset radius, units of dx 
Param:  imbeg int  -   -  		midpoint begin 
LDesc:  (defaults to: ihmax)
Param:  imend int  -   -  		midpoint end 
LDesc:  (defaults to: nx-ihmax-1)
Param:  imskip int  -  1 		midpoint skip 
Param:  iskip int  -  1 		interval between sources in units of dx 
Param:  isxbeg int  -   -  		far left source x coord in units of dx 
LDesc:  (defaults to: (nx)/2)
Param:  isxend int  -   -  		far right source x coord in units of dx 
LDesc:  (defaults to: (nx)/2)
Param:  isz int  -  1 		source depth, in units of dz 
Param:  nm int  -  0 		number of time steps to skip between movie frames
LDesc:         (<=0 for no movie) 
Param:  nt int  -   -  		number of time steps 
Param:  receiver string  -   -  		receiver movie file (auxiliary output file name)
Param:  source string  -   -  		source movie file (auxiliary output file name)

