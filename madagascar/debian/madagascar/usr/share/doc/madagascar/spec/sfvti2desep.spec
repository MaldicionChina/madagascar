[sfvti2desep]
Cat:    RSF/user/chengjb
Desc:   2-D two-components wavefield modeling using original elastic displacement wave equation in VTI media
DocCmd: sfvti2desep | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fvp0 data)
Port:   stdout rsf w req 	RSF standard output (containing Fo1 data)
Port:   ElasticSepP rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   ElasticSepSV rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Elasticz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apxs rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apxx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apxxs rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apzs rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apzz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   apzzs rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   del rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   epsi rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vs0 rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -  0.001 		
Param:  ihomo int  -  0 		if ihomo=1, homogeneous medium 
Param:  isep int  -  0 		if isep=1, separate wave-modes 
Param:  ns int  -  301 		
Param:  nstep int  -  1 		grid step to calculate operators: 1<=nstep<=5 
Param:  tapertype string  -   -  		taper type

