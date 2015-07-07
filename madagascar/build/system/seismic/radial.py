sfradial = rsf.doc.rsfprog('sfradial','system/seismic/Mradial.c','''Radial transform. ''')
sfradial.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfradial.par('nw',rsf.doc.rsfpar('int','2','','''accuracy level '''))
sfradial.par('tp',rsf.doc.rsfpar('float','t0','',''''''))
sfradial.par('xp',rsf.doc.rsfpar('float','0.','',''''''))
sfradial.par('nv',rsf.doc.rsfpar('int','','','''number of velocities (if inv=n) '''))
sfradial.par('vmin',rsf.doc.rsfpar('float','','','''minimum velocity (if inv=n) '''))
sfradial.par('vmax',rsf.doc.rsfpar('float','','','''maximum velocity (if inv=n) '''))
sfradial.version('1.7')
sfradial.synopsis('''sfradial < in.rsf > out.rsf inv=n nw=2 tp=t0 xp=0. nv= vmin= vmax=''','''''')
rsf.doc.progs['sfradial']=sfradial

