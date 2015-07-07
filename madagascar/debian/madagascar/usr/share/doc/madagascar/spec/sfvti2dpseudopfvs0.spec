[sfvti2dpseudopfvs0]
Cat:    RSF/user/chengjb
Desc:   2-D two-components wavefield modeling using pseudo-pure mode P-wave equation in VTI media
DocCmd: sfvti2dpseudopfvs0 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fvp0 data)
Port:   stdout rsf w req 	RSF standard output (containing Fo1 data)
Port:   Fvs0 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   PseudoPureP rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   PseudoPurePz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   PseudoPureSepP rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apvx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apvxx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apvz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apvzz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   del rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   epsi rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -  0.001 		
Param:  ihomo int  -  0 		if ihomo=1, homogeneous medium 
Param:  isep int  -  0 		if isep=1, separate wave-modes 
Param:  itaper int  -  0 		if itaper=1, taper the operator 
Param:  ns int  -  301 		
Param:  nstep int  -  1 		grid step to calculate operators: 1<=nstep<=5 
Param:  tapertype string  -   -  		taper type

