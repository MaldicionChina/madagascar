[sfewefd3d_multiNode]
Cat:    RSF/user/rweiss
Desc:   3D elastic time-domain FD modeling with multiple GPUs coordinated via MPI and p2p
DocCmd: sfewefd3d_multiNode | cat
Port:   stdout rsf w req 	RSF standard output (containing Fdat data)
Port:   ccc rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   um rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   uo rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wav rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dabc enum-bool  -  n 		absorbing BC 
Param:  free enum-bool  -  n 		free surface flag 
Param:  interp enum-bool  -  y 		perform linear interpolation on receiver locations 
Param:  jdata int  -  1 		extract receiver data every jdata time steps 
Param:  jsnap int  -   -  		save wavefield every jsnap time steps 
LDesc:  (defaults to: nt)
Param:  nbell int  -  5 		bell size 
Param:  ngpu int  -  1 		Number of GPUs in each node, must be set to lowest common number of GPUs
Param:  snap enum-bool  -  n 		wavefield snapshots flag 
Param:  ssou enum-bool  -  n 		stress source 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  wavSrc enum-bool  -  y 		if yes, look for a source wavelet.  if no, look for initial displacement fields (uo and um) 

