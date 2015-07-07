sfmysnr = rsf.doc.rsfprog('sfmysnr','user/pyang/Mmysnr.c','''print out signal-to-noise ratio in decibel (dB)''')
sfmysnr.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmysnr.version('1.7')
sfmysnr.synopsis('''sfmysnr < in.rsf ref=ref.rsf > out.rsf''','''''')
rsf.doc.progs['sfmysnr']=sfmysnr

