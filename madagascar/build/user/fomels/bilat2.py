sfbilat2 = rsf.doc.rsfprog('sfbilat2','user/fomels/Mbilat2.c','''2-D bilateral filtering ''')
sfbilat2.par('r1',rsf.doc.rsfpar('int','1','','''vertical smoothing radius '''))
sfbilat2.par('r2',rsf.doc.rsfpar('int','1','','''horizontal smoothing radius '''))
sfbilat2.par('a1',rsf.doc.rsfpar('float','0.0f','','''vertical attenuation factor '''))
sfbilat2.par('a2',rsf.doc.rsfpar('float','a1','','''horizontal attenuation factor '''))
sfbilat2.par('a3',rsf.doc.rsfpar('float','0.0f','','''data attenuation factor '''))
sfbilat2.par('repeat',rsf.doc.rsfpar('int','1','','''repeat the operation '''))
sfbilat2.version('1.7')
sfbilat2.synopsis('''sfbilat2 < inp.rsf > out.rsf r1=1 r2=1 a1=0.0f a2=a1 a3=0.0f repeat=1''','''''')
rsf.doc.progs['sfbilat2']=sfbilat2

