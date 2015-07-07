sfenoint2 = rsf.doc.rsfprog('sfenoint2','system/generic/Menoint2.c','''ENO interpolation in 2-D slices. ''')
sfenoint2.par('head',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfenoint2.par('xkey',rsf.doc.rsfpar('int','','','''x key number '''))
sfenoint2.par('ykey',rsf.doc.rsfpar('int','','','''y key number '''))
sfenoint2.par('interp',rsf.doc.rsfpar('int','2','','''interpolation order '''))
sfenoint2.version('1.7 Mbin.c 847 2004-10-27 20:33:16Z fomels')
sfenoint2.synopsis('''sfenoint2 < in.rsf > out.rsf head=head.rsf xkey= ykey= interp=2''','''''')
rsf.doc.progs['sfenoint2']=sfenoint2

