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

