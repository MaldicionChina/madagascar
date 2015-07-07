import rsf.doc

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

sfxtpen = rsf.doc.rsfprog('sfxtpen','pens/main/Mxtpen.c','''Vplot filter for X windows using the X Toolkit (Xt). ''')
sfxtpen.par('colormask',rsf.doc.rsfpar('bools','','',''' [5]'''))
sfxtpen.par('red',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfxtpen.par('green',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfxtpen.par('blue',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfxtpen.par('pause',rsf.doc.rsfpar('int','','',''''''))
sfxtpen.par('depth',rsf.doc.rsfpar('int','app_data.vis_depth','','''Choose a visual '''))
sfxtpen.par('aspect',rsf.doc.rsfpar('float','','','''aspect ratio '''))
sfxtpen.par('ppi',rsf.doc.rsfpar('float','','','''pixels per inch '''))
sfxtpen.par('numcol',rsf.doc.rsfpar('int','app_data.num_col','','''number of colors (take a default from the resource database) '''))
sfxtpen.par('buttons',rsf.doc.rsfpar('bool','(bool) app_data.buttons','','''if y, display a panel of buttons on top of the plot '''))
sfxtpen.par('labels',rsf.doc.rsfpar('bool','(bool) app_data.labels','','''if y, display frame number and inter-frame delay at the top of plot '''))
sfxtpen.par('want_text',rsf.doc.rsfpar('bool','(bool) app_data.textpane','','''if y, display a message window '''))
sfxtpen.par('stretchy',rsf.doc.rsfpar('bool','(bool) app_data.stretchy','','''if y, use the stretchy mode and fill the window '''))
sfxtpen.par('boxy',rsf.doc.rsfpar('bool','n','','''output coordinates and labels suitable for sfbox '''))
sfxtpen.par('see_progress',rsf.doc.rsfpar('bool','n','','''show progress of each frame, slow '''))
sfxtpen.par('images',rsf.doc.rsfpar('bool','(bool) app_data.images','','''copy the image created by plotting each frame and save it in
       the client program (xtpen). This will increase memory usage in
       the machine that runs the pen command. If you have a fast
       connection to your X-server it will make redisplay of frames
       faster. If you have a slow connection, it may make replotting
       slower. '''))
sfxtpen.par('pixmaps',rsf.doc.rsfpar('bool','(bool) app_data.pixmaps','','''Copy the image created by plotting each frame and save it in
       the X-server. This will increase memory usage of the machine that
       displays the window! Redisplay of frames will be very fast and
       the network traffic is very low so this is a suitable option for
       slow connections.  If your X-server is a workstation with plenty
       of memory and swap space then this option should be very useful.
       If your X-server has limited memory, this option may have
       undesirable effects on the response of your terminal. '''))
sfxtpen.par('mono',rsf.doc.rsfpar('bool','n','','''no color '''))
sfxtpen.par('endpause',rsf.doc.rsfpar('bool','','',''''''))
sfxtpen.par('cachepipe',rsf.doc.rsfpar('bool','','',''''''))
sfxtpen.par('shade',rsf.doc.rsfpar('bool','','',''''''))
sfxtpen.par('wantras',rsf.doc.rsfpar('bool','','',''''''))
sfxtpen.par('window',rsf.doc.rsfpar('bool','','',''''''))
sfxtpen.par('frame',rsf.doc.rsfpar('bool','','',''''''))
sfxtpen.par('overlay',rsf.doc.rsfpar('bool','','',''''''))
sfxtpen.par('invras',rsf.doc.rsfpar('bool','','',''''''))
sfxtpen.par('txsquare',rsf.doc.rsfpar('bool','','',''''''))
sfxtpen.par('serifs',rsf.doc.rsfpar('bool','','',''''''))
sfxtpen.par('background',rsf.doc.rsfpar('bool','','',''''''))
sfxtpen.par('redpow',rsf.doc.rsfpar('float','1.0','',''''''))
sfxtpen.par('greenpow',rsf.doc.rsfpar('float','1.0','',''''''))
sfxtpen.par('bluepow',rsf.doc.rsfpar('float','1.0','',''''''))
sfxtpen.par('dither',rsf.doc.rsfpar('int','','','''dithering to improve raster display, see "man vplotraster"
                    0    No dither,
                    1    Random Dither
                    2    Ordered Dither
                    3    Minimized Average Error Method
                    4    Digital Halftoning '''))
sfxtpen.par('greyc',rsf.doc.rsfpar('float','','','''"grey correction" modifies the grey scale used to display a raster to simulate the nonlinearity of displays, see "man vplotraster" '''))
sfxtpen.par('pixc',rsf.doc.rsfpar('float','','','''"pixel  correction" controls  alteration of the grey scale, see "man vplotraster". '''))
sfxtpen.par('txfont',rsf.doc.rsfpar('int','','',''''''))
sfxtpen.par('txprec',rsf.doc.rsfpar('int','','',''''''))
sfxtpen.par('txovly',rsf.doc.rsfpar('int','','',''''''))
sfxtpen.par('xcenter',rsf.doc.rsfpar('float','','',''''''))
sfxtpen.par('ycenter',rsf.doc.rsfpar('float','','',''''''))
sfxtpen.par('patternmult',rsf.doc.rsfpar('float','1.','',''''''))
sfxtpen.par('pause',rsf.doc.rsfpar('int','0','',''''''))
sfxtpen.par('fatmult',rsf.doc.rsfpar('float','','',''''''))
sfxtpen.par('rotate',rsf.doc.rsfpar('int','0','',''''''))
sfxtpen.par('txscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfxtpen.par('mkscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfxtpen.par('dashscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfxtpen.par('scale',rsf.doc.rsfpar('float','1.0','',''''''))
sfxtpen.par('xscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfxtpen.par('yscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfxtpen.par('xshift',rsf.doc.rsfpar('float','0.','',''''''))
sfxtpen.par('yshift',rsf.doc.rsfpar('float','0.','',''''''))
sfxtpen.par('xwmax',rsf.doc.rsfpar('float','','',''''''))
sfxtpen.par('ywmax',rsf.doc.rsfpar('float','','',''''''))
sfxtpen.par('xwmin',rsf.doc.rsfpar('float','','',''''''))
sfxtpen.par('ywmin',rsf.doc.rsfpar('float','','',''''''))
sfxtpen.par('fat',rsf.doc.rsfpar('int','0','','''base line fatness '''))
sfxtpen.par('interact',rsf.doc.rsfpar('string ',desc='''* save the command line arguments
     '''))
sfxtpen.par('message',rsf.doc.rsfpar('string ',desc=''''''))
sfxtpen.par('bgcolor',rsf.doc.rsfpar('string ',desc='''background color '''))
sfxtpen.par('erase',rsf.doc.rsfpar('string ',desc=''''''))
sfxtpen.par('break',rsf.doc.rsfpar('string ',desc=''''''))
sfxtpen.par('interact',rsf.doc.rsfpar('string ',desc='''* save the command line arguments'''))
sfxtpen.par('style',rsf.doc.rsfpar('string ',desc=''''''))
sfxtpen.par('size',rsf.doc.rsfpar('string ',desc=''''''))
sfxtpen.version('1.7')
sfxtpen.synopsis('''sfxtpen colormask= red= green= blue= pause= depth=app_data.vis_depth aspect= ppi= numcol=app_data.num_col buttons=(bool) app_data.buttons labels=(bool) app_data.labels want_text=(bool) app_data.textpane stretchy=(bool) app_data.stretchy boxy=n see_progress=n images=(bool) app_data.images pixmaps=(bool) app_data.pixmaps mono=n endpause= cachepipe= shade= wantras= window= frame= overlay= invras= txsquare= serifs= background= redpow=1.0 greenpow=1.0 bluepow=1.0 dither= greyc= pixc= txfont= txprec= txovly= xcenter= ycenter= patternmult=1. pause=0 fatmult= rotate=0 txscale=1.0 mkscale=1.0 dashscale=1.0 scale=1.0 xscale=1.0 yscale=1.0 xshift=0. yshift=0. xwmax= ywmax= xwmin= ywmin= fat=0 interact= message= bgcolor= erase= break= style= size=''','''
    This pen takes all the standard X-toolkit options
    E.g. -geometry 500x400 -font fixed

    The pen has two display modes

    RUNNING MODE: Runs through all the frames in a loop
    Active buttons are:
    QUIT : quits the program
    STOP : enter frame mode

    FRAME MODE (pause=-1): Pauses after each frame
    Active buttons are:
    NEXT : next frame
    PREV : previous frame
    QUIT : quits the program
    RESTART : go to the first frame
    RUN  : enter running mode
    STRETCHY/RIGID : make plot fill the frame or preserve aspect ratio
    FORWARDS/BACKWARDS/BOTH-WAYS : change direction of frame flipping
    Note that a backwards run will only show those frames already plotted
    It is advisable to run once through all the frames forwards.

    The following actions are available for binding to keystrokes;
    xt_quit(): quit program   xt_next(): next frame   xt_prev(): prev frame
    xt_run(): run mode        xt_stop(): frame mode   xt_restart(): first frame
    xt_faster(): reduce pause between frames in run mode
    xt_slower(): increase pause between frames in run mode
    xt_stretchy(): toggle between stretchy and rigid modes
    xt_number(digit): enter a digit in the current number
    xt_reset_number(): reset the current number
    xt_goto_frame(): goto the frame number given by the current number
    xt_print_coord(): Print mouse coords in the file given by interact=

    The default key bindings are:
    <Btn1Down>:            xt_print_coord()  \n\
    <KeyPress>n:           xt_stop() xt_reset_number() xt_next()  \n\
    <KeyPress>m:           xt_stop() xt_reset_number() xt_prev()  \n\
    <KeyPress>r:           xt_run()  \n\
    <KeyPress>q:           xt_quit()  \n\
    <KeyPress>.:           xt_stop()  \n\
    <KeyPress>f:           xt_faster()  \n\
    <KeyPress>s:           xt_slower()  \n\
    <KeyPress>t:           xt_stretchy()  \n\
    <KeyPress>0:           xt_number(0)  \n\
    ......                  .......
    <KeyPress>9:           xt_number(9)  \n\
    <KeyPress>Return:      xt_goto_frame() xt_reset_number()  \n\
    <KeyPress>Escape:      xt_reset_number()

    Here is an example of overriding these in your ~/.Xdefaults file
    this binds the keypad number 1 to skip to the first frame
    xtpen*translations: #override\n\
    <KeyPress>Q:       xt_quit() \n\
    <KeyPress>KP_1:       xt_number(1) xt_goto_frame() xt_reset_number()

    N.B using prev when you are at the first frame takes you to the last
    frame plotted so far; this is not necessarily the last frame!
    You can only jump to a frame if it has already been plotted once.
    If you give an invalid frame number it will jump to the next frame.

    Many parameters may have their defaults set in the Xresource database
    Here are the equivalent names:
    option name          X-Resource name         Type
    ===========          ===============         ====
    stretchy              XTpen.stretchy         Boolean
    images                XTpen.useImages        Boolean
    pixmaps               XTpen.usePixmaps       Boolean
    buttons               XTpen.showButtons      Boolean
    labels                XTpen.showLabels       Boolean
    want_text             XTpen.showText         Boolean
    numcol                XTpen.numCol           int
    pause                 XTpen.pause            int
 
    E.g. If you want xtpen to come up in stretchy mode as a default
    put this line in your Xdefaults file:
    XTpen.stretchy: True
''')
rsf.doc.progs['sfxtpen']=sfxtpen

sfx11pen = rsf.doc.rsfprog('sfx11pen','pens/main/Mx11pen.c','''Vplot filter for X-Window ''')
sfx11pen.par('colormask',rsf.doc.rsfpar('bools','','',''' [5]'''))
sfx11pen.par('red',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfx11pen.par('green',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfx11pen.par('blue',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfx11pen.par('stay',rsf.doc.rsfpar('bool','n','','''open terminal to count keys '''))
sfx11pen.par('width',rsf.doc.rsfpar('float','','',''''''))
sfx11pen.par('height',rsf.doc.rsfpar('float','','',''''''))
sfx11pen.par('mono',rsf.doc.rsfpar('bool','n','','''no color '''))
sfx11pen.par('endpause',rsf.doc.rsfpar('bool','','',''''''))
sfx11pen.par('cachepipe',rsf.doc.rsfpar('bool','','',''''''))
sfx11pen.par('shade',rsf.doc.rsfpar('bool','','',''''''))
sfx11pen.par('wantras',rsf.doc.rsfpar('bool','','',''''''))
sfx11pen.par('window',rsf.doc.rsfpar('bool','','',''''''))
sfx11pen.par('frame',rsf.doc.rsfpar('bool','','',''''''))
sfx11pen.par('overlay',rsf.doc.rsfpar('bool','','',''''''))
sfx11pen.par('invras',rsf.doc.rsfpar('bool','','',''''''))
sfx11pen.par('txsquare',rsf.doc.rsfpar('bool','','',''''''))
sfx11pen.par('serifs',rsf.doc.rsfpar('bool','','',''''''))
sfx11pen.par('background',rsf.doc.rsfpar('bool','','',''''''))
sfx11pen.par('redpow',rsf.doc.rsfpar('float','1.0','',''''''))
sfx11pen.par('greenpow',rsf.doc.rsfpar('float','1.0','',''''''))
sfx11pen.par('bluepow',rsf.doc.rsfpar('float','1.0','',''''''))
sfx11pen.par('dither',rsf.doc.rsfpar('int','','','''dithering to improve raster display, see "man vplotraster"
                    0    No dither,
                    1    Random Dither
                    2    Ordered Dither
                    3    Minimized Average Error Method
                    4    Digital Halftoning '''))
sfx11pen.par('greyc',rsf.doc.rsfpar('float','','','''"grey correction" modifies the grey scale used to display a raster to simulate the nonlinearity of displays, see "man vplotraster" '''))
sfx11pen.par('pixc',rsf.doc.rsfpar('float','','','''"pixel  correction" controls  alteration of the grey scale, see "man vplotraster". '''))
sfx11pen.par('txfont',rsf.doc.rsfpar('int','','',''''''))
sfx11pen.par('txprec',rsf.doc.rsfpar('int','','',''''''))
sfx11pen.par('txovly',rsf.doc.rsfpar('int','','',''''''))
sfx11pen.par('xcenter',rsf.doc.rsfpar('float','','',''''''))
sfx11pen.par('ycenter',rsf.doc.rsfpar('float','','',''''''))
sfx11pen.par('patternmult',rsf.doc.rsfpar('float','1.','',''''''))
sfx11pen.par('pause',rsf.doc.rsfpar('int','0','',''''''))
sfx11pen.par('fatmult',rsf.doc.rsfpar('float','','',''''''))
sfx11pen.par('rotate',rsf.doc.rsfpar('int','0','',''''''))
sfx11pen.par('txscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfx11pen.par('mkscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfx11pen.par('dashscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfx11pen.par('scale',rsf.doc.rsfpar('float','1.0','',''''''))
sfx11pen.par('xscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfx11pen.par('yscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfx11pen.par('xshift',rsf.doc.rsfpar('float','0.','',''''''))
sfx11pen.par('yshift',rsf.doc.rsfpar('float','0.','',''''''))
sfx11pen.par('xwmax',rsf.doc.rsfpar('float','','',''''''))
sfx11pen.par('ywmax',rsf.doc.rsfpar('float','','',''''''))
sfx11pen.par('xwmin',rsf.doc.rsfpar('float','','',''''''))
sfx11pen.par('ywmin',rsf.doc.rsfpar('float','','',''''''))
sfx11pen.par('fat',rsf.doc.rsfpar('int','0','','''base line fatness '''))
sfx11pen.par('align',rsf.doc.rsfpar('string ',desc=''''''))
sfx11pen.par('server',rsf.doc.rsfpar('string ',desc='''X server '''))
sfx11pen.par('erase',rsf.doc.rsfpar('string ',desc=''''''))
sfx11pen.par('break',rsf.doc.rsfpar('string ',desc=''''''))
sfx11pen.par('interact',rsf.doc.rsfpar('string ',desc=''''''))
sfx11pen.par('style',rsf.doc.rsfpar('string ',desc=''''''))
sfx11pen.par('size',rsf.doc.rsfpar('string ',desc=''''''))
sfx11pen.version('1.7')
sfx11pen.synopsis('''sfx11pen colormask= red= green= blue= stay=n width= height= mono=n endpause= cachepipe= shade= wantras= window= frame= overlay= invras= txsquare= serifs= background= redpow=1.0 greenpow=1.0 bluepow=1.0 dither= greyc= pixc= txfont= txprec= txovly= xcenter= ycenter= patternmult=1. pause=0 fatmult= rotate=0 txscale=1.0 mkscale=1.0 dashscale=1.0 scale=1.0 xscale=1.0 yscale=1.0 xshift=0. yshift=0. xwmax= ywmax= xwmin= ywmin= fat=0 align= server= erase= break= interact= style= size=''','''''')
rsf.doc.progs['sfx11pen']=sfx11pen

sfpspen = rsf.doc.rsfprog('sfpspen','pens/main/Mpspen.c','''Vplot filter for Postscript. ''')
sfpspen.par('colormask',rsf.doc.rsfpar('bools','','',''' [5]'''))
sfpspen.par('red',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfpspen.par('green',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfpspen.par('blue',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfpspen.par('ppi',rsf.doc.rsfpar('float','','','''pixels per inch '''))
sfpspen.par('dumbfat',rsf.doc.rsfpar('bool','n','',''''''))
sfpspen.par('color',rsf.doc.rsfpar('bool','n','','''use color '''))
sfpspen.par('force',rsf.doc.rsfpar('bool','n','','''if y, don't replace colors with their compliments '''))
sfpspen.par('forcebw',rsf.doc.rsfpar('bool','n','','''if y, don't replace black and white colors with their compliments '''))
sfpspen.par('force_raster',rsf.doc.rsfpar('bool','y','','''if y, don't replace raster colors with their compliments '''))
sfpspen.par('rgb',rsf.doc.rsfpar('bool','y','','''For figures turned into GEOPHYSICS, use "rgb=no". '''))
sfpspen.par('tex',rsf.doc.rsfpar('bool','n','',''''''))
sfpspen.par('hold',rsf.doc.rsfpar('bool','n','','''tells the printer to not print the job until you
       add paper through the manual feed slot '''))
sfpspen.par('copies',rsf.doc.rsfpar('int','1','','''number of copies '''))
sfpspen.par('corners',rsf.doc.rsfpar('bool','y','','''n - remove "corner" group. '''))
sfpspen.par('mono',rsf.doc.rsfpar('bool','n','','''no color '''))
sfpspen.par('endpause',rsf.doc.rsfpar('bool','','',''''''))
sfpspen.par('cachepipe',rsf.doc.rsfpar('bool','','',''''''))
sfpspen.par('shade',rsf.doc.rsfpar('bool','','',''''''))
sfpspen.par('wantras',rsf.doc.rsfpar('bool','','',''''''))
sfpspen.par('window',rsf.doc.rsfpar('bool','','',''''''))
sfpspen.par('frame',rsf.doc.rsfpar('bool','','',''''''))
sfpspen.par('overlay',rsf.doc.rsfpar('bool','','',''''''))
sfpspen.par('invras',rsf.doc.rsfpar('bool','','',''''''))
sfpspen.par('txsquare',rsf.doc.rsfpar('bool','','',''''''))
sfpspen.par('serifs',rsf.doc.rsfpar('bool','','',''''''))
sfpspen.par('background',rsf.doc.rsfpar('bool','','',''''''))
sfpspen.par('redpow',rsf.doc.rsfpar('float','1.0','',''''''))
sfpspen.par('greenpow',rsf.doc.rsfpar('float','1.0','',''''''))
sfpspen.par('bluepow',rsf.doc.rsfpar('float','1.0','',''''''))
sfpspen.par('dither',rsf.doc.rsfpar('int','','','''dithering to improve raster display, see "man vplotraster"
                    0    No dither,
                    1    Random Dither
                    2    Ordered Dither
                    3    Minimized Average Error Method
                    4    Digital Halftoning '''))
sfpspen.par('greyc',rsf.doc.rsfpar('float','','','''"grey correction" modifies the grey scale used to display a raster to simulate the nonlinearity of displays, see "man vplotraster" '''))
sfpspen.par('pixc',rsf.doc.rsfpar('float','','','''"pixel  correction" controls  alteration of the grey scale, see "man vplotraster". '''))
sfpspen.par('txfont',rsf.doc.rsfpar('int','','',''''''))
sfpspen.par('txprec',rsf.doc.rsfpar('int','','',''''''))
sfpspen.par('txovly',rsf.doc.rsfpar('int','','',''''''))
sfpspen.par('xcenter',rsf.doc.rsfpar('float','','',''''''))
sfpspen.par('ycenter',rsf.doc.rsfpar('float','','',''''''))
sfpspen.par('patternmult',rsf.doc.rsfpar('float','1.','',''''''))
sfpspen.par('pause',rsf.doc.rsfpar('int','0','',''''''))
sfpspen.par('fatmult',rsf.doc.rsfpar('float','','',''''''))
sfpspen.par('rotate',rsf.doc.rsfpar('int','0','',''''''))
sfpspen.par('txscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfpspen.par('mkscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfpspen.par('dashscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfpspen.par('scale',rsf.doc.rsfpar('float','1.0','',''''''))
sfpspen.par('xscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfpspen.par('yscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfpspen.par('xshift',rsf.doc.rsfpar('float','0.','',''''''))
sfpspen.par('yshift',rsf.doc.rsfpar('float','0.','',''''''))
sfpspen.par('xwmax',rsf.doc.rsfpar('float','','',''''''))
sfpspen.par('ywmax',rsf.doc.rsfpar('float','','',''''''))
sfpspen.par('xwmin',rsf.doc.rsfpar('float','','',''''''))
sfpspen.par('ywmin',rsf.doc.rsfpar('float','','',''''''))
sfpspen.par('fat',rsf.doc.rsfpar('int','0','','''base line fatness '''))
sfpspen.par('printer',rsf.doc.rsfpar('string ',desc='''what printer to send it to '''))
sfpspen.par('paper',rsf.doc.rsfpar('string ',desc=''''''))
sfpspen.par('label',rsf.doc.rsfpar('string ',desc=''''''))
sfpspen.par('erase',rsf.doc.rsfpar('string ',desc=''''''))
sfpspen.par('break',rsf.doc.rsfpar('string ',desc=''''''))
sfpspen.par('interact',rsf.doc.rsfpar('string ',desc=''''''))
sfpspen.par('style',rsf.doc.rsfpar('string ',desc=''''''))
sfpspen.par('size',rsf.doc.rsfpar('string ',desc=''''''))
sfpspen.version('1.7')
sfpspen.synopsis('''sfpspen colormask= red= green= blue= ppi= dumbfat=n color=n force=n forcebw=n force_raster=y rgb=y tex=n hold=n copies=1 corners=y mono=n endpause= cachepipe= shade= wantras= window= frame= overlay= invras= txsquare= serifs= background= redpow=1.0 greenpow=1.0 bluepow=1.0 dither= greyc= pixc= txfont= txprec= txovly= xcenter= ycenter= patternmult=1. pause=0 fatmult= rotate=0 txscale=1.0 mkscale=1.0 dashscale=1.0 scale=1.0 xscale=1.0 yscale=1.0 xshift=0. yshift=0. xwmax= ywmax= xwmin= ywmin= fat=0 printer= paper= label= erase= break= interact= style= size=''','''
   output is in PostScript language; if not redirected, it is sent to
   lpr -Ppostscript   (override with $PSPRINTER environment variable.)
''')
rsf.doc.progs['sfpspen']=sfpspen

sfraspen = rsf.doc.rsfprog('sfraspen','pens/main/Mraspen.c','''vplot filter for ppm format output. ''')
sfraspen.par('colormask',rsf.doc.rsfpar('bools','','',''' [5]'''))
sfraspen.par('red',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfraspen.par('green',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfraspen.par('blue',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfraspen.par('aspect',rsf.doc.rsfpar('float','','','''aspect ratio '''))
sfraspen.par('ppi',rsf.doc.rsfpar('float','','','''pixels per inch '''))
sfraspen.par('n1',rsf.doc.rsfpar('int','','',''''''))
sfraspen.par('n2',rsf.doc.rsfpar('int','','','''image size '''))
sfraspen.par('mono',rsf.doc.rsfpar('bool','n','','''no color '''))
sfraspen.par('endpause',rsf.doc.rsfpar('bool','','',''''''))
sfraspen.par('cachepipe',rsf.doc.rsfpar('bool','','',''''''))
sfraspen.par('shade',rsf.doc.rsfpar('bool','','',''''''))
sfraspen.par('wantras',rsf.doc.rsfpar('bool','','',''''''))
sfraspen.par('window',rsf.doc.rsfpar('bool','','',''''''))
sfraspen.par('frame',rsf.doc.rsfpar('bool','','',''''''))
sfraspen.par('overlay',rsf.doc.rsfpar('bool','','',''''''))
sfraspen.par('invras',rsf.doc.rsfpar('bool','','',''''''))
sfraspen.par('txsquare',rsf.doc.rsfpar('bool','','',''''''))
sfraspen.par('serifs',rsf.doc.rsfpar('bool','','',''''''))
sfraspen.par('background',rsf.doc.rsfpar('bool','','',''''''))
sfraspen.par('redpow',rsf.doc.rsfpar('float','1.0','',''''''))
sfraspen.par('greenpow',rsf.doc.rsfpar('float','1.0','',''''''))
sfraspen.par('bluepow',rsf.doc.rsfpar('float','1.0','',''''''))
sfraspen.par('dither',rsf.doc.rsfpar('int','','','''dithering to improve raster display, see "man vplotraster"
                    0    No dither,
                    1    Random Dither
                    2    Ordered Dither
                    3    Minimized Average Error Method
                    4    Digital Halftoning '''))
sfraspen.par('greyc',rsf.doc.rsfpar('float','','','''"grey correction" modifies the grey scale used to display a raster to simulate the nonlinearity of displays, see "man vplotraster" '''))
sfraspen.par('pixc',rsf.doc.rsfpar('float','','','''"pixel  correction" controls  alteration of the grey scale, see "man vplotraster". '''))
sfraspen.par('txfont',rsf.doc.rsfpar('int','','',''''''))
sfraspen.par('txprec',rsf.doc.rsfpar('int','','',''''''))
sfraspen.par('txovly',rsf.doc.rsfpar('int','','',''''''))
sfraspen.par('xcenter',rsf.doc.rsfpar('float','','',''''''))
sfraspen.par('ycenter',rsf.doc.rsfpar('float','','',''''''))
sfraspen.par('patternmult',rsf.doc.rsfpar('float','1.','',''''''))
sfraspen.par('pause',rsf.doc.rsfpar('int','0','',''''''))
sfraspen.par('fatmult',rsf.doc.rsfpar('float','','',''''''))
sfraspen.par('rotate',rsf.doc.rsfpar('int','0','',''''''))
sfraspen.par('txscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfraspen.par('mkscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfraspen.par('dashscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfraspen.par('scale',rsf.doc.rsfpar('float','1.0','',''''''))
sfraspen.par('xscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfraspen.par('yscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfraspen.par('xshift',rsf.doc.rsfpar('float','0.','',''''''))
sfraspen.par('yshift',rsf.doc.rsfpar('float','0.','',''''''))
sfraspen.par('xwmax',rsf.doc.rsfpar('float','','',''''''))
sfraspen.par('ywmax',rsf.doc.rsfpar('float','','',''''''))
sfraspen.par('xwmin',rsf.doc.rsfpar('float','','',''''''))
sfraspen.par('ywmin',rsf.doc.rsfpar('float','','',''''''))
sfraspen.par('fat',rsf.doc.rsfpar('int','0','','''base line fatness '''))
sfraspen.par('bgcolor',rsf.doc.rsfpar('string ',desc='''background color '''))
sfraspen.par('erase',rsf.doc.rsfpar('string ',desc=''''''))
sfraspen.par('break',rsf.doc.rsfpar('string ',desc=''''''))
sfraspen.par('interact',rsf.doc.rsfpar('string ',desc=''''''))
sfraspen.par('style',rsf.doc.rsfpar('string ',desc=''''''))
sfraspen.par('size',rsf.doc.rsfpar('string ',desc=''''''))
sfraspen.version('1.7')
sfraspen.synopsis('''sfraspen colormask= red= green= blue= aspect= ppi= n1= n2= mono=n endpause= cachepipe= shade= wantras= window= frame= overlay= invras= txsquare= serifs= background= redpow=1.0 greenpow=1.0 bluepow=1.0 dither= greyc= pixc= txfont= txprec= txovly= xcenter= ycenter= patternmult=1. pause=0 fatmult= rotate=0 txscale=1.0 mkscale=1.0 dashscale=1.0 scale=1.0 xscale=1.0 yscale=1.0 xshift=0. yshift=0. xwmax= ywmax= xwmin= ywmin= fat=0 bgcolor= erase= break= interact= style= size=''','''''')
rsf.doc.progs['sfraspen']=sfraspen

sfgdpen = rsf.doc.rsfprog('sfgdpen','pens/main/Mgdpen.c','''vplot filter for LibGD. ''')
sfgdpen.par('colormask',rsf.doc.rsfpar('bools','','',''' [5]'''))
sfgdpen.par('red',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfgdpen.par('green',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfgdpen.par('blue',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfgdpen.par('aspect',rsf.doc.rsfpar('float','','','''aspect ratio '''))
sfgdpen.par('ppi',rsf.doc.rsfpar('float','','','''pixels per inch '''))
sfgdpen.par('n1',rsf.doc.rsfpar('int','','',''''''))
sfgdpen.par('n2',rsf.doc.rsfpar('int','','','''image size '''))
sfgdpen.par('delay',rsf.doc.rsfpar('int','10','','''animation delay (if type=="gif" or "mpeg") '''))
sfgdpen.par('bitrate',rsf.doc.rsfpar('int','400000','','''MPEG bitrate '''))
sfgdpen.par('mono',rsf.doc.rsfpar('bool','n','','''no color '''))
sfgdpen.par('endpause',rsf.doc.rsfpar('bool','','',''''''))
sfgdpen.par('cachepipe',rsf.doc.rsfpar('bool','','',''''''))
sfgdpen.par('shade',rsf.doc.rsfpar('bool','','',''''''))
sfgdpen.par('wantras',rsf.doc.rsfpar('bool','','',''''''))
sfgdpen.par('window',rsf.doc.rsfpar('bool','','',''''''))
sfgdpen.par('frame',rsf.doc.rsfpar('bool','','',''''''))
sfgdpen.par('overlay',rsf.doc.rsfpar('bool','','',''''''))
sfgdpen.par('invras',rsf.doc.rsfpar('bool','','',''''''))
sfgdpen.par('txsquare',rsf.doc.rsfpar('bool','','',''''''))
sfgdpen.par('serifs',rsf.doc.rsfpar('bool','','',''''''))
sfgdpen.par('background',rsf.doc.rsfpar('bool','','',''''''))
sfgdpen.par('redpow',rsf.doc.rsfpar('float','1.0','',''''''))
sfgdpen.par('greenpow',rsf.doc.rsfpar('float','1.0','',''''''))
sfgdpen.par('bluepow',rsf.doc.rsfpar('float','1.0','',''''''))
sfgdpen.par('dither',rsf.doc.rsfpar('int','','','''dithering to improve raster display, see "man vplotraster"
                    0    No dither,
                    1    Random Dither
                    2    Ordered Dither
                    3    Minimized Average Error Method
                    4    Digital Halftoning '''))
sfgdpen.par('greyc',rsf.doc.rsfpar('float','','','''"grey correction" modifies the grey scale used to display a raster to simulate the nonlinearity of displays, see "man vplotraster" '''))
sfgdpen.par('pixc',rsf.doc.rsfpar('float','','','''"pixel  correction" controls  alteration of the grey scale, see "man vplotraster". '''))
sfgdpen.par('txfont',rsf.doc.rsfpar('int','','',''''''))
sfgdpen.par('txprec',rsf.doc.rsfpar('int','','',''''''))
sfgdpen.par('txovly',rsf.doc.rsfpar('int','','',''''''))
sfgdpen.par('xcenter',rsf.doc.rsfpar('float','','',''''''))
sfgdpen.par('ycenter',rsf.doc.rsfpar('float','','',''''''))
sfgdpen.par('patternmult',rsf.doc.rsfpar('float','1.','',''''''))
sfgdpen.par('pause',rsf.doc.rsfpar('int','0','',''''''))
sfgdpen.par('fatmult',rsf.doc.rsfpar('float','','',''''''))
sfgdpen.par('rotate',rsf.doc.rsfpar('int','0','',''''''))
sfgdpen.par('txscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfgdpen.par('mkscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfgdpen.par('dashscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfgdpen.par('scale',rsf.doc.rsfpar('float','1.0','',''''''))
sfgdpen.par('xscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfgdpen.par('yscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfgdpen.par('xshift',rsf.doc.rsfpar('float','0.','',''''''))
sfgdpen.par('yshift',rsf.doc.rsfpar('float','0.','',''''''))
sfgdpen.par('xwmax',rsf.doc.rsfpar('float','','',''''''))
sfgdpen.par('ywmax',rsf.doc.rsfpar('float','','',''''''))
sfgdpen.par('xwmin',rsf.doc.rsfpar('float','','',''''''))
sfgdpen.par('ywmin',rsf.doc.rsfpar('float','','',''''''))
sfgdpen.par('fat',rsf.doc.rsfpar('int','0','','''base line fatness '''))
sfgdpen.par('bgcolor',rsf.doc.rsfpar('string ',desc='''background color (black,white,light,dark) 
       'light' and 'dark' cause the background to be transparent (in PNG and GIF) '''))
sfgdpen.par('type',rsf.doc.rsfpar('string ',desc='''image type (png, jpeg, gif, mpeg) '''))
sfgdpen.par('erase',rsf.doc.rsfpar('string ',desc=''''''))
sfgdpen.par('break',rsf.doc.rsfpar('string ',desc=''''''))
sfgdpen.par('interact',rsf.doc.rsfpar('string ',desc=''''''))
sfgdpen.par('style',rsf.doc.rsfpar('string ',desc=''''''))
sfgdpen.par('size',rsf.doc.rsfpar('string ',desc=''''''))
sfgdpen.version('1.7')
sfgdpen.synopsis('''sfgdpen colormask= red= green= blue= aspect= ppi= n1= n2= delay=10 bitrate=400000 mono=n endpause= cachepipe= shade= wantras= window= frame= overlay= invras= txsquare= serifs= background= redpow=1.0 greenpow=1.0 bluepow=1.0 dither= greyc= pixc= txfont= txprec= txovly= xcenter= ycenter= patternmult=1. pause=0 fatmult= rotate=0 txscale=1.0 mkscale=1.0 dashscale=1.0 scale=1.0 xscale=1.0 yscale=1.0 xshift=0. yshift=0. xwmax= ywmax= xwmin= ywmin= fat=0 bgcolor= type= erase= break= interact= style= size=''','''''')
rsf.doc.progs['sfgdpen']=sfgdpen

sfcrpen = rsf.doc.rsfprog('sfcrpen','pens/main/Mcrpen.c','''vplot filter for Cairo Graphics. ''')
sfcrpen.par('colormask',rsf.doc.rsfpar('bools','','',''' [5]'''))
sfcrpen.par('red',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfcrpen.par('green',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfcrpen.par('blue',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfcrpen.par('aspect',rsf.doc.rsfpar('float','','','''aspect ratio '''))
sfcrpen.par('ppi',rsf.doc.rsfpar('float','','','''pixels per inch '''))
sfcrpen.par('n1',rsf.doc.rsfpar('int','','',''''''))
sfcrpen.par('n2',rsf.doc.rsfpar('int','','','''image size '''))
sfcrpen.par('mono',rsf.doc.rsfpar('bool','n','','''no color '''))
sfcrpen.par('endpause',rsf.doc.rsfpar('bool','','',''''''))
sfcrpen.par('cachepipe',rsf.doc.rsfpar('bool','','',''''''))
sfcrpen.par('shade',rsf.doc.rsfpar('bool','','',''''''))
sfcrpen.par('wantras',rsf.doc.rsfpar('bool','','',''''''))
sfcrpen.par('window',rsf.doc.rsfpar('bool','','',''''''))
sfcrpen.par('frame',rsf.doc.rsfpar('bool','','',''''''))
sfcrpen.par('overlay',rsf.doc.rsfpar('bool','','',''''''))
sfcrpen.par('invras',rsf.doc.rsfpar('bool','','',''''''))
sfcrpen.par('txsquare',rsf.doc.rsfpar('bool','','',''''''))
sfcrpen.par('serifs',rsf.doc.rsfpar('bool','','',''''''))
sfcrpen.par('background',rsf.doc.rsfpar('bool','','',''''''))
sfcrpen.par('redpow',rsf.doc.rsfpar('float','1.0','',''''''))
sfcrpen.par('greenpow',rsf.doc.rsfpar('float','1.0','',''''''))
sfcrpen.par('bluepow',rsf.doc.rsfpar('float','1.0','',''''''))
sfcrpen.par('dither',rsf.doc.rsfpar('int','','','''dithering to improve raster display, see "man vplotraster"
                    0    No dither,
                    1    Random Dither
                    2    Ordered Dither
                    3    Minimized Average Error Method
                    4    Digital Halftoning '''))
sfcrpen.par('greyc',rsf.doc.rsfpar('float','','','''"grey correction" modifies the grey scale used to display a raster to simulate the nonlinearity of displays, see "man vplotraster" '''))
sfcrpen.par('pixc',rsf.doc.rsfpar('float','','','''"pixel  correction" controls  alteration of the grey scale, see "man vplotraster". '''))
sfcrpen.par('txfont',rsf.doc.rsfpar('int','','',''''''))
sfcrpen.par('txprec',rsf.doc.rsfpar('int','','',''''''))
sfcrpen.par('txovly',rsf.doc.rsfpar('int','','',''''''))
sfcrpen.par('xcenter',rsf.doc.rsfpar('float','','',''''''))
sfcrpen.par('ycenter',rsf.doc.rsfpar('float','','',''''''))
sfcrpen.par('patternmult',rsf.doc.rsfpar('float','1.','',''''''))
sfcrpen.par('pause',rsf.doc.rsfpar('int','0','',''''''))
sfcrpen.par('fatmult',rsf.doc.rsfpar('float','','',''''''))
sfcrpen.par('rotate',rsf.doc.rsfpar('int','0','',''''''))
sfcrpen.par('txscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfcrpen.par('mkscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfcrpen.par('dashscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfcrpen.par('scale',rsf.doc.rsfpar('float','1.0','',''''''))
sfcrpen.par('xscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfcrpen.par('yscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfcrpen.par('xshift',rsf.doc.rsfpar('float','0.','',''''''))
sfcrpen.par('yshift',rsf.doc.rsfpar('float','0.','',''''''))
sfcrpen.par('xwmax',rsf.doc.rsfpar('float','','',''''''))
sfcrpen.par('ywmax',rsf.doc.rsfpar('float','','',''''''))
sfcrpen.par('xwmin',rsf.doc.rsfpar('float','','',''''''))
sfcrpen.par('ywmin',rsf.doc.rsfpar('float','','',''''''))
sfcrpen.par('fat',rsf.doc.rsfpar('int','0','','''base line fatness '''))
sfcrpen.par('bgcolor',rsf.doc.rsfpar('string ',desc='''background color (black,white,light,dark) 
       'light' and 'dark' cause the background to be transparent (in PNG and GIF) '''))
sfcrpen.par('erase',rsf.doc.rsfpar('string ',desc=''''''))
sfcrpen.par('break',rsf.doc.rsfpar('string ',desc=''''''))
sfcrpen.par('interact',rsf.doc.rsfpar('string ',desc=''''''))
sfcrpen.par('style',rsf.doc.rsfpar('string ',desc=''''''))
sfcrpen.par('size',rsf.doc.rsfpar('string ',desc=''''''))
sfcrpen.version('1.7')
sfcrpen.synopsis('''sfcrpen colormask= red= green= blue= aspect= ppi= n1= n2= mono=n endpause= cachepipe= shade= wantras= window= frame= overlay= invras= txsquare= serifs= background= redpow=1.0 greenpow=1.0 bluepow=1.0 dither= greyc= pixc= txfont= txprec= txovly= xcenter= ycenter= patternmult=1. pause=0 fatmult= rotate=0 txscale=1.0 mkscale=1.0 dashscale=1.0 scale=1.0 xscale=1.0 yscale=1.0 xshift=0. yshift=0. xwmax= ywmax= xwmin= ywmin= fat=0 bgcolor= erase= break= interact= style= size=''','''''')
rsf.doc.progs['sfcrpen']=sfcrpen

sfoglpen = rsf.doc.rsfprog('sfoglpen','pens/main/Moglpen.c','''vplot filter for OpenGL. ''')
sfoglpen.par('colormask',rsf.doc.rsfpar('bools','','',''' [5]'''))
sfoglpen.par('red',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfoglpen.par('green',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfoglpen.par('blue',rsf.doc.rsfpar('floats','','',''' [4]'''))
sfoglpen.par('aspect',rsf.doc.rsfpar('float','','','''aspect ratio '''))
sfoglpen.par('ppi',rsf.doc.rsfpar('float','','','''pixels per inch '''))
sfoglpen.par('stretchy',rsf.doc.rsfpar('bool','n','','''y - stretch plot to all borders of the drawing area '''))
sfoglpen.par('aalias',rsf.doc.rsfpar('bool','n','','''y - draw lines, points, polygons with antialialing '''))
sfoglpen.par('aawidth',rsf.doc.rsfpar('int','1','','''width of transition areas when aalias=y '''))
sfoglpen.par('mono',rsf.doc.rsfpar('bool','n','','''no color '''))
sfoglpen.par('endpause',rsf.doc.rsfpar('bool','','',''''''))
sfoglpen.par('cachepipe',rsf.doc.rsfpar('bool','','',''''''))
sfoglpen.par('shade',rsf.doc.rsfpar('bool','','',''''''))
sfoglpen.par('wantras',rsf.doc.rsfpar('bool','','',''''''))
sfoglpen.par('window',rsf.doc.rsfpar('bool','','',''''''))
sfoglpen.par('frame',rsf.doc.rsfpar('bool','','',''''''))
sfoglpen.par('overlay',rsf.doc.rsfpar('bool','','',''''''))
sfoglpen.par('invras',rsf.doc.rsfpar('bool','','',''''''))
sfoglpen.par('txsquare',rsf.doc.rsfpar('bool','','',''''''))
sfoglpen.par('serifs',rsf.doc.rsfpar('bool','','',''''''))
sfoglpen.par('background',rsf.doc.rsfpar('bool','','',''''''))
sfoglpen.par('redpow',rsf.doc.rsfpar('float','1.0','',''''''))
sfoglpen.par('greenpow',rsf.doc.rsfpar('float','1.0','',''''''))
sfoglpen.par('bluepow',rsf.doc.rsfpar('float','1.0','',''''''))
sfoglpen.par('dither',rsf.doc.rsfpar('int','','','''dithering to improve raster display, see "man vplotraster"
                    0    No dither,
                    1    Random Dither
                    2    Ordered Dither
                    3    Minimized Average Error Method
                    4    Digital Halftoning '''))
sfoglpen.par('greyc',rsf.doc.rsfpar('float','','','''"grey correction" modifies the grey scale used to display a raster to simulate the nonlinearity of displays, see "man vplotraster" '''))
sfoglpen.par('pixc',rsf.doc.rsfpar('float','','','''"pixel  correction" controls  alteration of the grey scale, see "man vplotraster". '''))
sfoglpen.par('txfont',rsf.doc.rsfpar('int','','',''''''))
sfoglpen.par('txprec',rsf.doc.rsfpar('int','','',''''''))
sfoglpen.par('txovly',rsf.doc.rsfpar('int','','',''''''))
sfoglpen.par('xcenter',rsf.doc.rsfpar('float','','',''''''))
sfoglpen.par('ycenter',rsf.doc.rsfpar('float','','',''''''))
sfoglpen.par('patternmult',rsf.doc.rsfpar('float','1.','',''''''))
sfoglpen.par('pause',rsf.doc.rsfpar('int','0','',''''''))
sfoglpen.par('fatmult',rsf.doc.rsfpar('float','','',''''''))
sfoglpen.par('rotate',rsf.doc.rsfpar('int','0','',''''''))
sfoglpen.par('txscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfoglpen.par('mkscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfoglpen.par('dashscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfoglpen.par('scale',rsf.doc.rsfpar('float','1.0','',''''''))
sfoglpen.par('xscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfoglpen.par('yscale',rsf.doc.rsfpar('float','1.0','',''''''))
sfoglpen.par('xshift',rsf.doc.rsfpar('float','0.','',''''''))
sfoglpen.par('yshift',rsf.doc.rsfpar('float','0.','',''''''))
sfoglpen.par('xwmax',rsf.doc.rsfpar('float','','',''''''))
sfoglpen.par('ywmax',rsf.doc.rsfpar('float','','',''''''))
sfoglpen.par('xwmin',rsf.doc.rsfpar('float','','',''''''))
sfoglpen.par('ywmin',rsf.doc.rsfpar('float','','',''''''))
sfoglpen.par('fat',rsf.doc.rsfpar('int','0','','''base line fatness '''))
sfoglpen.par('bgcolor',rsf.doc.rsfpar('string ',desc='''background color (black,white,light,dark) '''))
sfoglpen.par('erase',rsf.doc.rsfpar('string ',desc=''''''))
sfoglpen.par('break',rsf.doc.rsfpar('string ',desc=''''''))
sfoglpen.par('interact',rsf.doc.rsfpar('string ',desc=''''''))
sfoglpen.par('style',rsf.doc.rsfpar('string ',desc=''''''))
sfoglpen.par('size',rsf.doc.rsfpar('string ',desc=''''''))
sfoglpen.version('1.7')
sfoglpen.synopsis('''sfoglpen colormask= red= green= blue= aspect= ppi= stretchy=n aalias=n aawidth=1 mono=n endpause= cachepipe= shade= wantras= window= frame= overlay= invras= txsquare= serifs= background= redpow=1.0 greenpow=1.0 bluepow=1.0 dither= greyc= pixc= txfont= txprec= txovly= xcenter= ycenter= patternmult=1. pause=0 fatmult= rotate=0 txscale=1.0 mkscale=1.0 dashscale=1.0 scale=1.0 xscale=1.0 yscale=1.0 xshift=0. yshift=0. xwmax= ywmax= xwmin= ywmin= fat=0 bgcolor= erase= break= interact= style= size=''','''''')
rsf.doc.progs['sfoglpen']=sfoglpen

rsf.doc.progs['sfjpegpen']=sfraspen
rsf.doc.progs['sfpen']=sfoglpen
rsf.doc.progs['sfpdfpen']=sfcrpen
rsf.doc.progs['sfppmpen']=sfraspen
rsf.doc.progs['sfsvgpen']=sfcrpen
rsf.doc.progs['sfpngpen']=sfcrpen
rsf.doc.progs['sftiffpen']=sfraspen
