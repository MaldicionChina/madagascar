[sftahnmo]
Cat:    RSF/user/karl
Desc:   Trace And Header Normal MoveOut
DocCmd: sftahnmo | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  inv enum-bool  -  n 		if y, do inverse nmo.  Otherwise forward nmo 
Param:  lmute float  -   -  		length of the mute zone in seconds 
LDesc:  (defaults to: 12.*d1)
Param:  str float  -  0.5 		maximum stretch allowed 
Param:  tnmo float-list  -   -  		list of NMO times for the vnmo velocities.  [numtnmo]
Param:  verbose int  -  1 		
LDesc:  
LDesc:       flag to control amount of print
LDesc:       0 terse, 1 informative, 2 chatty, 3 debug
LDesc:    
Param:  vnmo float-list  -   -  		list of NMO velocities for the tnmo times.  [numvnmo]

