sfmshots = rsf.doc.rsfprog('sfmshots','user/pyang/Mmshots.c','''2-D prestack forward modeling using sponge ABC using 4-th order FD''')
sfmshots.par('amp',rsf.doc.rsfpar('float','1000','','''maximum amplitude of ricker '''))
sfmshots.par('fm',rsf.doc.rsfpar('float','10','','''dominant freq of ricker '''))
sfmshots.par('nb',rsf.doc.rsfpar('int','30','','''thickness of sponge ABC  '''))
sfmshots.par('dt',rsf.doc.rsfpar('float','','','''time interval '''))
sfmshots.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sfmshots.par('ns',rsf.doc.rsfpar('int','','','''total shots '''))
sfmshots.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sfmshots.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sfmshots.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sfmshots.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sfmshots.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sfmshots.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sfmshots.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sfmshots.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sfmshots.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sfmshots.par('csdgather',rsf.doc.rsfpar('bool','n','','''default, common shot-gather; if n, record at every point'''))
sfmshots.version('1.7')
sfmshots.synopsis('''sfmshots < vinit.rsf > shots.rsf amp=1000 fm=10 nb=30 dt= nt= ns= ng= jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= csdgather=n''','''NB: prepare high quality prestack seismic data for LSRTM and FWI
Top boundary is free surface (no ABC applied)!
 ''')
rsf.doc.progs['sfmshots']=sfmshots

