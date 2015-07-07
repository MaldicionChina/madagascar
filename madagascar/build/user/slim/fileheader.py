sffileheader = rsf.doc.rsfprog('sffileheader','user/slim/Mfileheader.c','''dumps header information to the standard output.''')
sffileheader.par('large',rsf.doc.rsfpar('bool','n','','''if y, file with large dimensions. '''))
sffileheader.par('parform',rsf.doc.rsfpar('bool','y','','''If y, print out parameter=value. If n, print out value. '''))
sffileheader.par('all',rsf.doc.rsfpar('bool','n','','''If y, print all values, icluding singleton dimensions.
       If n, drop trailing singleteon dimensions.'''))
sffileheader.version('1.7')
sffileheader.synopsis('''sffileheader < in.rsf large=n parform=y all=n''','''   Extended sffiledims.''')
rsf.doc.progs['sffileheader']=sffileheader

