[sfdagap]
Cat:    RSF/user/aklokov
Desc:   Reflection event apex protector/removal for dip-angle gathers
DocCmd: sfdagap | cat
Port:   stdin  rsf r req 	RSF standard input (containing dagFile data)
Port:   stdout rsf w req 	RSF standard output (containing taperFile data)
Param:  ddep enum-bool  -  y 		if y, taper depends on depth; if n, no 
Param:  dips string  -   -  		dips esitimated in the image domain (in degree) (auxiliary input file name)
Param:  dz float  -   -  		half of a migrated wave length 
LDesc:  (defaults to: 20.f)
Param:  greyarea float  -   -  		width of event tail taper (in degree) 
LDesc:  (defaults to: 10.f)
Param:  pwidth float  -   -  		protected width (in degree) 
LDesc:  (defaults to: 10.f)

