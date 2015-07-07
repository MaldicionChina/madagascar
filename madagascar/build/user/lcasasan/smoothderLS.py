sfsmoothderLS = rsf.doc.rsfprog('sfsmoothderLS','user/lcasasan/MsmoothderLS.c','''Convert input to its derivative using LS and shaping regularization''')
sfsmoothderLS.par('dataout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsmoothderLS.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of iterations '''))
sfsmoothderLS.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfsmoothderLS.par('dataout',rsf.doc.rsfpar('string ',desc='''optionally, output predicted data (auxiliary output file name)'''))
sfsmoothderLS.version('1.7 Mdix.c 5595 2010-03-21 16:54:14Z sfomel')
sfsmoothderLS.synopsis('''sfsmoothderLS < DATA.rsf > MODEL.rsf dataout=DATA_OUT.rsf niter=100 rect#=(1,1,...)''',''' * applied to causint_lop d = L m

 Takes: rect1= rect2= ...

 rectN defines the size of the smoothing stencil in N-th dimension.
''')
rsf.doc.progs['sfsmoothderLS']=sfsmoothderLS

