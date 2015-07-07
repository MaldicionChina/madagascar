sfangle = rsf.doc.rsfprog('sfangle','user/fomels/Mangle.c','''Illustration of angle gathers.''')
sfangle.par('nw',rsf.doc.rsfpar('int','513','',''''''))
sfangle.par('nm',rsf.doc.rsfpar('int','257','',''''''))
sfangle.par('nh',rsf.doc.rsfpar('int','257','',''''''))
sfangle.par('dw',rsf.doc.rsfpar('float','1./(2*(nw-1)*0.004)','',''''''))
sfangle.par('dm',rsf.doc.rsfpar('float','1./(2*(nm-1)*0.01)','',''''''))
sfangle.par('dh',rsf.doc.rsfpar('float','1./(2*(nh-1)*0.01)','',''''''))
sfangle.par('w0',rsf.doc.rsfpar('float','dw','',''''''))
sfangle.par('vel',rsf.doc.rsfpar('float','2.','',''''''))
sfangle.version('1.7 Mangle.c 7884 2011-11-17 02:52:47Z sfomel')
sfangle.synopsis('''sfangle > angle.rsf nw=513 nm=257 nh=257 dw=1./(2*(nw-1)*0.004) dm=1./(2*(nm-1)*0.01) dh=1./(2*(nh-1)*0.01) w0=dw vel=2.''','''''')
rsf.doc.progs['sfangle']=sfangle

