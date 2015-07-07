[sfgpurtm]
Cat:    RSF/user/pyang
Desc:   2D prestack GPU-based RTM using effective boundary saving
DocCmd: sfgpurtm | cat
Port:   stdin  rsf r req 	RSF standard input (containing vmodl data)
Port:   stdout rsf w req 	RSF standard output (containing imag1 data)
Port:   imag2 rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  csdgather enum-bool  -  y 		default, common shot-gather; if n, record at every point
Param:  dt float  -   -  		time interval 
Param:  fm float  -   -  		dominant freq of ricker 
Param:  gxbeg int  -   -  		x-begining index of receivers, starting from 0 
Param:  gzbeg int  -   -  		z-begining index of receivers, starting from 0 
Param:  jgx int  -  1 		receiver x-axis jump interval 
Param:  jgz int  -  0 		receiver z-axis jump interval 
Param:  jsx int  -   -  		source x-axis  jump interval  
Param:  jsz int  -  0 		source z-axis jump interval  
Param:  ng int  -   -  		total receivers in each shot 
Param:  ns int  -   -  		total shots 
Param:  nt int  -   -  		total modeling time steps 
Param:  order int  -  6 		order of finite difference, order=2,4,6,8,10 
Param:  phost float  -  0 		phost% points on host with zero-copy pinned memory, the rest on device 
Param:  sxbeg int  -   -  		x-begining index of sources, starting from 0 
Param:  szbeg int  -   -  		z-begining index of sources, starting from 0 
Param:  tdmute int  -   -  		number of deleyed time samples to mute 
LDesc:  (defaults to: 2.0/(fm*dt))
Param:  vmute float  -  1500 		muting velocity to remove the low-freq artifacts, unit=m/s

