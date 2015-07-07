sfinfill = rsf.doc.rsfprog('sfinfill','system/seismic/Minfill.c','''Shot interpolation. ''')
sfinfill.par('eps',rsf.doc.rsfpar('float','0.1','','''regularization parameter '''))
sfinfill.par('positive',rsf.doc.rsfpar('bool','y','','''initial offset orientation '''))
sfinfill.version('1.7')
sfinfill.synopsis('''sfinfill < in.rsf > out.rsf eps=0.1 positive=y''','''''')
rsf.doc.progs['sfinfill']=sfinfill

