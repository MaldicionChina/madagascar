sffd2_10 = rsf.doc.rsfprog('sffd2_10','user/songxl/Mfd2_10.c','''2-D Fourth-order Optimized Finite-difference wave extrapolation ''')
sffd2_10.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffd2_10.par('dt',rsf.doc.rsfpar('float','','',''''''))
sffd2_10.par('nt',rsf.doc.rsfpar('int','','',''''''))
sffd2_10.par('isx',rsf.doc.rsfpar('int','','',''''''))
sffd2_10.par('isz',rsf.doc.rsfpar('int','','',''''''))
sffd2_10.version('1.7')
sffd2_10.synopsis('''sffd2_10 > out.rsf vel=vel.rsf < source.rsf dt= nt= isx= isz=''','''''')
rsf.doc.progs['sffd2_10']=sffd2_10

