sfwcorr = rsf.doc.rsfprog('sfwcorr','user/gchliu/Mwcorr.c','''Stack a dataset over the second dimensions by SNR weighted method. ''')
sfwcorr.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwcorr.par('w',rsf.doc.rsfpar('int','50','','''size of window'''))
sfwcorr.par('eps',rsf.doc.rsfpar('float','0','','''stable parameter'''))
sfwcorr.version('1.7')
sfwcorr.synopsis('''sfwcorr < in.rsf other=other.rsf > out.rsf w=50 eps=0''','''''')
rsf.doc.progs['sfwcorr']=sfwcorr

