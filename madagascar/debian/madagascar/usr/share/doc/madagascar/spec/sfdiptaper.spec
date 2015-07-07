[sfdiptaper]
Cat:    RSF/user/aklokov
Desc:   Aperture optimization for migrated gathers in the dip-angle domain
DocCmd: sfdiptaper | cat
Port:   stdin  rsf r req 	RSF standard input (containing dipFile data)
Port:   stdout rsf w req 	RSF standard output (containing taperFile data)
Param:  dz float  -   -  		half of a migrated wave length 
LDesc:  (defaults to: 20.f)
Param:  greyarea float  -   -  		width of event tail taper (in degree) 
LDesc:  (defaults to: 10.f)

