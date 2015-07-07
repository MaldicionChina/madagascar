sftentwt = rsf.doc.rsfprog('sftentwt','user/gee/Mtentwt.c','''Tent-like weight for patching.''')
sftentwt.par('windwt',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftentwt.par('w',rsf.doc.rsfpar('ints','','','''window size  [dim]'''))
sftentwt.par('k',rsf.doc.rsfpar('ints','','','''number of windows  [dim]'''))
sftentwt.par('a',rsf.doc.rsfpar('ints','','','''filter size  [dim]'''))
sftentwt.par('center',rsf.doc.rsfpar('ints','','',''' [dim]'''))
sftentwt.par('dim',rsf.doc.rsfpar('int','2','','''number of dimensions '''))
sftentwt.par('tent',rsf.doc.rsfpar('bool','y','','''if y, use tent-like weight; n, cosine weight '''))
sftentwt.version('1.7 Mtentwt.c 840 2004-10-25 12:31:16Z fomels')
sftentwt.synopsis('''sftentwt > wallwt.rsf windwt=windwt.rsf w= k= a= center= dim=2 tent=y''','''''')
rsf.doc.progs['sftentwt']=sftentwt

