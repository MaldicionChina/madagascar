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

