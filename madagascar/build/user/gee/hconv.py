sfhconv = rsf.doc.rsfprog('sfhconv','user/gee/Mhconv.c','''Convolution of two helix filters. ''')
sfhconv.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhconv.par('one',rsf.doc.rsfpar('bool','y','','''include leading one '''))
sfhconv.par('lag',rsf.doc.rsfpar('string ',desc=''''''))
sfhconv.version('1.7')
sfhconv.synopsis('''sfhconv < inp.rsf other=oth.rsf > out.rsf one=y lag=''','''''')
rsf.doc.progs['sfhconv']=sfhconv

