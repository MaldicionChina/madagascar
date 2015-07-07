sfconflict = rsf.doc.rsfprog('sfconflict','user/gee/Mconflict.c','''2-D synthetic data of conflicting dips. ''')
sfconflict.par('n1',rsf.doc.rsfpar('int','150','',''''''))
sfconflict.par('n2',rsf.doc.rsfpar('int','80','',''''''))
sfconflict.version('1.7 Mconflict.c 1659 2005-12-16 09:40:21Z fomels')
sfconflict.synopsis('''sfconflict > mod.rsf n1=150 n2=80''','''''')
rsf.doc.progs['sfconflict']=sfconflict

