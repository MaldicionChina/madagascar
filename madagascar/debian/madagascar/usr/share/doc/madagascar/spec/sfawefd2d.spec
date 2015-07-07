[sfawefd2d]
Cat:    RSF/user/cwp
Desc:   2D acoustic time-domain FD modeling
DocCmd: sfawefd2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing file_wav data)
Port:   stdout rsf w req 	RSF standard output (containing file_dat data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  cden string  -   -  		Constant density
Param:  dabc enum-bool  -  n 		Absorbing BC 
Param:  dqx float  -   -  		Saved wfld window dx 
LDesc:  (defaults to: sf_d(ax))
Param:  dqz float  -   -  		Saved wfld window dz 
LDesc:  (defaults to: sf_d(az))
Param:  expl enum-bool  -  n 		Multiple sources, one wvlt
Param:  fdorder int  -  4 		spatial FD order 
Param:  fsrf enum-bool  -  n 		Free surface flag 
Param:  hybridbc enum-bool  -  n 		hybrid Absorbing BC 
Param:  jdata int  -  1 		# of t steps at which to save receiver data 
Param:  jsnap int  -   -  		# of t steps at which to save wavefield 
LDesc:  (defaults to: nt)
Param:  nbell int  -  5 		gaussian for source injection 
Param:  nqx int  -   -  		Saved wfld window nx 
LDesc:  (defaults to: sf_n(ax))
Param:  nqz int  -   -  		Saved wfld window nz 
LDesc:  (defaults to: sf_n(az))
Param:  optfd enum-bool  -  n 		optimized FD coefficients flag 
Param:  oqx float  -   -  		Saved wfld window ox 
LDesc:  (defaults to: sf_o(ax))
Param:  oqz float  -   -  		Saved wfld window oz 
LDesc:  (defaults to: sf_o(az))
Param:  sinc enum-bool  -  n 		sinc source injection 
Param:  snap enum-bool  -  n 		Wavefield snapshots flag 
Param:  verb enum-bool  -  n 		Verbosity flag 

