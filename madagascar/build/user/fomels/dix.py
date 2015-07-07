sfdix = rsf.doc.rsfprog('sfdix','user/fomels/Mdix.c','''Convert RMS to interval velocity using LS and shaping regularization. ''')
sfdix.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdix.par('vrmsout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdix.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of iterations '''))
sfdix.par('rect#',rsf.doc.rsfpar('string','(1,1,...)','','''smoothing radius on #-th axis '''))
sfdix.par('weight',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdix.par('vrmsout',rsf.doc.rsfpar('string ',desc='''optionally, output predicted vrms (auxiliary output file name)'''))
sfdix.version('1.7 Mdix.c 7107 2011-04-10 02:04:14Z ivlad')
sfdix.synopsis('''sfdix < vrms.rsf > vint.rsf weight=weight.rsf vrmsout=vout.rsf niter=100 rect#=(1,1,...)''','''''')
rsf.doc.progs['sfdix']=sfdix

