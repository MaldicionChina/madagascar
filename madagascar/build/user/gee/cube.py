sfcube = rsf.doc.rsfprog('sfcube','user/gee/Mcube.c','''Simple cube fault synthetic ''')
sfcube.par('n',rsf.doc.rsfpar('int','51','','''cube dimensions '''))
sfcube.par('p',rsf.doc.rsfpar('float','0.5','','''inline slope '''))
sfcube.par('q',rsf.doc.rsfpar('float','0.5','','''crossline slope '''))
sfcube.version('1.7')
sfcube.synopsis('''sfcube > cube.rsf n=51 p=0.5 q=0.5''','''''')
rsf.doc.progs['sfcube']=sfcube

