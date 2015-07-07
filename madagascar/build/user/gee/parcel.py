sfparcel = rsf.doc.rsfprog('sfparcel','user/gee/Mparcel.c','''Patching test.''')
sfparcel.par('w',rsf.doc.rsfpar('ints','','',''' [dim]'''))
sfparcel.par('k',rsf.doc.rsfpar('ints','','',''' [dim]'''))
sfparcel.version('1.7 Mparcel.c 4796 2009-09-29 19:39:07Z ivlad')
sfparcel.synopsis('''sfparcel < in.rsf > out.rsf w= k=''','''''')
rsf.doc.progs['sfparcel']=sfparcel

