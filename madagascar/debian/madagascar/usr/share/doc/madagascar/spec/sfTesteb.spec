[sfTesteb]
Cat:    RSF/user/pyang
Desc:   Demo for effective boundary saving in regular grid
DocCmd: sfTesteb | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fv data)
Port:   stdout rsf w req 	RSF standard output (containing Fw1 data)
Port:   back rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt float  -   -  		time sampling interval 
Param:  fm float  -  20.0 		dominant freq of Ricker wavelet 
Param:  ft int  -  0 		first recorded time 
Param:  jt int  -  1 		time interval 
Param:  nb int  -  20 		thickness of sponge ABC 
Param:  ng int  -   -  		number of receivers 
LDesc:  (defaults to: nx)
Param:  ns int  -  1 		number of shots 
Param:  nt int  -   -  		number of time steps 

