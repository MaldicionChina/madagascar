sfvam = rsf.doc.rsfprog('sfvam','user/hpcss/Mvam.c','''Create a layered model. ''')
sfvam.par('nz',rsf.doc.rsfpar('int','','','''depth grid '''))
sfvam.par('nx',rsf.doc.rsfpar('int','','','''distance grid '''))
sfvam.par('dz',rsf.doc.rsfpar('float','','','''depth sampling '''))
sfvam.par('dx',rsf.doc.rsfpar('float','','','''distance sampling '''))
sfvam.version('1.7')
sfvam.synopsis('''sfvam > vfile.rsf nz= nx= dz= dx=''','''''')
rsf.doc.progs['sfvam']=sfvam

