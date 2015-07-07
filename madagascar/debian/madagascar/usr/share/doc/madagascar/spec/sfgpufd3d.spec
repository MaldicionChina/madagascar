[sfgpufd3d]
Cat:    RSF/user/pyang
Desc:   GPU-based finite difference on 3-D grid
DocCmd: sfgpufd3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fv data)
Port:   stdout rsf w req 	RSF standard output (containing Fw data)
Param:  dt float  -   -  		time sampling interval 
Param:  fm float  -  20 		dominant frequency of Ricker wavelet 
Param:  jsx int  -   -  		source jump interval in x-axis 
Param:  jsy int  -   -  		source jump interval in y-axis 
Param:  jsz int  -   -  		source jump interval in z-axis 
Param:  kt int  -   -  		record wavefield at time kt 
Param:  ns int  -  1 		number of sources 
Param:  nt int  -   -  		total number of time steps 
Param:  sxbeg int  -   -  		source beginning of x-axis 
Param:  sybeg int  -   -  		source beginning of y-axis 
Param:  szbeg int  -   -  		source beginning of z-axis 
Param:  verb enum-bool  -  n 		verbosit2 

