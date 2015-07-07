[sfpcrdata2]
Cat:    RSF/user/cram
Desc:   Prepare data for 2-D angle-domain migration
DocCmd: sfpcrdata2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  KMAH enum-bool  -  y 		y - account for phase shifts due to KMAH index 
Param:  absoff enum-bool  -  n 		y - absolute offset (default - relative to shot axis) 
Param:  diff enum-bool  -  y 		y - apply half-order differentiation 
Param:  filter enum-bool  -  y 		y - antialiasing filter for data 
Param:  verb enum-bool  -  n 		verbosity flag 

