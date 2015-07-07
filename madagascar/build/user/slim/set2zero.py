sfset2zero = rsf.doc.rsfprog('sfset2zero','user/slim/Mset2zero.c','''replaces content of RSF file with zeros''')
sfset2zero.version('1.7')
sfset2zero.synopsis('''sfset2zero file1.rsf [file2.rsf ...]''','''Used to create initial guess for SLIMpy.
''')
rsf.doc.progs['sfset2zero']=sfset2zero

