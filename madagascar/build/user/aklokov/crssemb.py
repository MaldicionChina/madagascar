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

