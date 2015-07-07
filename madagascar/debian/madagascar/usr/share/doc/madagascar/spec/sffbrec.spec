[sffbrec]
Cat:    RSF/user/pyang
Desc:   Forward-backword exact reconstruction using boundary saving
DocCmd: sffbrec | cat
Port:   stdin  rsf r req 	RSF standard input (containing vinit data)
Port:   stdout rsf w req 	RSF standard output (containing Fw1 data)
Port:   back rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  amp float  -  1000 		maximum amplitude of ricker 
Param:  csdgather enum-bool  -  y 		default, common shot-gather; if n, record at every point
Param:  dt float  -   -  		time interval 
Param:  fm float  -  10 		dominant freq of ricker 
Param:  ft int  -  0 		first recorded time 
Param:  gxbeg int  -   -  		x-begining index of receivers, starting from 0 
Param:  gzbeg int  -   -  		z-begining index of receivers, starting from 0 
Param:  jgx int  -  1 		receiver x-axis jump interval 
Param:  jgz int  -  0 		receiver z-axis jump interval 
Param:  jsx int  -   -  		source x-axis  jump interval  
Param:  jsz int  -  0 		source z-axis jump interval  
Param:  jt int  -  1 		time interval 
Param:  ng int  -   -  		total receivers in each shot 
Param:  ns int  -  1 		total shots 
Param:  nt int  -   -  		total modeling time steps 
Param:  sxbeg int  -   -  		x-begining index of sources, starting from 0 
Param:  szbeg int  -   -  		z-begining index of sources, starting from 0 

