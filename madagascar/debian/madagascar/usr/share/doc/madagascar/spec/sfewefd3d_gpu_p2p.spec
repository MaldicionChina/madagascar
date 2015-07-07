[sfewefd3d_gpu_p2p]
Cat:    RSF/user/rweiss
Desc:   3D elastic time-domain FD modeling with GPU (For use in single node with one or more GPUs)
DocCmd: sfewefd3d_gpu_p2p | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwav data)
Port:   stdout rsf w req 	RSF standard output (containing Fdat data)
Port:   ccc rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dabc enum-bool  -  n 		absorbing BC 
Param:  free enum-bool  -  n 		free surface flag 
Param:  interp enum-bool  -  y 		perform linear interpolation on receiver data 
Param:  jdata int  -  1 		extract receiver data every jdata time steps 
Param:  jsnap int  -   -  		save wavefield every jsnap time steps 
LDesc:  (defaults to: nt)
Param:  nbell int  -  5 		bell size 
Param:  ngpu int  -  1 		how many local GPUs to use 
Param:  snap enum-bool  -  n 		wavefield snapshots flag 
Param:  ssou enum-bool  -  n 		stress source 
Param:  verb enum-bool  -  n 		verbosity flag 

