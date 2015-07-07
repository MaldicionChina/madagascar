sfpclip = rsf.doc.rsfprog('sfpclip','user/ivlad/Mpclip.py','''Percentile clip. Shell for sfclip(sfquantile(input)).''')
sfpclip.par('inp',rsf.doc.rsfpar('string','','','''input file'''))
sfpclip.par('out',rsf.doc.rsfpar('string','','','''output file'''))
sfpclip.par('verb',rsf.doc.rsfpar('bool','n','','''if y, print system commands, outputs'''))
sfpclip.par('pclip',rsf.doc.rsfpar('float','99','','''percentile clip'''))
sfpclip.version('1.7')
sfpclip.synopsis('''sfpclip inp= out= verb=n pclip=99''','''''')
rsf.doc.progs['sfpclip']=sfpclip

