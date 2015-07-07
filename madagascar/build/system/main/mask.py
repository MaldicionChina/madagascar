sfmask = rsf.doc.rsfprog('sfmask','system/main/mask.c','''Create a mask.''')
sfmask.par('min',rsf.doc.rsfpar('float','','','''minimum header value '''))
sfmask.par('max',rsf.doc.rsfpar('float','','','''maximum header value '''))
sfmask.par('min',rsf.doc.rsfpar('int','','','''minimum header value '''))
sfmask.par('max',rsf.doc.rsfpar('int','','','''maximum header value '''))
sfmask.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfmask')
sfmask.version('1.7 mask.c 7791 2011-10-29 13:22:26Z sfomel')
sfmask.synopsis('''sfmask < in.rsf > out.rsf min= max= min= max=''','''
Mask is an integer data with ones and zeros. 
Ones correspond to input values between min and max.

The output can be used with sfheaderwindow.
''')
rsf.doc.progs['sfmask']=sfmask

