[sfvti2dpseudop1]
Cat:    RSF/user/chengjb
Desc:   2-D two-components wavefield modeling using pseudo-pure mode P-wave equation in VTI media
DocCmd: sfvti2dpseudop1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fvp0 data)
Port:   stdout rsf w req 	RSF standard output (containing Fo1 data)
Port:   PseudoPureP rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   PseudoPurePz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   PseudoPureSepP rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   adx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   adxx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   adz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   adzz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apvx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apvxx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apvz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apvzz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apxx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apzz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   del rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   epsi rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vs0 rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -  0.001 		
Param:  ihomo int  -  0 		if ihomo=1, homogeneous medium 
Param:  isep int  -  0 		if isep=1, separate wave-modes 
Param:  itaper int  -  0 		if itaper=1, taper the wavenumber domain p=operators
Param:  ns int  -  301 		
Param:  nstep int  -  2 		
Param:  tapertype string  -   -  		taper type

