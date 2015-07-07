sfdip = rsf.doc.rsfprog('sfdip','user/pwd/Mdip.c','''3-D dip estimation by plane wave destruction. ''')
sfdip.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdip.par('idip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdip.par('xdip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdip.par('both',rsf.doc.rsfpar('bool','n','','''if y, compute both left and right predictions '''))
sfdip.par('n4',rsf.doc.rsfpar('int','2','','''what to compute in 3-D. 0: in-line, 1: cross-line, 2: both '''))
sfdip.par('niter',rsf.doc.rsfpar('int','5','','''number of iterations '''))
sfdip.par('liter',rsf.doc.rsfpar('int','20','','''number of linear iterations '''))
sfdip.par('rect1',rsf.doc.rsfpar('int','1','','''dip smoothness on 1st axis '''))
sfdip.par('rect2',rsf.doc.rsfpar('int','1','','''dip smoothness on 2nd axis '''))
sfdip.par('rect3',rsf.doc.rsfpar('int','1','','''dip smoothness on 3rd axuis '''))
sfdip.par('p0',rsf.doc.rsfpar('float','0.','','''initial in-line dip '''))
sfdip.par('q0',rsf.doc.rsfpar('float','0.','','''initial cross-line dip '''))
sfdip.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfdip.par('nj1',rsf.doc.rsfpar('int','1','','''in-line antialiasing '''))
sfdip.par('nj2',rsf.doc.rsfpar('int','1','','''cross-line antialiasing '''))
sfdip.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfdip.par('pmin',rsf.doc.rsfpar('float','-FLT_MAX','','''minimum inline dip '''))
sfdip.par('pmax',rsf.doc.rsfpar('float','+FLT_MAX','','''maximum inline dip '''))
sfdip.par('qmin',rsf.doc.rsfpar('float','-FLT_MAX','','''minimum cross-line dip '''))
sfdip.par('qmax',rsf.doc.rsfpar('float','+FLT_MAX','','''maximum cross-line dip '''))
sfdip.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sfdip.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdip.par('idip',rsf.doc.rsfpar('string ',desc='''initial in-line dip (auxiliary input file name)'''))
sfdip.par('xdip',rsf.doc.rsfpar('string ',desc='''initial cross-line dip (auxiliary input file name)'''))
sfdip.version('1.7 Mdip.c 11132 2013-10-20 18:40:59Z sfomel')
sfdip.synopsis('''sfdip < in.rsf > out.rsf mask=mask.rsf idip=idip0.rsf xdip=xdip0.rsf both=n n4=2 niter=5 liter=20 rect1=1 rect2=1 rect3=1 p0=0. q0=0. order=1 nj1=1 nj2=1 verb=n pmin=-FLT_MAX pmax=+FLT_MAX qmin=-FLT_MAX qmax=+FLT_MAX eps=0.0f''','''
The output is dimensionless (stepout in time measured in time samples). 

June 2012 program of the month:
http://ahay.org/rsflog/index.php?/archives/295-Program-of-the-month-sfdip.html
''')
rsf.doc.progs['sfdip']=sfdip

