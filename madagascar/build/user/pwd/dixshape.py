sfdixshape = rsf.doc.rsfprog('sfdixshape','user/pwd/Mdixshape.c','''Convert RMS to interval velocity using LS and shaping regularization.''')
sfdixshape.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdixshape.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdixshape.par('vrmsout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdixshape.par('rect1',rsf.doc.rsfpar('int','3','',''''''))
sfdixshape.par('rect2',rsf.doc.rsfpar('int','3','','''smoothing radius '''))
sfdixshape.par('lam',rsf.doc.rsfpar('float','1.','','''operator scaling for inversion '''))
sfdixshape.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfdixshape.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of iterations '''))
sfdixshape.par('vrmsout',rsf.doc.rsfpar('string ',desc='''optionally, output predicted vrms (auxiliary output file name)'''))
sfdixshape.version('1.7 Mdix.c 1131 2005-04-20 18:19:10Z fomels')
sfdixshape.synopsis('''sfdixshape < vrms.rsf > vint.rsf weight=weight.rsf dip=dip.rsf vrmsout=vout.rsf rect1=3 rect2=3 lam=1. order=1 niter=100 rect1= rect2= ...''','''rectN defines the size of the smoothing stencil in N-th dimension.
''')
rsf.doc.progs['sfdixshape']=sfdixshape

