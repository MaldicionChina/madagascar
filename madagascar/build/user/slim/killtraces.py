sfkilltraces = rsf.doc.rsfprog('sfkilltraces','user/slim/Mkilltraces.py','''''')
sfkilltraces.par('perc',rsf.doc.rsfpar('float','.75','','''percentage of traces to remove'''))
sfkilltraces.par('maxfactor',rsf.doc.rsfpar('float','1.','','''maximum gap factor'''))
sfkilltraces.par('seed',rsf.doc.rsfpar('int','np.random.randn(','',''''''))
sfkilltraces.version('1.7')
sfkilltraces.synopsis('''sfkilltraces perc=.75 maxfactor=1. seed=np.random.randn(''','''Return mask to remove random traces in 2D and 3D using a maximum gap
size constraint
''')
rsf.doc.progs['sfkilltraces']=sfkilltraces

