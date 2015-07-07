sfdmigda = rsf.doc.rsfprog('sfdmigda','user/aklokov/Mdmigda.cc','''2D depth scattering-angle Kirchhoff migration  ''')
sfdmigda.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdmigda.par('dag',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdmigda.par('cig',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdmigda.par('mcig',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdmigda.par('esct',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdmigda.par('escx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdmigda.par('axis2label',rsf.doc.rsfpar('int','0','','''0 - shot; 1 - cmp; 2 - receiver '''))
sfdmigda.par('isAA',rsf.doc.rsfpar('bool','y','','''if y, apply anti-aliasing '''))
sfdmigda.par('izn',rsf.doc.rsfpar('int','dp.zNum','','''number of imaged depth samples '''))
sfdmigda.par('ixn',rsf.doc.rsfpar('int','dp.xNum','','''number of imaged inlines '''))
sfdmigda.par('iyn',rsf.doc.rsfpar('int','rp.is3D ? vp.yNum : 1','','''number of imaged crosslines '''))
sfdmigda.par('izo',rsf.doc.rsfpar('float','dp.zStart','','''first imaged depth (in meters) '''))
sfdmigda.par('ixo',rsf.doc.rsfpar('float','dp.xStart','','''first imaged inline (in meters) '''))
sfdmigda.par('iyo',rsf.doc.rsfpar('float','dp.yStart','','''first imaged crossline (in meters) '''))
sfdmigda.par('izd',rsf.doc.rsfpar('float','dp.zStep','','''step in depth (in meters) '''))
sfdmigda.par('ixd',rsf.doc.rsfpar('float','dp.xStep','','''step in inlines (in meters) '''))
sfdmigda.par('iyd',rsf.doc.rsfpar('float','dp.yStep','','''step in crosslines (in meters) '''))
sfdmigda.par('dipn',rsf.doc.rsfpar('int','161','','''number of dip-angles '''))
sfdmigda.par('dipo',rsf.doc.rsfpar('float','-80.f','','''first dip-angle '''))
sfdmigda.par('dipd',rsf.doc.rsfpar('float','1.f','','''step in dip-angle '''))
sfdmigda.par('iscatn',rsf.doc.rsfpar('int','1','','''number of scattering-angles '''))
sfdmigda.par('iscato',rsf.doc.rsfpar('float','0.f','','''first scattering-angle (in degree) '''))
sfdmigda.par('iscatd',rsf.doc.rsfpar('float','2 * gp.dipStep','','''scattering-angle increment (in degree) '''))
sfdmigda.par('ttd',rsf.doc.rsfpar('float','0.002f','','''travel-times increment '''))
sfdmigda.par('ttn',rsf.doc.rsfpar('int','(int) floor(0.001 * 0.5 * maxTime / ttStep + 1)','','''travel-times number '''))
sfdmigda.par('ttrayd',rsf.doc.rsfpar('float','gp.dipStep / 2.f','','''travel-times rays increment '''))
sfdmigda.par('ttrayo',rsf.doc.rsfpar('float','minttRay','','''travel-times rays start '''))
sfdmigda.par('ttrayn',rsf.doc.rsfpar('int','(int) floor((maxttRay - minttRay) / ttRayStep + 1)','','''travel-times rays number '''))
sfdmigda.par('vel',rsf.doc.rsfpar('string ',desc='''velocity model file (velocity in m/s) (auxiliary input file name)'''))
sfdmigda.par('dag',rsf.doc.rsfpar('string ',desc='''output file containing CIGs in the dip-angle domain (auxiliary output file name)'''))
sfdmigda.par('cig',rsf.doc.rsfpar('string ',desc='''output file containing CIGs in the scattering-angle domain (auxiliary output file name)'''))
sfdmigda.par('mcig',rsf.doc.rsfpar('string ',desc='''output file containing multi-CIGs (in the dip-angle and the scattering-angle domain both (auxiliary output file name)'''))
sfdmigda.par('esct',rsf.doc.rsfpar('string ',desc='''output file containing escqpe times (auxiliary output file name)'''))
sfdmigda.par('escx',rsf.doc.rsfpar('string ',desc='''output file containing escape positions (auxiliary output file name)'''))
sfdmigda.version('1.7')
sfdmigda.synopsis('''sfdmigda < dataFile.rsf vel=velFile.rsf > imageFile.rsf dag=dagFile.rsf cig=acigFile.rsf mcig=mcigFile.rsf esct=tEscFile.rsf escx=xEscFile.rsf axis2label=0 isAA=y izn=dp.zNum ixn=dp.xNum iyn=rp.is3D ? vp.yNum : 1 izo=dp.zStart ixo=dp.xStart iyo=dp.yStart izd=dp.zStep ixd=dp.xStep iyd=dp.yStep dipn=161 dipo=-80.f dipd=1.f iscatn=1 iscato=0.f iscatd=2 * gp.dipStep ttd=0.002f ttn=(int) floor(0.001 * 0.5 * maxTime / ttStep + 1) ttrayd=gp.dipStep / 2.f ttrayo=minttRay ttrayn=(int) floor((maxttRay - minttRay) / ttRayStep + 1)''','''''')
rsf.doc.progs['sfdmigda']=sfdmigda

