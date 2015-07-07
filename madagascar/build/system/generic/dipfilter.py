sfdipfilter = rsf.doc.rsfprog('sfdipfilter','system/generic/Mdipfilter.c','''Filter data based on dip in 2-D or 3-D.''')
sfdipfilter.par('dim',rsf.doc.rsfpar('int','2','[2,3]','''Dimensionality: filter 2-D planes or 3-D cubes '''))
sfdipfilter.par('angle',rsf.doc.rsfpar('bool','n','','''Filter based on angle (or velocity) '''))
sfdipfilter.par('v',rsf.doc.rsfpar('float','-1.','','''constant velocity (if angle-y)
	   The default is d(frequency)/d(wavenumber) '''))
sfdipfilter.par('ang1',rsf.doc.rsfpar('float','-50.','',''''''))
sfdipfilter.par('ang2',rsf.doc.rsfpar('float','-45.','',''''''))
sfdipfilter.par('ang3',rsf.doc.rsfpar('float','45.','',''''''))
sfdipfilter.par('ang4',rsf.doc.rsfpar('float','50.','','''Angle gate (in degrees) '''))
sfdipfilter.par('v1',rsf.doc.rsfpar('float','0.','',''''''))
sfdipfilter.par('v2',rsf.doc.rsfpar('float','0.1','',''''''))
sfdipfilter.par('v3',rsf.doc.rsfpar('float','99999.','',''''''))
sfdipfilter.par('v4',rsf.doc.rsfpar('float','999999.','','''Velocity gate '''))
sfdipfilter.par('pass',rsf.doc.rsfpar('bool','y','','''Pass or reject band '''))
sfdipfilter.version('1.7 Mdipfilter.c 11735 2014-02-07 15:39:24Z sfomel')
sfdipfilter.synopsis('''sfdipfilter < in.rsf > out.rsf dim=2 angle=n v=-1. ang1=-50. ang2=-45. ang3=45. ang4=50. v1=0. v2=0.1 v3=99999. v4=999999. pass=y''','''
February 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/374-Program-of-the-month-sfdipfilter.html
''')
rsf.doc.progs['sfdipfilter']=sfdipfilter

