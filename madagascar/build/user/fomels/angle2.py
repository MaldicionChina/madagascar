sfangle2 = rsf.doc.rsfprog('sfangle2','user/fomels/Mangle2.c','''Another illustration of angle gathers.''')
sfangle2.par('nx',rsf.doc.rsfpar('int','451','',''''''))
sfangle2.par('ny',rsf.doc.rsfpar('int','451','',''''''))
sfangle2.par('dx',rsf.doc.rsfpar('float','0.1','',''''''))
sfangle2.par('dy',rsf.doc.rsfpar('float','0.1','',''''''))
sfangle2.par('zx',rsf.doc.rsfpar('float','0.','',''''''))
sfangle2.par('zy',rsf.doc.rsfpar('float','0.','',''''''))
sfangle2.version('1.7 Mangle2.c 7107 2011-04-10 02:04:14Z ivlad')
sfangle2.synopsis('''sfangle2 > angle.rsf nx=451 ny=451 dx=0.1 dy=0.1 zx=0. zy=0.''','''''')
rsf.doc.progs['sfangle2']=sfangle2

