sfmake = rsf.doc.rsfprog('sfmake','user/gee/Mmake.c','''Simple 2-D synthetics with crossing plane waves.''')
sfmake.par('n1',rsf.doc.rsfpar('int','100','',''''''))
sfmake.par('n2',rsf.doc.rsfpar('int','14','',''''''))
sfmake.par('n3',rsf.doc.rsfpar('int','1','','''dimensions '''))
sfmake.par('second',rsf.doc.rsfpar('bool','y','','''if n, only one plane wave is modeled '''))
sfmake.par('n',rsf.doc.rsfpar('int','3','',''''''))
sfmake.par('p',rsf.doc.rsfpar('int','3','',''''''))
sfmake.par('t1',rsf.doc.rsfpar('int','4','','''triangle smoother for first wave '''))
sfmake.par('t2',rsf.doc.rsfpar('int','4','','''triangle smoother for second wave '''))
sfmake.version('1.7 Mmake.c 7267 2011-06-13 18:38:18Z saragiotis')
sfmake.synopsis('''sfmake > mod.rsf n1=100 n2=14 n3=1 second=y n=3 p=3 t1=4 t2=4''','''''')
rsf.doc.progs['sfmake']=sfmake

