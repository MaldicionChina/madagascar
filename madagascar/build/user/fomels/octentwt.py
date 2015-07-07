sfoctentwt = rsf.doc.rsfprog('sfoctentwt','user/fomels/Moctentwt.c','''Tent-like weight for out-of-core patching. ''')
sfoctentwt.par('windwt',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfoctentwt.par('w',rsf.doc.rsfpar('ints','','','''window size  [dim]'''))
sfoctentwt.par('k',rsf.doc.rsfpar('ints','','','''number of windows  [dim]'''))
sfoctentwt.par('a',rsf.doc.rsfpar('ints','','','''filter size  [dim]'''))
sfoctentwt.par('center',rsf.doc.rsfpar('ints','','',''' [dim]'''))
sfoctentwt.par('dim',rsf.doc.rsfpar('int','2','','''number of dimensions '''))
sfoctentwt.version('1.7 Mtentwt.c 691 2004-07-04 19:28:08Z fomels')
sfoctentwt.synopsis('''sfoctentwt > wallwt.rsf windwt=windwt.rsf w= k= a= center= dim=2''','''''')
rsf.doc.progs['sfoctentwt']=sfoctentwt

