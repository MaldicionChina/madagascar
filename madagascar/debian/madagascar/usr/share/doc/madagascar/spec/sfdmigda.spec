[sfdmigda]
Cat:    RSF/user/aklokov
Desc:   2D depth scattering-angle Kirchhoff migration
DocCmd: sfdmigda | cat
Port:   stdin  rsf r req 	RSF standard input (containing dataFile data)
Port:   stdout rsf w req 	RSF standard output (containing imageFile data)
Param:  axis2label int  -  0 		0 - shot; 1 - cmp; 2 - receiver 
Param:  cig string  -   -  		output file containing CIGs in the scattering-angle domain (auxiliary output file name)
Param:  dag string  -   -  		output file containing CIGs in the dip-angle domain (auxiliary output file name)
Param:  dipd float  -   -  		step in dip-angle 
LDesc:  (defaults to: 1.f)
Param:  dipn int  -  161 		number of dip-angles 
Param:  dipo float  -   -  		first dip-angle 
LDesc:  (defaults to: -80.f)
Param:  esct string  -   -  		output file containing escqpe times (auxiliary output file name)
Param:  escx string  -   -  		output file containing escape positions (auxiliary output file name)
Param:  isAA enum-bool  -  y 		if y, apply anti-aliasing 
Param:  iscatd float  -   -  		scattering-angle increment (in degree) 
LDesc:  (defaults to: 2 * gp.dipStep)
Param:  iscatn int  -  1 		number of scattering-angles 
Param:  iscato float  -   -  		first scattering-angle (in degree) 
LDesc:  (defaults to: 0.f)
Param:  ixd float  -   -  		step in inlines (in meters) 
LDesc:  (defaults to: dp.xStep)
Param:  ixn int  -   -  		number of imaged inlines 
LDesc:  (defaults to: dp.xNum)
Param:  ixo float  -   -  		first imaged inline (in meters) 
LDesc:  (defaults to: dp.xStart)
Param:  iyd float  -   -  		step in crosslines (in meters) 
LDesc:  (defaults to: dp.yStep)
Param:  iyn int  -   -  		number of imaged crosslines 
LDesc:  (defaults to: rp.is3D ? vp.yNum : 1)
Param:  iyo float  -   -  		first imaged crossline (in meters) 
LDesc:  (defaults to: dp.yStart)
Param:  izd float  -   -  		step in depth (in meters) 
LDesc:  (defaults to: dp.zStep)
Param:  izn int  -   -  		number of imaged depth samples 
LDesc:  (defaults to: dp.zNum)
Param:  izo float  -   -  		first imaged depth (in meters) 
LDesc:  (defaults to: dp.zStart)
Param:  mcig string  -   -  		output file containing multi-CIGs (in the dip-angle and the scattering-angle domain both (auxiliary output file name)
Param:  ttd float  -   -  		travel-times increment 
LDesc:  (defaults to: 0.002f)
Param:  ttn int  -   -  		travel-times number 
LDesc:  (defaults to: (int) floor(0.001 * 0.5 * maxTime / ttStep + 1))
Param:  ttrayd float  -   -  		travel-times rays increment 
LDesc:  (defaults to: gp.dipStep / 2.f)
Param:  ttrayn int  -   -  		travel-times rays number 
LDesc:  (defaults to: (int) floor((maxttRay - minttRay) / ttRayStep + 1))
Param:  ttrayo float  -   -  		travel-times rays start 
LDesc:  (defaults to: minttRay)
Param:  vel string  -   -  		velocity model file (velocity in m/s) (auxiliary input file name)

