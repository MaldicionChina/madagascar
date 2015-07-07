sftti2dpseudoplrsep = rsf.doc.rsfprog('sftti2dpseudoplrsep','user/chengjb/Mtti2dpseudoplrsep.cc','''None''')
sftti2dpseudoplrsep.par('PseudoPureSepPx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudoplrsep.par('PseudoPureSepPz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudoplrsep.par('PseudoPureP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudoplrsep.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti2dpseudoplrsep.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sftti2dpseudoplrsep.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sftti2dpseudoplrsep.par('ns',rsf.doc.rsfpar('','','',''''''))
sftti2dpseudoplrsep.par('dt',rsf.doc.rsfpar('','','',''''''))
sftti2dpseudoplrsep.version('1.7')
sftti2dpseudoplrsep.synopsis('''sftti2dpseudoplrsep < vp0.rsf > PseudoPurePx.rsf PseudoPureSepPx=PseudoPureSepPx.rsf PseudoPureSepPz=PseudoPureSepPz.rsf PseudoPureP=PseudoPureP.rsf seed=time(NULL eps=1.e-6 npk=20 ns= dt=''','''''')
rsf.doc.progs['sftti2dpseudoplrsep']=sftti2dpseudoplrsep

