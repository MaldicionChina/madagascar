sfheat3 = rsf.doc.rsfprog('sfheat3','user/gee/Mheat3.c','''Finite-difference 3-D heat-flow equation using helix ''')
sfheat3.par('n3',rsf.doc.rsfpar('int','10','',''''''))
sfheat3.par('nh',rsf.doc.rsfpar('int','5','',''''''))
sfheat3.version('1.7')
sfheat3.synopsis('''sfheat3 > out.rsf n3=10 nh=5''','''''')
rsf.doc.progs['sfheat3']=sfheat3

