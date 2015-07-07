sfgrey = rsf.doc.rsfprog('sfgrey','plot/main/grey.c','''Generate raster plot.''')
sfgrey.par('transp',rsf.doc.rsfpar('bool','y','','''if y, transpose the display axes '''))
sfgrey.par('yreverse',rsf.doc.rsfpar('bool','y','','''if y, reverse the vertical axis '''))
sfgrey.par('xreverse',rsf.doc.rsfpar('bool','n','','''if y, reverse the horizontal axis '''))
sfgrey.par('gpow',rsf.doc.rsfpar('float','','',''''''))
sfgrey.par('phalf',rsf.doc.rsfpar('float','','','''percentage for estimating gpow '''))
sfgrey.par('clip',rsf.doc.rsfpar('float','','','''data clip '''))
sfgrey.par('pclip',rsf.doc.rsfpar('float','','','''data clip percentile (default is 99) '''))
sfgrey.par('gainstep',rsf.doc.rsfpar('int','0.5+n1/256.','','''subsampling for gpow and clip estimation '''))
sfgrey.par('allpos',rsf.doc.rsfpar('bool','n','','''if y, assume positive data '''))
sfgrey.par('mean',rsf.doc.rsfpar('bool','n','','''if y, bias on the mean value '''))
sfgrey.par('bias',rsf.doc.rsfpar('float','0.','','''value mapped to the center of the color table '''))
sfgrey.par('polarity',rsf.doc.rsfpar('bool','n','','''if y, reverse polarity (white is high by default) '''))
sfgrey.par('symcp',rsf.doc.rsfpar('bool','n','','''if y, assume symmetric color palette of 255 colors '''))
sfgrey.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfgrey.par('scalebar',rsf.doc.rsfpar('bool','n','','''if y, draw scalebar '''))
sfgrey.par('minval',rsf.doc.rsfpar('float','','','''minimum value for scalebar (default is the data minimum) '''))
sfgrey.par('maxval',rsf.doc.rsfpar('float','','','''maximum value for scalebar (default is the data maximum) '''))
sfgrey.par('barreverse',rsf.doc.rsfpar('bool','n','','''if y, go from small to large on the bar scale '''))
sfgrey.par('wantframenum',rsf.doc.rsfpar('bool','(bool) (n3 > 1)','','''if y, display third axis position in the corner '''))
sfgrey.par('nreserve',rsf.doc.rsfpar('int','8','','''reserved colors '''))
sfgrey.par('gpow',rsf.doc.rsfpar('float','1','','''raise data to gpow power for display '''))
sfgrey.par('gainpanel',rsf.doc.rsfpar('string ',desc='''gain reference: 'a' for all, 'e' for each, or number '''))
sfgrey.par('bar',rsf.doc.rsfpar('string ',desc='''file for scalebar data '''))
sfgrey.par('color',rsf.doc.rsfpar('string ',desc='''color scheme (default is i) '''))
sfgrey.version('1.7')
sfgrey.synopsis('''sfgrey < in.rsf > out.rsf > bar.rsf transp=y yreverse=y xreverse=n gpow= phalf= clip= pclip= gainstep=0.5+n1/256. allpos=n mean=n bias=0. polarity=n symcp=n verb=n scalebar=n minval= maxval= barreverse=n wantframenum=(bool) (n3 > 1) nreserve=8 gpow=1 gainpanel= bar= color= > (plot.vpl | char.rsf)''','''Can input char values.
If called "byte", outputs char values.

If called "bar", outputs scalebar data.

Run "sfdoc stdplot" for more parameters.
''')
rsf.doc.progs['sfgrey']=sfgrey

