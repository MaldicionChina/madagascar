sftti2delrsep = rsf.doc.rsfprog('sftti2delrsep','user/chengjb/Mtti2delrsep.cc','''None''')
sftti2delrsep.par('ElasticSepP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrsep.par('ElasticSepSV',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrsep.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti2delrsep.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sftti2delrsep.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sftti2delrsep.par('ns',rsf.doc.rsfpar('','','',''''''))
sftti2delrsep.par('dt',rsf.doc.rsfpar('','','',''''''))
sftti2delrsep.version('1.7')
sftti2delrsep.synopsis('''sftti2delrsep < vp0.rsf > Elasticx.rsf ElasticSepP=ElasticSepP.rsf ElasticSepSV=ElasticSepSV.rsf seed=time(NULL eps=1.e-6 npk=20 ns= dt=''','''''')
rsf.doc.progs['sftti2delrsep']=sftti2delrsep

