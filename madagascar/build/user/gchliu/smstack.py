sfsmstack = rsf.doc.rsfprog('sfsmstack','user/gchliu/Msmstack.c','''Stack a dataset over the second dimensions by smart stacking. ''')
sfsmstack.par('s',rsf.doc.rsfpar('int','1','','''exponent'''))
sfsmstack.par('l',rsf.doc.rsfpar('int','0','','''parameter for alpha-trimmed mean '''))
sfsmstack.par('ifwt',rsf.doc.rsfpar('bool','y','',''''''))
sfsmstack.par('esp',rsf.doc.rsfpar('float','1e-10','',''''''))
sfsmstack.version('1.7')
sfsmstack.synopsis('''sfsmstack < in.rsf > out.rsf s=1 l=0 ifwt=y esp=1e-10''','''''')
rsf.doc.progs['sfsmstack']=sfsmstack

