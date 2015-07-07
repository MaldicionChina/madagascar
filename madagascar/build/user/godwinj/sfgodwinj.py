import rsf.doc

sfpysvd = rsf.doc.rsfprog('sfpysvd','user/godwinj/Mpysvd.py','''Perform SVD on a matrix using SCIPY.  ''')
sfpysvd.par('vectors',rsf.doc.rsfpar('bool','n','','''Output singular vectors?'''))
sfpysvd.par('left',rsf.doc.rsfpar('string','','','''File to store left singular vectors'''))
sfpysvd.par('right',rsf.doc.rsfpar('string','','','''File to store right singular vectors'''))
sfpysvd.version('1.7')
sfpysvd.synopsis('''sfpysvd < fin.rsf > fout.rsf > lout.rsf > rout.rsf vectors=n left= right=''','''
REQUIRES the PYTHON API, NUMPY AND SCIPY
''')
rsf.doc.progs['sfpysvd']=sfpysvd

sfthreedcube = rsf.doc.rsfprog('sfthreedcube','user/godwinj/Mthreedcube.py','''Interactively displays a 3D cube of RSF data using Python + MayaVi2 + VTK.  ''')
sfthreedcube.version('1.7')
sfthreedcube.synopsis('''sfthreedcube < fin.rsf''','''
REQUIRES NUMPY, SCIPY, and MAyaVi2
''')
rsf.doc.progs['sfthreedcube']=sfthreedcube

sfgui = rsf.doc.rsfprog('sfgui','user/godwinj/Mgui.py','''''')
sfgui.version('1.7')
sfgui.synopsis('''sfgui''','''Open tkMadagascar GUI
''')
rsf.doc.progs['sfgui']=sfgui

sfbrowser = rsf.doc.rsfprog('sfbrowser','user/godwinj/Mbrowser.py','''''')
sfbrowser.version('1.7')
sfbrowser.synopsis('''sfbrowser''','''Open tkMadagascar program browser.
''')
rsf.doc.progs['sfbrowser']=sfbrowser

