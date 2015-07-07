sfplane = rsf.doc.rsfprog('sfplane','user/fomels/Mplane.c','''Generating plane waves with steering filters. ''')
sfplane.par('p',rsf.doc.rsfpar('float','0.7','','''plane wave slope '''))
sfplane.par('a1',rsf.doc.rsfpar('int','2','','''filter length '''))
sfplane.par('b1',rsf.doc.rsfpar('int','1','','''denominator length '''))
sfplane.par('hyp',rsf.doc.rsfpar('bool','n','','''generate hyperbolas '''))
sfplane.par('lag',rsf.doc.rsfpar('string ',desc=''''''))
sfplane.version('1.7')
sfplane.synopsis('''sfplane < inp.rsf > out.rsf p=0.7 a1=2 b1=1 hyp=n lag=''','''''')
rsf.doc.progs['sfplane']=sfplane

