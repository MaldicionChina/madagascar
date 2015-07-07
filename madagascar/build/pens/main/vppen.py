sfvppen = rsf.doc.rsfprog('sfvppen','pens/main/Mvppen.c','''Vplot filter for the virtual vplot device.''')
sfvppen.par('gridnum',rsf.doc.rsfpar('ints','','','''( gridnum grids the screen, each part has gridsize=xwidth,ywidth
      numy defaults to numx. [xy]size default to [xy]screensize /
      num[xy] ) [2]'''))
sfvppen.par('gridsize',rsf.doc.rsfpar('floats','','',''' [2]'''))
sfvppen.par('colormask',rsf.doc.rsfpar('bools','','',''' [5]'''))
sfvppen.par('red',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfvppen.par('green',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfvppen.par('blue',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfvppen.par('dumb',rsf.doc.rsfpar('bool','n','','''if y, causes output to only be vectors, erases, and color changes '''))
sfvppen.par('blast',rsf.doc.rsfpar('bool','y','','''if y, don't try to compact the output.  If n, compaction will
       be done.  Compaction does run-length encoding and compacts repeated
       lines.  Compaction can make the vplot file considerably smaller, but
       it also takes longer to create the file. '''))
sfvppen.par('bit',rsf.doc.rsfpar('int','0','','''if > 0,  then bit raster is used with bit the color '''))
sfvppen.par('grid',rsf.doc.rsfpar('int','-1','','''turns on drawing a grid, with the specified fatness '''))
sfvppen.par('xsize',rsf.doc.rsfpar('float','0.','',''''''))
sfvppen.par('ysize',rsf.doc.rsfpar('float','0.','','''scale the vplot image to fit within a given size rectangle '''))
sfvppen.par('big',rsf.doc.rsfpar('bool','','','''if y, expand the size of the device's screen (and hence
       outermost clipping window) to nearly infinity (bad for rotated
       style!) '''))
sfvppen.par('vpstyle',rsf.doc.rsfpar('bool','','','''if n, omit declaring absolute style in the output file '''))
sfvppen.par('mono',rsf.doc.rsfpar('bool','n','','''no color '''))
sfvppen.par('endpause',rsf.doc.rsfpar('bool','','',''''''))
sfvppen.par('cachepipe',rsf.doc.rsfpar('bool','','',''''''))
sfvppen.par('shade',rsf.doc.rsfpar('bool','','',''''''))
sfvppen.par('wantras',rsf.doc.rsfpar('bool','','',''''''))
sfvppen.par('window',rsf.doc.rsfpar('bool','','',''''''))
sfvppen.par('frame',rsf.doc.rsfpar('bool','','',''''''))
sfvppen.par('overlay',rsf.doc.rsfpar('bool','','',''''''))
sfvppen.par('invras',rsf.doc.rsfpar('bool','','',''''''))
sfvppen.par('txsquare',rsf.doc.rsfpar('bool','','',''''''))
sfvppen.par('serifs',rsf.doc.rsfpar('bool','','',''''''))
sfvppen.par('background',rsf.doc.rsfpar('bool','','',''''''))
sfvppen.par('redpow',rsf.doc.rsfpar('float','1.0','',''''''))
sfvppen.par('greenpow',rsf.doc.rsfpar('float','1.0','',''''''))
sfvppen.par('bluepow',rsf.doc.rsfpar('float','1.0','',''''''))
sfvppen.par('dither',rsf.doc.rsfpar('int','','','''dithering to improve raster display, see "man vplotraster"
                    0    No dither,
                    1    Random Dither
                    2    Ordered Dither
                    3    Minimized Average Error Method
                    4    Digital Halftoning '''))
sfvppen.par('greyc',rsf.doc.rsfpar('float','','','''"grey correction" modifies the grey scale used to display a raster to simulate the nonlinearity of displays, see "man vplotraster" '''))
sfvppen.par('pixc',rsf.doc.rsfpar('float','','','''"pixel  correction" controls  alteration of the grey scale, see "man vplotraster". '''))
sfvppen.par('txfont',rsf.doc.rsfpar('int','','',''''''))
sfvppen.par('txprec',rsf.doc.rsfpar('int','','',''''''))
sfvppen.par('txovly',rsf.doc.rsfpar('int','','',''''''))
sfvppen.par('xcenter',rsf.doc.rsfpar('float','','',''''''))
sfvppen.par('ycenter',rsf.doc.rsfpar('float','','',''''''))
sfvppen.par('patternmult',rsf.doc.rsfpar('float','1.','',''''''))
sfvppen.par('pause',rsf.doc.rsfpar('int','0','',''''''))
sfvppen.par('fatmult',rsf.doc.rsfpar('float','','',''''''))
sfvppen.par('rotate',rsf.doc.rsfpar('int','0','',''''''))
sfvppen.par('txscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfvppen.par('mkscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfvppen.par('dashscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfvppen.par('scale',rsf.doc.rsfpar('float','1.0','',''''''))
sfvppen.par('xscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfvppen.par('yscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfvppen.par('xshift',rsf.doc.rsfpar('float','0.','',''''''))
sfvppen.par('yshift',rsf.doc.rsfpar('float','0.','',''''''))
sfvppen.par('xwmax',rsf.doc.rsfpar('float','','',''''''))
sfvppen.par('ywmax',rsf.doc.rsfpar('float','','',''''''))
sfvppen.par('xwmin',rsf.doc.rsfpar('float','','',''''''))
sfvppen.par('ywmin',rsf.doc.rsfpar('float','','',''''''))
sfvppen.par('fat',rsf.doc.rsfpar('int','0','','''base line fatness '''))
sfvppen.par('gridnum',rsf.doc.rsfpar('ints','','','''grids the screen, each part has gridsize=xwidth,ywidth
      numy defaults to numx. [xy]size default to [xy]screensize /
      num[xy]  [2]'''))
sfvppen.par('stat',rsf.doc.rsfpar('string','n','','''if y, print plot statistics; if l, insert extra spaces '''))
sfvppen.par('out#',rsf.doc.rsfpar('string','','','''redirect frame # to corresponding file '''))
sfvppen.par('stat',rsf.doc.rsfpar('string ',desc='''if y, print plot statistics; if l, insert extra spaces'''))
sfvppen.par('align',rsf.doc.rsfpar('string ',desc='''aligns plot accoording to xy:
       x is one of l, r, c, u for left, right, center, unaligned
       y is one of b, t, c, u for bottom, top, center, unaligned.
       In all cases the given point is aligned to have coordinate zero. '''))
sfvppen.par('outN',rsf.doc.rsfpar('string ',desc=''''''))
sfvppen.par('erase',rsf.doc.rsfpar('string ',desc=''''''))
sfvppen.par('break',rsf.doc.rsfpar('string ',desc=''''''))
sfvppen.par('interact',rsf.doc.rsfpar('string ',desc=''''''))
sfvppen.par('style',rsf.doc.rsfpar('string ',desc=''''''))
sfvppen.par('size',rsf.doc.rsfpar('string ',desc=''''''))
sfvppen.version('1.7')
sfvppen.synopsis('''sfvppen gridnum= gridsize= colormask= red= green= blue= dumb=n blast=y bit=0 grid=-1 xsize=0. ysize=0. big= vpstyle= mono=n endpause= cachepipe= shade= wantras= window= frame= overlay= invras= txsquare= serifs= background= redpow=1.0 greenpow=1.0 bluepow=1.0 dither= greyc= pixc= txfont= txprec= txovly= xcenter= ycenter= patternmult=1. pause=0 fatmult= rotate=0 txscale=1.0 mkscale=1.0 dashscale=1.0 scale=1.0 xscale=1.0 yscale=1.0 xshift=0. yshift=0. xwmax= ywmax= xwmin= ywmin= fat=0 gridnum= stat=n out#= align= outN= erase= break= interact= style= size=''','''
Although it is perhaps not obvious, this program can be used to
"Capture the screen". Ie, you play with Pen options until you
get something you like, and then you can use those options with
this program to make a new vplot file that without any options
will draw the same thing.
''')
rsf.doc.progs['sfvppen']=sfvppen

