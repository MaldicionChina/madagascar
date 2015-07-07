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

