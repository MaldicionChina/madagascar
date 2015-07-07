sfcp = rsf.doc.rsfprog('sfcp','system/main/cp.c','''Copy or move a dataset.''')
sfcp.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfcp')
sfcp.version('1.7')
sfcp.synopsis('''sfcp < in.rsf > out.rsf in.rsf out.rsf''','''sfcp - copy, sfmv - move.
Mimics standard Unix commands.
''')
rsf.doc.progs['sfcp']=sfcp

