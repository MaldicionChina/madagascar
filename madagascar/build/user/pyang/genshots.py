sfgenshots = rsf.doc.rsfprog('sfgenshots','user/pyang/Mgenshots.cu','''Generate shots for FWI using Enquist absorbing boundary condition''')
sfgenshots.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgenshots.par('check',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgenshots.par('chk',rsf.doc.rsfpar('bool','n','','''check whether GPU-CPU implementation coincide with each other or not '''))
sfgenshots.par('kt',rsf.doc.rsfpar('int','100','','''check it at it=100 '''))
sfgenshots.par('amp',rsf.doc.rsfpar('float','1000','','''maximum amplitude of ricker '''))
sfgenshots.par('fm',rsf.doc.rsfpar('float','10','','''dominant freq of ricker '''))
sfgenshots.par('dt',rsf.doc.rsfpar('float','','','''time interval '''))
sfgenshots.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sfgenshots.par('ns',rsf.doc.rsfpar('int','','','''total shots '''))
sfgenshots.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sfgenshots.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sfgenshots.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sfgenshots.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sfgenshots.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sfgenshots.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sfgenshots.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sfgenshots.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sfgenshots.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sfgenshots.par('csdgather',rsf.doc.rsfpar('bool','n','','''default, common shot-gather; if n, record at every point'''))
sfgenshots.version('1.7')
sfgenshots.synopsis('''sfgenshots < vinit.rsf > shots.rsf time=time.rsf check=check.rsf chk=n kt=100 amp=1000 fm=10 dt= nt= ns= ng= jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= csdgather=n''','''
Note: 	You can try other complex boundary condition but we do not
	recommend to do so. The main reason is that FWI is to recover
	the low-frequency information of the earth model. Low-freq 
	means that exact absorbing is not necessarilly needed. The 
	result will be improved with the optimization procedure. 
	Furthermore, complex boundary condition (such as sponge ABC or
	PML) implies more computational cost, which will degrade the
	efficiency of FWI. 
''')
rsf.doc.progs['sfgenshots']=sfgenshots

