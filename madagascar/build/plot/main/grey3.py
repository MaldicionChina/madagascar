sfgrey3 = rsf.doc.rsfprog('sfgrey3','plot/main/grey3.c','''Generate 3-D cube plot.''')
sfgrey3.par('point1',rsf.doc.rsfpar('float','0.5','','''fraction of the vertical axis for front face '''))
sfgrey3.par('point2',rsf.doc.rsfpar('float','0.5','','''fraction of the horizontal axis for front face '''))
sfgrey3.par('frame1',rsf.doc.rsfpar('int','0','','''top frame number '''))
sfgrey3.par('frame2',rsf.doc.rsfpar('int','n2-1','','''side frame number '''))
sfgrey3.par('frame3',rsf.doc.rsfpar('int','0','','''front frame number '''))
sfgrey3.par('movie',rsf.doc.rsfpar('int','0','','''0: no movie, 1: movie over axis 1, 2: axis 2, 3: axis 3 '''))
sfgrey3.par('dframe',rsf.doc.rsfpar('int','1','','''frame increment in a movie '''))
sfgrey3.par('n1pix',rsf.doc.rsfpar('int','n1/point1+n3/(1.-point1)','','''number of vertical pixels '''))
sfgrey3.par('n2pix',rsf.doc.rsfpar('int','n2/point2+n3/(1.-point2)','','''number of horizontal pixels '''))
sfgrey3.par('flat',rsf.doc.rsfpar('bool','y','','''if n, display perspective view '''))
sfgrey3.par('scalebar',rsf.doc.rsfpar('bool','n','','''if y, draw scalebar '''))
sfgrey3.par('minval',rsf.doc.rsfpar('float','','','''minimum value for scalebar (default is the data minimum) '''))
sfgrey3.par('maxval',rsf.doc.rsfpar('float','','','''maximum value for scalebar (default is the data maximum) '''))
sfgrey3.par('barreverse',rsf.doc.rsfpar('bool','n','','''if y, go from small to large on the bar scale '''))
sfgrey3.par('nreserve',rsf.doc.rsfpar('int','8','','''reserved colors '''))
sfgrey3.par('bar',rsf.doc.rsfpar('string ',desc='''file for scalebar data '''))
sfgrey3.par('color',rsf.doc.rsfpar('string ',desc='''color scheme (default is i) '''))
sfgrey3.version('1.7 grey3.c 13825 2015-02-04 22:57:20Z sfomel')
sfgrey3.synopsis('''sfgrey3 < in.rsf point1=0.5 point2=0.5 frame1=0 frame2=n2-1 frame3=0 movie=0 dframe=1 n1pix=n1/point1+n3/(1.-point1) n2pix=n2/point2+n3/(1.-point2) flat=y scalebar=n minval= maxval= barreverse=n nreserve=8 bar= color= > plot.vpl''','''Requires an "unsigned char" input (the output of sfbyte).

April 2012 program of the month:
http://ahay.org/rsflog/index.php?/archives/287-Program-of-the-month-sfgrey3.html
''')
rsf.doc.progs['sfgrey3']=sfgrey3

