sfmodrefl2 = rsf.doc.rsfprog('sfmodrefl2','system/seismic/Mmodrefl2.c','''Normal reflectivity modeling. ''')
sfmodrefl2.par('nt',rsf.doc.rsfpar('int','','','''time samples '''))
sfmodrefl2.par('dt',rsf.doc.rsfpar('float','','','''time sampling '''))
sfmodrefl2.par('nw',rsf.doc.rsfpar('int','4','','''interpolation length '''))
sfmodrefl2.version('1.7')
sfmodrefl2.synopsis('''sfmodrefl2 < in.rsf > out.rsf nt= dt= nw=4''','''
In this version, the input contains Vp, Vs, and density into one file. 
The output contains PP intercept, PP gradient, and PS gradient.

''')
rsf.doc.progs['sfmodrefl2']=sfmodrefl2

