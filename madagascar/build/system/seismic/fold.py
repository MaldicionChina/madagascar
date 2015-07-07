sffold = rsf.doc.rsfprog('sffold','system/seismic/Mfold.c','''Make a seismic foldplot/stacking chart. ''')
sffold.par('verbose',rsf.doc.rsfpar('int','1','','''0 terse, 1 informative, 2 chatty, 3 debug '''))
sffold.par('o1',rsf.doc.rsfpar('float','','','''Minimum label1 - usually min offset '''))
sffold.par('o2',rsf.doc.rsfpar('float','','','''Minimum label2 - usually min xline  '''))
sffold.par('o3',rsf.doc.rsfpar('float','','','''Minimum label3 - usually min iline '''))
sffold.par('n1',rsf.doc.rsfpar('int','','','''Number label1 - usually number offset '''))
sffold.par('n2',rsf.doc.rsfpar('int','','','''Number label2 - usually number xline '''))
sffold.par('n3',rsf.doc.rsfpar('int','','','''Number label3 - usually number iline '''))
sffold.par('d1',rsf.doc.rsfpar('float','','','''Delta label1 - usually delta offset  '''))
sffold.par('d2',rsf.doc.rsfpar('float','','','''Delta label2 - usually delta xline  '''))
sffold.par('d3',rsf.doc.rsfpar('float','','','''Delta label3 - usually delta iline  '''))
sffold.par('label1',rsf.doc.rsfpar('string ',desc='''header for axis1 - usually offset '''))
sffold.par('label2',rsf.doc.rsfpar('string ',desc='''header for axis2 - usually xline or cdp  '''))
sffold.par('label3',rsf.doc.rsfpar('string ',desc='''header for axis3 - usually iline  '''))
sffold.version('1.7')
sffold.synopsis('''sffold < in.rsf > out.rsf verbose=1 o1= o2= o3= n1= n2= n3= d1= d2= d3= label1= label2= label3=''','''
This is a general 3D histogram program implemented to create foldplot or
stacking charts on a 3d project from trace headers.  Axis1, 2 and 3 
define the bins for the output fold map.  These are usually 
(offset,xline,iline), but you might want to compute some other
histogram.  This can be done by selecting other segy headers using 
label1, 2 and 3.

See also fold= option in sfbin for creating 2D histograms.

EXAMPLES:

   To make a stacking chart movie showing fold(xline,offset) for each 
   iline from a 3D segyfile:

   sfsegyread tfile=tteapot.rsf hfile=teapot.asc bfile=teapot.bin \\
           tape=npr3_field.sgy > teapot.rsf

   # read the tfile, which contains the segy trace headers
   < tteapot.rsf sfdd type=float             \\
   | sffold verbose=1                        \\
            o1=0 n1=96  d1=200 label1=offset \\
            o2=1 n2=188 d2=1   label2=xline  \\
            o3=1 n3=345 d3=1   label3=iline  \\
   >foldplot.rsf
   <foldplot.rsf sfgrey title=foldplot pclip=100 \\
   | sfpen 

  # transpose this data to plot foldmaps for each offset window:

  < foldplot.rsf sftransp plane=13          \\
  | sftransp plane=12                       \\
  | sfgrey title=foldplot_off gainpanel=all \\
  | sfpen
  
''')
rsf.doc.progs['sffold']=sffold

