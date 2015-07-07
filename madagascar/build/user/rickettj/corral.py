sfcorral = rsf.doc.rsfprog('sfcorral','user/rickettj/Mcorral.c','''Cross-correlate every trace with every other in frequency domain. ''')
sfcorral.par('nlags',rsf.doc.rsfpar('int','100','','''number of lags '''))
sfcorral.version('1.7')
sfcorral.synopsis('''sfcorral < inp.rsf > out.rsf nlags=100''','''''')
rsf.doc.progs['sfcorral']=sfcorral

