sftan2ang = rsf.doc.rsfprog('sftan2ang','system/seismic/Mtan2ang.c','''tangent to angle transformation ''')
sftan2ang.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftan2ang.par('na',rsf.doc.rsfpar('int','nt','',''''''))
sftan2ang.par('da',rsf.doc.rsfpar('float','90/(nt-1)','',''''''))
sftan2ang.par('a0',rsf.doc.rsfpar('float','0.','',''''''))
sftan2ang.par('extend',rsf.doc.rsfpar('int','4','','''tmp extension '''))
sftan2ang.par('top',rsf.doc.rsfpar('bool','n','',''''''))
sftan2ang.version('1.7')
sftan2ang.synopsis('''sftan2ang < Fstk.rsf > Fang.rsf velocity=velocity.rsf na=nt da=90/(nt-1) a0=0. extend=4 top=n''','''''')
rsf.doc.progs['sftan2ang']=sftan2ang

