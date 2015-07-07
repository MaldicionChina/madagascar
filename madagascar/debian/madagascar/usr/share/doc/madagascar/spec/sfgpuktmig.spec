[sfgpuktmig]
Cat:    RSF/user/cuda
Desc:   Prestack time migration (2-D/3-D) with CUDA
DocCmd: sfgpuktmig | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing image data)
Param:  aa enum-bool  -  y 		Antialiaing flag 
Param:  apx int  -   -  		Apperture half-width in x direction 
LDesc:  (defaults to: onx/2)
Param:  apy int  -   -  		Apperture half-width in y direction 
LDesc:  (defaults to: ony/2)
Param:  cxcy string  -   -  		File with midpoint coordinates (auxiliary input file name)
Param:  dbtr int  -  -1 		Desired number of traces per block of threads 
Param:  diff enum-bool  -  y 		Differentiation flag 
Param:  gxgy string  -   -  		File with receiver coordinates (auxiliary input file name)
Param:  maxtri int  -  13 		Maximum half-length of the antialias filter 
Param:  sxsy string  -   -  		File with shot coordinates (auxiliary input file name)
Param:  time enum-bool  -  n 		Total time measurement time 
Param:  trfact float  -   -  		Trace factor for antialias filter length calculation 
LDesc:  (defaults to: 4.0*(0.5*(odx + ody)/dt))
Param:  verb enum-bool  -  n 		Verbosity flag 
Param:  vrms string  -   -  		File with RMS velocities (auxiliary input file name)

