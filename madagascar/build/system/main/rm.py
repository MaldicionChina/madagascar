sfrm = rsf.doc.rsfprog('sfrm','system/main/rm.c','''Remove RSF files together with their data.''')
sfrm.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfrm')
sfrm.version('1.7')
sfrm.synopsis('''sfrm file1.rsf [file2.rsf ...] [-i] [-v] [-f] ''','''Mimics the standard Unix rm command.

See also: sfmv, sfcp.
''')
rsf.doc.progs['sfrm']=sfrm

