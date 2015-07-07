sfgraph = rsf.doc.rsfprog('sfgraph','plot/main/graph.c','''Graph plot.''')
sfgraph.par('depth',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgraph.par('symbolsz',rsf.doc.rsfpar('floats','','','''symbol size (default is 2)  [n2]'''))
sfgraph.par('scalebar',rsf.doc.rsfpar('bool','n','','''if y, draw scalebar '''))
sfgraph.par('wantframenum',rsf.doc.rsfpar('bool','(bool) (n3 > 1)','','''if y, display third axis position in the corner '''))
sfgraph.par('nreserve',rsf.doc.rsfpar('int','8','','''reserved colors '''))
sfgraph.par('minval',rsf.doc.rsfpar('float','','','''minimum value for scalebar (default is the data minimum) '''))
sfgraph.par('maxval',rsf.doc.rsfpar('float','','','''maximum value for scalebar (default is the data maximum) '''))
sfgraph.par('barreverse',rsf.doc.rsfpar('bool','n','','''if y, go from small to large on the bar scale '''))
sfgraph.par('pclip',rsf.doc.rsfpar('float','100.','','''clip percentile '''))
sfgraph.par('transp',rsf.doc.rsfpar('bool','n','','''if y, transpose the axes '''))
sfgraph.par('depth',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfgraph.par('color',rsf.doc.rsfpar('string ',desc='''color scheme (default is j) '''))
sfgraph.par('bar',rsf.doc.rsfpar('string ',desc='''file for scalebar data '''))
sfgraph.par('symbol',rsf.doc.rsfpar('string ',desc='''if set, plot with symbols instead of lines '''))
sfgraph.version('1.7 graph.c 13354 2014-10-06 13:02:12Z sfomel')
sfgraph.synopsis('''sfgraph < in.rsf depth=depth.rsf symbolsz= scalebar=n wantframenum=(bool) (n3 > 1) nreserve=8 minval= maxval= barreverse=n pclip=100. transp=n color= bar= symbol= > plot.vpl''','''Run "sfdoc stdplot" for more parameters.

August 2011 program of the month:
http://ahay.org/rsflog/index.php?/archives/266-Program-of-the-month-sfgraph.html
''')
rsf.doc.progs['sfgraph']=sfgraph

