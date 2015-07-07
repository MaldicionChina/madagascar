sftti2delrdecomp = rsf.doc.rsfprog('sftti2delrdecomp','user/chengjb/Mtti2delrdecomp.cc','''None''')
sftti2delrdecomp.par('ElasticPx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp.par('ElasticPz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp.par('ElasticSVx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp.par('ElasticSVz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2delrdecomp.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sftti2delrdecomp.par('eps',rsf.doc.rsfpar('','1.e-6','','''tolerance'''))
sftti2delrdecomp.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sftti2delrdecomp.par('ns',rsf.doc.rsfpar('','','',''''''))
sftti2delrdecomp.par('dt',rsf.doc.rsfpar('','','',''''''))
sftti2delrdecomp.version('1.7')
sftti2delrdecomp.synopsis('''sftti2delrdecomp < vp0.rsf > Elasticx.rsf ElasticPx=ElasticPx.rsf ElasticPz=ElasticPz.rsf ElasticSVx=ElasticSVx.rsf ElasticSVz=ElasticSVz.rsf seed=time(NULL eps=1.e-6 npk=20 ns= dt=''','''''')
rsf.doc.progs['sftti2delrdecomp']=sftti2delrdecomp

