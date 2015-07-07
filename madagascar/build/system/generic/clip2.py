sfclip2 = rsf.doc.rsfprog('sfclip2','system/generic/Mclip2.c','''One- or two-sided data clipping.''')
sfclip2.par('upper',rsf.doc.rsfpar('float','+FLT_MAX','','''upper clip value '''))
sfclip2.par('lower',rsf.doc.rsfpar('float','-FLT_MAX','','''lower clip value '''))
sfclip2.version('1.7')
sfclip2.synopsis('''sfclip2 < in.rsf > out.rsf upper=+FLT_MAX lower=-FLT_MAX''','''
sfclip2 is a generalization of sfclip.

Clip values above xu:         sfclip2 < in.rsf > out.rsf upper=xu
Clip values below xl:         sfclip2 < in.rsf > out.rsf lower=xl
Clip values outside [xu,xl]:  sfclip2 < in.rsf > out.rsf upper=xu lower=xl

sfclip2 < in.rsf > out.rsf upper=x lower=-x

is equivalent to

sfclip < in.rsf > out.rsf clip=x
''')
rsf.doc.progs['sfclip2']=sfclip2

