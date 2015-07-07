sfrmrf = rsf.doc.rsfprog('sfrmrf','user/ivlad/Mrmrf.py','''Recursively removes all RSF headers in a directory (associated binaries too)''')
sfrmrf.par('verb',rsf.doc.rsfpar('bool','n','','''Display headers and binaries being deleted'''))
sfrmrf.par('dir',rsf.doc.rsfpar('string','','','''Directory with files'''))
sfrmrf.par('rec',rsf.doc.rsfpar('bool','n','','''Whether to go down recursively'''))
sfrmrf.version('1.7')
sfrmrf.synopsis('''sfrmrf verb=n dir= rec=n''','''Missing binaries do not cause failure.''')
rsf.doc.progs['sfrmrf']=sfrmrf

