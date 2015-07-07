[sfffd0]
Cat:    RSF/user/songxl
Desc:   2-D FFD zero-offset migration: MPI + OMP
DocCmd: sfffd0 | cat
Port:   stdin  rsf r req 	RSF standard input (containing source data)
Port:   stdout rsf w req 	RSF standard output (containing output data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  alpha float  -  -0.7 		
Param:  ax float  -  2.0 		suppress HF parameter
Param:  az float  -  2.0 		suppress HF parameter
Param:  cb float  -  0.01 		decaying parameter
Param:  cl float  -  0.01 		decaying parameter
Param:  cr float  -  0.01 		decaying parameter
Param:  ct float  -  0.01 		decaying parameter
Param:  err float  -  0.00001 		
Param:  factor float  -  2.0/3.0 		suppress HF parameter
Param:  jm int  -  20 		
Param:  jr int  -  1 		
Param:  nbb int  -  44 		
Param:  nbl int  -  44 		
Param:  nbr int  -  44 		
Param:  nbt int  -  44 		
Param:  opt enum-bool  -  y 		
Param:  r0 int  -  0 		

