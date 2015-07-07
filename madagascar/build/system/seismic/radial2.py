sfradial2 = rsf.doc.rsfprog('sfradial2','system/seismic/Mradial2.c','''Another version of radial transform. ''')
sfradial2.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfradial2.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfradial2.par('tp',rsf.doc.rsfpar('float','t0','',''''''))
sfradial2.par('nv',rsf.doc.rsfpar('int','','','''number of velocities (if inv=n) '''))
sfradial2.par('vmin',rsf.doc.rsfpar('float','','','''minimum velocity (if inv=n) '''))
sfradial2.par('vmax',rsf.doc.rsfpar('float','','','''maximum velocity (if inv=n) '''))
sfradial2.version('1.7')
sfradial2.synopsis('''sfradial2 < in.rsf > out.rsf inv=n eps=0.01 tp=t0 nv= vmin= vmax=''','''''')
rsf.doc.progs['sfradial2']=sfradial2

