sfhole = rsf.doc.rsfprog('sfhole','user/gee/Mhole.c','''Cut an elliptic hole in data (for interpolation tests).''')
sfhole.par('maskout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfhole.version('1.7 Mhole.c 7107 2011-04-10 02:04:14Z ivlad')
sfhole.synopsis('''sfhole < in.rsf > out.rsf maskout=mask.rsf''','''''')
rsf.doc.progs['sfhole']=sfhole

