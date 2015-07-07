sffdip = rsf.doc.rsfprog('sffdip','user/pwd/Mfdip.c','''3D fast dip estimation by plane wave destruction ''')
sffdip.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffdip.par('n4',rsf.doc.rsfpar('int','2','','''what to compute in 3-D. 0: in-line, 1: cross-line, 2: both '''))
sffdip.par('liter',rsf.doc.rsfpar('int','20','','''number of linear iterations '''))
sffdip.par('rect1',rsf.doc.rsfpar('int','1','','''dip smoothness on 1st axis '''))
sffdip.par('rect2',rsf.doc.rsfpar('int','1','','''dip smoothness on 2nd axis '''))
sffdip.par('rect3',rsf.doc.rsfpar('int','1','','''dip smoothness on 3rd axuis '''))
sffdip.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sffdip.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffdip.version('1.7')
sffdip.synopsis('''sffdip < in.rsf > out.rsf mask=mask.rsf n4=2 liter=20 rect1=1 rect2=1 rect3=1 verb=n''','''''')
rsf.doc.progs['sffdip']=sffdip

