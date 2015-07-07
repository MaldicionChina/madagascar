sfocparcel = rsf.doc.rsfprog('sfocparcel','user/fomels/Mocparcel.c','''Patching test for out-of-core patching. ''')
sfocparcel.par('w',rsf.doc.rsfpar('ints','','',''' [dim]'''))
sfocparcel.par('k',rsf.doc.rsfpar('ints','','',''' [dim]'''))
sfocparcel.version('1.7 Mparcel.c 691 2004-07-04 19:28:08Z fomels')
sfocparcel.synopsis('''sfocparcel < in.rsf > out.rsf w= k=''','''''')
rsf.doc.progs['sfocparcel']=sfocparcel

