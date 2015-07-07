sfcontour = rsf.doc.rsfprog('sfcontour','plot/main/contour.c','''Contour plot.''')
sfcontour.par('c',rsf.doc.rsfpar('floats','','',''' [nc]'''))
sfcontour.par('min1',rsf.doc.rsfpar('float','o1','','''minimum on 1st axis '''))
sfcontour.par('min2',rsf.doc.rsfpar('float','o2','','''minimum on 2nd axis '''))
sfcontour.par('max1',rsf.doc.rsfpar('float','o1+(n1-1)*d1','','''maximum on 1st axis '''))
sfcontour.par('max2',rsf.doc.rsfpar('float','o2+(n2-1)*d2','','''maximum on 2nd axis '''))
sfcontour.par('nc',rsf.doc.rsfpar('int','50','','''number of contours '''))
sfcontour.par('dc',rsf.doc.rsfpar('float','','','''contour increment '''))
sfcontour.par('c0',rsf.doc.rsfpar('float','','','''first contour '''))
sfcontour.par('transp',rsf.doc.rsfpar('bool','y','','''if y, transpose the axes '''))
sfcontour.par('minval',rsf.doc.rsfpar('float','','','''minimum value for scalebar (default is the data minimum) '''))
sfcontour.par('maxval',rsf.doc.rsfpar('float','','','''maximum value for scalebar (default is the data maximum) '''))
sfcontour.par('allpos',rsf.doc.rsfpar('bool','y','','''contour positive values only '''))
sfcontour.par('cfile',rsf.doc.rsfpar('string ',desc='''contours in a file '''))
sfcontour.par('barlabel',rsf.doc.rsfpar('string ',desc='''scale bar label '''))
sfcontour.version('1.7')
sfcontour.synopsis('''sfcontour < in.rsf c= min1=o1 min2=o2 max1=o1+(n1-1)*d1 max2=o2+(n2-1)*d2 nc=50 dc= c0= transp=y minval= maxval= allpos=y cfile= barlabel= > plot.vpl''','''Run "sfdoc stdplot" for more parameters.

December 2011 program of the month:
http://ahay.org/rsflog/index.php?/archives/277-Programs-of-the-month-sfcontour.html
''')
rsf.doc.progs['sfcontour']=sfcontour

