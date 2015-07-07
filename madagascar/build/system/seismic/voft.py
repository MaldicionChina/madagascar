sfvoft = rsf.doc.rsfprog('sfvoft','system/seismic/Mvoft.c','''V(t) function for a linear V(Z) profile.''')
sfvoft.par('v0',rsf.doc.rsfpar('float','1.5','','''initial velocity '''))
sfvoft.par('alpha',rsf.doc.rsfpar('float','0.5','','''velocity gradient '''))
sfvoft.version('1.7')
sfvoft.synopsis('''sfvoft < in.rsf > out.rsf v0=1.5 alpha=0.5''','''''')
rsf.doc.progs['sfvoft']=sfvoft

