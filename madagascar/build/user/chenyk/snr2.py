sfsnr2 = rsf.doc.rsfprog('sfsnr2','user/chenyk/Msnr2.c','''Compute signal-noise-ratio.''')
sfsnr2.par('noise',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsnr2.version('1.7')
sfsnr2.synopsis('''sfsnr2 < signal.rsf noise=noise.rsf > snrf.rsf''','''SNR=10 log10(sum(clean)/sum(noise))''')
rsf.doc.progs['sfsnr2']=sfsnr2

