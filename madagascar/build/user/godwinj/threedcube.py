sfthreedcube = rsf.doc.rsfprog('sfthreedcube','user/godwinj/Mthreedcube.py','''Interactively displays a 3D cube of RSF data using Python + MayaVi2 + VTK.  ''')
sfthreedcube.version('1.7')
sfthreedcube.synopsis('''sfthreedcube < fin.rsf''','''
REQUIRES NUMPY, SCIPY, and MAyaVi2
''')
rsf.doc.progs['sfthreedcube']=sfthreedcube

