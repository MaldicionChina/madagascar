sfgpurtm = rsf.doc.rsfprog('sfgpurtm','user/pyang/Mgpurtm.cu','''2D prestack GPU-based RTM using effective boundary saving.''')
sfgpurtm.par('imag2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgpurtm.par('fm',rsf.doc.rsfpar('float','','','''dominant freq of ricker '''))
sfgpurtm.par('dt',rsf.doc.rsfpar('float','','','''time interval '''))
sfgpurtm.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sfgpurtm.par('ns',rsf.doc.rsfpar('int','','','''total shots '''))
sfgpurtm.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sfgpurtm.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sfgpurtm.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sfgpurtm.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sfgpurtm.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sfgpurtm.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sfgpurtm.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sfgpurtm.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sfgpurtm.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sfgpurtm.par('order',rsf.doc.rsfpar('int','6','','''order of finite difference, order=2,4,6,8,10 '''))
sfgpurtm.par('phost',rsf.doc.rsfpar('float','0','','''phost% points on host with zero-copy pinned memory, the rest on device '''))
sfgpurtm.par('csdgather',rsf.doc.rsfpar('bool','y','','''default, common shot-gather; if n, record at every point'''))
sfgpurtm.par('vmute',rsf.doc.rsfpar('float','1500','','''muting velocity to remove the low-freq artifacts, unit=m/s'''))
sfgpurtm.par('tdmute',rsf.doc.rsfpar('int','2.0/(fm*dt)','','''number of deleyed time samples to mute '''))
sfgpurtm.version('1.7')
sfgpurtm.synopsis('''sfgpurtm < vmodl.rsf > imag1.rsf imag2=imag2.rsf fm= dt= nt= ns= ng= jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= order=6 phost=0 csdgather=y vmute=1500 tdmute=2.0/(fm*dt)''','''
Some basic descriptions of this code are in order.
1) Coordinate configuration of seismic data:

		o--------------> x (2nd dim: *.y)
		|
		|
		|
		|
		|
		z (1st dim: *.x)
	1st dim: i1=threadIdx.x+blockDim.x*blockIdx.x;
	2nd dim: i2=threadIdx.y+blockDim.y*blockIdx.y;
	(i1, i2)=i1+i2*nnz;

2) stability condition:	
	min(dx, dz)>sqrt(2)*dt*max(v) (NJ=2)
   numerical dispersion condition:	
	max(dx, dz)<min(v)/(10*fmax)  (NJ=2)
	max(dx, dz)<min(v)/(5*fmax)   (NJ=4)

3) This code doesn't save the history of forward time steps. We 
   just save the least boundaries (referred to as effective boundary 
   in our work) of every time step and the two final steps of the 
   wavefield. Using this information, we can easily reconstruct 
   the exact wavefield in the reverse time steps. It is noteworthy
   that to implement large scale seismic imaging, pinned memory is 
   employed to save the boundaries of each step so that all the saved
   data can be computed on the device directly.

4) In our implementation, we employ staggered grid based 
   convolutional PML (CPML) boundary condition. Using 20 points for 
   CPML is enough to obtain perfect absorbing effect (while commonly 
   used sponge ABC may need 30 or more). However, we use 32 points on
   each side due to the grid alignment reasons. (To make your code 
   fast, you should consider that the GPU codes implementation unit 
   is half-warp (16 threads). The thickness of the boundary should be 
   times of 16. 

5) The final images can be two kinds: result of correlation imaging 
   condition and the normalized one. The normalized correlation imaging
   result is preferred due to compensated illumination. Some filters 
   are popular and effective to remove the low frequency artifacts of 
   the imaging: the Laplacian filtering, derivative filtering and 
   the bandpass filtering. In this code, we use laplacian filtering.
''')
rsf.doc.progs['sfgpurtm']=sfgpurtm

