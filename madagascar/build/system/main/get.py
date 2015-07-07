sfget = rsf.doc.rsfprog('sfget','system/main/get.c','''Output parameters from the header.''')
sfget.par('parform',rsf.doc.rsfpar('bool','y','','''If y, print out parameter=value. If n, print out value. '''))
sfget.par('all',rsf.doc.rsfpar('bool','n','','''If output all values. '''))
sfget.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfget')
sfget.version('1.7')
sfget.synopsis('''sfget parform=y all=n par1 par2 ...''','''''')
rsf.doc.progs['sfget']=sfget

