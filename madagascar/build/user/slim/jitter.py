sfjitter = rsf.doc.rsfprog('sfjitter','user/slim/Mjitter.py','''''')
sfjitter.par('perc',rsf.doc.rsfpar('float','.75','','''percentage of traces to remove'''))
sfjitter.par('jit',rsf.doc.rsfpar('float','1/(1-perc','',''''''))
sfjitter.par('seed',rsf.doc.rsfpar('int','np.random.randn(','',''''''))
sfjitter.version('1.7')
sfjitter.synopsis('''sfjitter perc=.75 jit=1/(1-perc seed=np.random.randn(''','''Return mask to remove random traces in 2D using jittered sampling
''')
rsf.doc.progs['sfjitter']=sfjitter

