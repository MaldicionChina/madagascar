sfchebvc = rsf.doc.rsfprog('sfchebvc','user/fomels/Mchebvc.c','''Post-stack 2-D velocity continuation by Chebyshev-tau method. ''')
sfchebvc.par('nv',rsf.doc.rsfpar('int','','',''''''))
sfchebvc.par('vel',rsf.doc.rsfpar('float','','',''''''))
sfchebvc.version('1.7')
sfchebvc.synopsis('''sfchebvc < in.rsf > out.rsf nv= vel=''','''''')
rsf.doc.progs['sfchebvc']=sfchebvc

