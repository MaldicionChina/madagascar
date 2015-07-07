sfautocorr = rsf.doc.rsfprog('sfautocorr','user/gee/Mautocorr.c','''Autocorrelation for helix filters. ''')
sfautocorr.par('lag',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfautocorr.par('lagout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfautocorr.par('lag',rsf.doc.rsfpar('string ',desc='''optional input file with filter lags (auxiliary input file name)'''))
sfautocorr.par('lagout',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfautocorr.version('1.7 Mautocorr.c 7107 2011-04-10 02:04:14Z ivlad')
sfautocorr.synopsis('''sfautocorr < in.rsf > out.rsf lag=lag0.rsf lagout=lag.rsf''','''''')
rsf.doc.progs['sfautocorr']=sfautocorr

