sfsynmarine = rsf.doc.rsfprog('sfsynmarine','user/gee/Msynmarine.c','''Simple synthetic marine data example. ''')
sfsynmarine.par('nt',rsf.doc.rsfpar('int','250','','''time samples '''))
sfsynmarine.par('nh',rsf.doc.rsfpar('int','48','','''offset samples '''))
sfsynmarine.par('ny',rsf.doc.rsfpar('int','10','','''midpoint samples '''))
sfsynmarine.par('nz',rsf.doc.rsfpar('int','25','','''depth samples '''))
sfsynmarine.version('1.7 Msynmarine.c 7107 2011-04-10 02:04:14Z ivlad')
sfsynmarine.synopsis('''sfsynmarine > out.rsf nt=250 nh=48 ny=10 nz=25''','''''')
rsf.doc.progs['sfsynmarine']=sfsynmarine

