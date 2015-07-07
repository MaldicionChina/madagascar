sfphaserot = rsf.doc.rsfprog('sfphaserot','user/fomels/Mphaserot.c','''Non-stationary phase rotation. ''')
sfphaserot.par('phase',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfphaserot.par('na',rsf.doc.rsfpar('int','721','','''number of angles '''))
sfphaserot.par('da',rsf.doc.rsfpar('float','1.0','','''angle increment '''))
sfphaserot.par('a0',rsf.doc.rsfpar('float','-360.','','''first angle '''))
sfphaserot.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order '''))
sfphaserot.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfphaserot.version('1.7')
sfphaserot.synopsis('''sfphaserot < inp.rsf phase=pha.rsf > out.rsf na=721 da=1.0 a0=-360. order=100 ref=1.''','''''')
rsf.doc.progs['sfphaserot']=sfphaserot

