sffd2bs = rsf.doc.rsfprog('sffd2bs','user/songxl/Mfd2bs.c','''2-D Fourth-order Finite-difference wave extrapolation ''')
sffd2bs.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffd2bs.par('opt',rsf.doc.rsfpar('bool','y','','''if y, determine optimal size for efficiency '''))
sffd2bs.par('dt',rsf.doc.rsfpar('float','','',''''''))
sffd2bs.par('nt',rsf.doc.rsfpar('int','','',''''''))
sffd2bs.par('isx',rsf.doc.rsfpar('int','','',''''''))
sffd2bs.par('isz',rsf.doc.rsfpar('int','','',''''''))
sffd2bs.par('nb',rsf.doc.rsfpar('int','30','',''''''))
sffd2bs.par('c',rsf.doc.rsfpar('float','0.01','','''decaying parameter'''))
sffd2bs.version('1.7')
sffd2bs.synopsis('''sffd2bs > out.rsf vel=vel.rsf < source.rsf opt=y dt= nt= isx= isz= nb=30 c=0.01''','''''')
rsf.doc.progs['sffd2bs']=sffd2bs

