sfquantile = rsf.doc.rsfprog('sfquantile','user/ivlad/Mquantile.c','''Computes what clip value corresponds to a given pclip.''')
sfquantile.par('pclip',rsf.doc.rsfpar('float','','','''Percentage clip, between 0 and 100 '''))
sfquantile.par('memsize',rsf.doc.rsfpar('int','sf_memsize()','','''Max amount of RAM (in Mb) to be used '''))
sfquantile.version('1.7')
sfquantile.synopsis('''sfquantile < in.rsf pclip= memsize=sf_memsize()''','''Loads the entire dataset in core. Use it to find a clip= parameter for sfclip, given a wanted pclip=''')
rsf.doc.progs['sfquantile']=sfquantile

