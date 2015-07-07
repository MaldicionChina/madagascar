sfexgr = rsf.doc.rsfprog('sfexgr','user/fomels/Mexgr.c','''Exact group velocity in VTI media ''')
sfexgr.par('aq',rsf.doc.rsfpar('float','14.47','',''''''))
sfexgr.par('bq',rsf.doc.rsfpar('float','2.28','',''''''))
sfexgr.par('cq',rsf.doc.rsfpar('float','9.57','',''''''))
sfexgr.par('dq',rsf.doc.rsfpar('float','4.51','',''''''))
sfexgr.version('1.7')
sfexgr.synopsis('''sfexgr > out.rsf aq=14.47 bq=2.28 cq=9.57 dq=4.51''','''''')
rsf.doc.progs['sfexgr']=sfexgr

