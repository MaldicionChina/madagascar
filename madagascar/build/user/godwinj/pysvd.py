sfpysvd = rsf.doc.rsfprog('sfpysvd','user/godwinj/Mpysvd.py','''Perform SVD on a matrix using SCIPY.  ''')
sfpysvd.par('vectors',rsf.doc.rsfpar('bool','n','','''Output singular vectors?'''))
sfpysvd.par('left',rsf.doc.rsfpar('string','','','''File to store left singular vectors'''))
sfpysvd.par('right',rsf.doc.rsfpar('string','','','''File to store right singular vectors'''))
sfpysvd.version('1.7')
sfpysvd.synopsis('''sfpysvd < fin.rsf > fout.rsf > lout.rsf > rout.rsf vectors=n left= right=''','''
REQUIRES the PYTHON API, NUMPY AND SCIPY
''')
rsf.doc.progs['sfpysvd']=sfpysvd

