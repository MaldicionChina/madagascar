sfpef = rsf.doc.rsfprog('sfpef','su/main/pef.c','''Wiener predictive error filtering ''')
sfpef.par('wiener',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpef.par('mix',rsf.doc.rsfpar('floats','','','''weights for moving average of the autocorrelations  [nmix]'''))
sfpef.par('minlag',rsf.doc.rsfpar('float','','','''first lag of prediction filter (sec) '''))
sfpef.par('maxlag',rsf.doc.rsfpar('float','','','''last lag of prediction filter (sec) '''))
sfpef.par('pnoise',rsf.doc.rsfpar('float','0.001','','''relative additive noise level '''))
sfpef.par('nmix',rsf.doc.rsfpar('int','1','','''number of weights (floats) for moving averages '''))
sfpef.par('mincorr',rsf.doc.rsfpar('float','','','''start of autocorrelation window in sec '''))
sfpef.par('maxcorr',rsf.doc.rsfpar('float','','','''end of autocorrelation window in sec '''))
sfpef.par('wiener',rsf.doc.rsfpar('string ',desc='''file to output Wiener filter (auxiliary output file name)'''))
sfpef.version('1.7')
sfpef.synopsis('''sfpef < inp.rsf > out.rsf wiener=wien.rsf mix= minlag= maxlag= pnoise=0.001 nmix=1 mincorr= maxcorr=''','''''')
rsf.doc.progs['sfpef']=sfpef

