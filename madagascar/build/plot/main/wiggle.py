sfwiggle = rsf.doc.rsfprog('sfwiggle','plot/main/wiggle.c','''Plot data with wiggly traces. ''')
sfwiggle.par('xpos',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwiggle.par('xmax',rsf.doc.rsfpar('float','','','''maximum trace position (if using xpos) '''))
sfwiggle.par('xmin',rsf.doc.rsfpar('float','','','''minimum trace position (if using xpos) '''))
sfwiggle.par('poly',rsf.doc.rsfpar('bool','n','','''if draw polygons '''))
sfwiggle.par('polyneg',rsf.doc.rsfpar('bool','n','','''if polygons for negative values '''))
sfwiggle.par('fatp',rsf.doc.rsfpar('int','1','','''polygon border fatness '''))
sfwiggle.par('xmask',rsf.doc.rsfpar('int','1','','''polygon filling '''))
sfwiggle.par('ymask',rsf.doc.rsfpar('int','1','','''polygon filling '''))
sfwiggle.par('pclip',rsf.doc.rsfpar('float','98.','','''clip percentile '''))
sfwiggle.par('zplot',rsf.doc.rsfpar('float','0.75','','''vertical separation '''))
sfwiggle.par('clip',rsf.doc.rsfpar('float','0.','','''data clip (estimated from pclip by default '''))
sfwiggle.par('seemean',rsf.doc.rsfpar('bool','n','','''if y, plot mean lines of traces '''))
sfwiggle.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfwiggle.par('transp',rsf.doc.rsfpar('bool','n','','''if y, transpose the axes '''))
sfwiggle.par('yreverse',rsf.doc.rsfpar('bool','n','','''if y, reverse the vertical axis '''))
sfwiggle.par('xreverse',rsf.doc.rsfpar('bool','n','','''if y, reverse the horizontal axis '''))
sfwiggle.par('xpos',rsf.doc.rsfpar('string ',desc='''optional header file with trace positions (auxiliary input file name)'''))
sfwiggle.version('1.7')
sfwiggle.synopsis('''sfwiggle < in.rsf xpos=xpos.rsf xmax= xmin= poly=n polyneg=n fatp=1 xmask=1 ymask=1 pclip=98. zplot=0.75 clip=0. seemean=n verb=n transp=n yreverse=n xreverse=n > plot.vpl''','''Run "sfdoc stdplot" for more parameters.

June 2013 program of the month:
http://www.ahay.org/rsflog/index.php?/archives/340-Program-of-the-month-sfwiggle.html
''')
rsf.doc.progs['sfwiggle']=sfwiggle

