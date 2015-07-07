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

