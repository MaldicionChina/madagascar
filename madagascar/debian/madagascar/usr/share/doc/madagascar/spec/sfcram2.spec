[sfcram2]
Cat:    RSF/user/cram
Desc:   2-D angle-domain Kirchhoff migration based on escape tables
DocCmd: sfcram2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing esct data)
Port:   stdout rsf w req 	RSF standard output (containing oimag data)
Param:  data string  -   -  		Processed prestack data (auxiliary input file name)
Param:  dazmax float  -  180.0 		Maximum allowed dip angle (abs.value) at z max 
Param:  dazmin float  -  180.0 		Maximum allowed dip angle (abs.value) at z min 
Param:  dipagath string  -   -  		Dip angle gathers (angle, z, x) (auxiliary output file name)
Param:  dipimap string  -   -  		Dip gathers illumination (angle, z, x) (auxiliary output file name)
Param:  dipsmap string  -   -  		Dip gathers semblance (angle, z, x) (auxiliary output file name)
Param:  full string  -   -  		Full image (scattering angle, dip angle, z, x) (auxiliary output file name)
Param:  hmax float  -   -  		Maximum allowed width of the receiver ray branch  
LDesc:  (defaults to: 20*fabsf (dh))
Param:  imap string  -   -  		Scattering gathers illumination (angle, z, x) (auxiliary output file name)
Param:  mute enum-bool  -  n 		y - mute signal in constant z plane before stacking 
Param:  oazmax float  -  180.0 		Maximum allowed scattering angle at z max 
Param:  oazmin float  -  180.0 		Maximum allowed scattering angle at z min 
Param:  smap string  -   -  		Scattering gathers semblance (angle, z, x) (auxiliary output file name)
Param:  smax float  -   -  		Maximum allowed width of the shot ray branch  
LDesc:  (defaults to: 10*fabsf (ds))
Param:  sqsmb enum-bool  -  n 		y - output energy traces instead of semblance 
Param:  th int  -  5 		Tapering length at the edges of the receiver direction 
Param:  ts int  -  3 		Tapering length at the edges of the source direction 
Param:  vconst float  -  1.5 		Constant velocity, if vz= is not used 
Param:  vz string  -   -  		Velocity model for amplitude weights (auxiliary input file name)

