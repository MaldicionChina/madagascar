import rsf.doc

sfcrssemb = rsf.doc.rsfprog('sfcrssemb','user/aklokov/Mcrssemb.c','''CRS-based semblance''')
sfcrssemb.par('dataSq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcrssemb.par('xapp',rsf.doc.rsfpar('int','1','','''number of CIGs in the inline-direction processed simultaneously '''))
sfcrssemb.par('dipapp',rsf.doc.rsfpar('int','11','','''number of traces in the x-dip direction processed simultaneously '''))
sfcrssemb.par('coher',rsf.doc.rsfpar('int','11','','''height of a vertical window for semblance calculation '''))
sfcrssemb.par('scatnum',rsf.doc.rsfpar('int','1','','''shows how many traces were stacked in the scattering angle direction; 
       if the stack was normalized use the default value 
    '''))
sfcrssemb.par('s1',rsf.doc.rsfpar('float','','',''''''))
sfcrssemb.par('s2',rsf.doc.rsfpar('float','','',''''''))
sfcrssemb.version('1.7')
sfcrssemb.synopsis('''sfcrssemb < inDags_.rsf dataSq=inDagsSq_.rsf > sembFile_.rsf xapp=1 dipapp=11 coher=11 scatnum=1 s1= s2=''','''
   Several CIGs are used simultaneously. Dip-angle sections corresponding to the same 
   dip-angle compose a subvolume. The subvolume allows calculating semblance in the
   scattering-angle direction along reflection boundaries.

   Input:
   inDags_.rsf   - dip-angle gathers - stack in the scattering-angle direction
   InDagsSq_.rsf - stack of amplitude squares in the scattering-angle direction

   Working with just dip-angle gathers use default value of "scatnum" parameter

   Output:
   sembFile_.rsf - crs-based semblance file; has the same dimensions as the input files
''')
rsf.doc.progs['sfcrssemb']=sfcrssemb

sfcrssemb3d = rsf.doc.rsfprog('sfcrssemb3d','user/aklokov/Mcrssemb3d.c','''CRS-based semblance for 3D''')
sfcrssemb3d.par('dataSq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcrssemb3d.par('xapp',rsf.doc.rsfpar('int','1','','''number of CIGs in the inline-direction processed simultaneously '''))
sfcrssemb3d.par('yapp',rsf.doc.rsfpar('int','1','','''number of CIGs in the crossline-direction processed simultaneously '''))
sfcrssemb3d.par('dipappx',rsf.doc.rsfpar('int','11','','''number of traces in the x-dip direction processed simultaneously '''))
sfcrssemb3d.par('dipappy',rsf.doc.rsfpar('int','11','','''number of traces in the y-dip direction processed simultaneously '''))
sfcrssemb3d.par('coher',rsf.doc.rsfpar('int','11','','''height of a vertical window for semblance calculation '''))
sfcrssemb3d.par('scatnum',rsf.doc.rsfpar('int','1','','''shows how many traces were stacked in the scattering angle direction; 
       if the stack was normalized use the default value 
    '''))
sfcrssemb3d.version('1.7')
sfcrssemb3d.synopsis('''sfcrssemb3d < inDags_.rsf dataSq=inDagsSq_.rsf > sembFile_.rsf xapp=1 yapp=1 dipappx=11 dipappy=11 coher=11 scatnum=1''','''   Several CIGs are used simultaneously. Dip-angle sections corresponding to the same 
   dip-angle compose a subvolume. The subvolume allows calculating semblance in the
   scattering-angle direction along reflection boundaries.

   Input:
   inDags_.rsf   - 3D dip-angle gathers - stack in the scattering-angle direction
   inDagsSq_.rsf - stack of amplitude squares in the scattering-angle direction

   Working with just dip-angle gathers use default value of "scatnum" parameter

   Output:
   sembFile_.rsf - crs-based semblance file; has the same dimensions as the input files
''')
rsf.doc.progs['sfcrssemb3d']=sfcrssemb3d

sfdagap = rsf.doc.rsfprog('sfdagap','user/aklokov/Mdagap.c','''Reflection event apex protector/removal for dip-angle gathers.''')
sfdagap.par('dips',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdagap.par('ddep',rsf.doc.rsfpar('bool','y','','''if y, taper depends on depth; if n, no '''))
sfdagap.par('pwidth',rsf.doc.rsfpar('float','10.f','','''protected width (in degree) '''))
sfdagap.par('greyarea',rsf.doc.rsfpar('float','10.f','','''width of event tail taper (in degree) '''))
sfdagap.par('dz',rsf.doc.rsfpar('float','20.f','','''half of a migrated wave length '''))
sfdagap.par('dips',rsf.doc.rsfpar('string ',desc='''dips esitimated in the image domain (in degree) (auxiliary input file name)'''))
sfdagap.version('1.7')
sfdagap.synopsis('''sfdagap < dagFile.rsf dips=dipFile.rsf > taperFile.rsf ddep=y pwidth=10.f greyarea=10.f dz=20.f''','''
   May be used for migration aperture optimization or for reflected energy
   supression. For the last multiply the output on -1.

   Input:
   dagFile.rsf - input dip-angle gathers;
   dipFile.rsf - dips esitimated in the image domain. The dips are in degree (!)

   Output:
   taperFile.rsf - mask for input dip-angle gathers
''')
rsf.doc.progs['sfdagap']=sfdagap

sfdiptaper = rsf.doc.rsfprog('sfdiptaper','user/aklokov/Mdiptaper.c','''Aperture optimization for migrated gathers in the dip-angle domain.''')
sfdiptaper.par('dz',rsf.doc.rsfpar('float','20.f','','''half of a migrated wave length '''))
sfdiptaper.par('greyarea',rsf.doc.rsfpar('float','10.f','','''width of event tail taper (in degree) '''))
sfdiptaper.version('1.7')
sfdiptaper.synopsis('''sfdiptaper < dipFile.rsf > taperFile.rsf dz=20.f greyarea=10.f''','''
   Estimates a constructive imaging part of a reflection event in the dip-angle domain.
   Basing on the estimation defines a stacking weight for every migrated sample.

   Input:
   dipFile.rsf - dips esitimated in constant-dip subimages. The dips are in degree (!).
   A positive dip corresponds to an ascending boundary, a negative dip - to a descending boundary.
   A constant-dip subimage consists of migrated traces correspondig to the same dip-angle.

   Output:
   taperFile.rsf - optimal weights for the migrated samples
''')
rsf.doc.progs['sfdiptaper']=sfdiptaper

sftmigda = rsf.doc.rsfprog('sftmigda','user/aklokov/Mtmigda.cc','''3D time scattering-angle Kirchhoff migration  ''')
sftmigda.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftmigda.par('semb',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftmigda.par('dag',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftmigda.par('cig',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftmigda.par('is3d',rsf.doc.rsfpar('bool','n','','''if y, apply 3D migration '''))
sftmigda.par('axis2label',rsf.doc.rsfpar('int','0','','''0 - shot; 1 - cmp; 2 - receiver '''))
sftmigda.par('isAA',rsf.doc.rsfpar('bool','y','','''if y, apply anti-aliasing '''))
sftmigda.par('isDipAz',rsf.doc.rsfpar('bool','y','','''if y, apply dip/azimuth mode; if n, apply inline/crossline angle mode '''))
sftmigda.par('hmign',rsf.doc.rsfpar('int','dp.hNum','','''number of migrated offsets '''))
sftmigda.par('sembWindow',rsf.doc.rsfpar('int','11','','''vertical window for semblance calculation (in samples) '''))
sftmigda.par('edgeTaper',rsf.doc.rsfpar('float','5.f','','''edge taper for dip-angle gathers (in degree) '''))
sftmigda.par('itn',rsf.doc.rsfpar('int','dp.zNum','','''number of imaged times '''))
sftmigda.par('ixn',rsf.doc.rsfpar('int','dp.xNum','','''number of imaged inlines '''))
sftmigda.par('iyn',rsf.doc.rsfpar('int','rp.is3D ? vp.yNum : 1','','''number of imaged crosslines '''))
sftmigda.par('ito',rsf.doc.rsfpar('float','dp.zStart','','''first imaged time (in ms) '''))
sftmigda.par('ixo',rsf.doc.rsfpar('float','dp.xStart','','''first imaged inline '''))
sftmigda.par('iyo',rsf.doc.rsfpar('float','dp.yStart','','''first imaged crossline '''))
sftmigda.par('itd',rsf.doc.rsfpar('float','dp.zStep','','''step in imaged times  (in ms) '''))
sftmigda.par('ixd',rsf.doc.rsfpar('float','dp.xStep','','''step in imaged inlines '''))
sftmigda.par('iyd',rsf.doc.rsfpar('float','dp.yStep','','''step in imaged crosslines '''))
sftmigda.par('dipn',rsf.doc.rsfpar('int','1','','''number of dip-angles '''))
sftmigda.par('sdipn',rsf.doc.rsfpar('int','1','','''number of secondary (azimuth or crossline) angles '''))
sftmigda.par('dipo',rsf.doc.rsfpar('float','0.f','','''first dip-angle '''))
sftmigda.par('sdipo',rsf.doc.rsfpar('float','90.f','','''first secondary (azimuth or crossline) angle '''))
sftmigda.par('dipd',rsf.doc.rsfpar('float','1.f','','''step in dip-angle '''))
sftmigda.par('sdipd',rsf.doc.rsfpar('float','1.f','','''step in secondary (azimuth or crossline) angle '''))
sftmigda.par('vel',rsf.doc.rsfpar('string ',desc='''velocity model file (velocity in m/s) (auxiliary input file name)'''))
sftmigda.par('semb',rsf.doc.rsfpar('string ',desc='''output file containing semblance measure of CIGs stacking (auxiliary output file name)'''))
sftmigda.par('dag',rsf.doc.rsfpar('string ',desc='''output file containing CIGs in the dip-angle domain (auxiliary output file name)'''))
sftmigda.par('cig',rsf.doc.rsfpar('string ',desc='''output file containing CIGs in the surface-offset domain (auxiliary output file name)'''))
sftmigda.version('1.7')
sftmigda.synopsis('''sftmigda < dataFile.rsf vel=velFile.rsf > imageFile.rsf semb=sembFile.rsf dag=dagFile.rsf cig=cigFile.rsf is3d=n axis2label=0 isAA=y isDipAz=y hmign=dp.hNum sembWindow=11 edgeTaper=5.f itn=dp.zNum ixn=dp.xNum iyn=rp.is3D ? vp.yNum : 1 ito=dp.zStart ixo=dp.xStart iyo=dp.yStart itd=dp.zStep ixd=dp.xStep iyd=dp.yStep dipn=1 sdipn=1 dipo=0.f sdipo=90.f dipd=1.f sdipd=1.f''','''''')
rsf.doc.progs['sftmigda']=sftmigda

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

