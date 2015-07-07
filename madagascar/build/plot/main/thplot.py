sfthplot = rsf.doc.rsfprog('sfthplot','plot/main/thplot.c','''Hidden-line surface plot.''')
sfthplot.par('uflag',rsf.doc.rsfpar('bool','y','','''if y, plot upper side of the surface '''))
sfthplot.par('dflag',rsf.doc.rsfpar('bool','y','','''if y, plot down side of the surface '''))
sfthplot.par('alpha',rsf.doc.rsfpar('float','45.','','''apparent angle in degrees, |alpha| < 89 '''))
sfthplot.par('titlsz',rsf.doc.rsfpar('int','9','','''title size '''))
sfthplot.par('axissz',rsf.doc.rsfpar('int','6','','''axes size '''))
sfthplot.par('plotfat',rsf.doc.rsfpar('int','0','','''line fatness '''))
sfthplot.par('titlefat',rsf.doc.rsfpar('int','2','','''title fatness '''))
sfthplot.par('axisfat',rsf.doc.rsfpar('int','2','','''axes fatness '''))
sfthplot.par('plotcolup',rsf.doc.rsfpar('int','VP_YELLOW','','''color of the upper side '''))
sfthplot.par('plotcoldn',rsf.doc.rsfpar('int','VP_RED','','''color of the lower side '''))
sfthplot.par('wanttitle',rsf.doc.rsfpar('bool','y','',''''''))
sfthplot.par('axis',rsf.doc.rsfpar('bool','y','',''''''))
sfthplot.par('axis1',rsf.doc.rsfpar('bool','y','',''''''))
sfthplot.par('axis2',rsf.doc.rsfpar('bool','y','',''''''))
sfthplot.par('axis3',rsf.doc.rsfpar('bool','y','','''plot axis '''))
sfthplot.par('clip',rsf.doc.rsfpar('float','0.','','''data clip '''))
sfthplot.par('pclip',rsf.doc.rsfpar('float','100.','','''data clip percentile '''))
sfthplot.par('gainstep',rsf.doc.rsfpar('int','0.5+nx/256.','','''subsampling for gpow and clip estimation '''))
sfthplot.par('bias',rsf.doc.rsfpar('float','0.','','''subtract bias from data '''))
sfthplot.par('dclip',rsf.doc.rsfpar('float','1.','','''change the clip: clip *= dclip '''))
sfthplot.par('norm',rsf.doc.rsfpar('bool','y','','''normalize by the clip '''))
sfthplot.par('xc',rsf.doc.rsfpar('float','1.5','',''''''))
sfthplot.par('zc',rsf.doc.rsfpar('float','3','','''lower left corner of the plot '''))
sfthplot.par('ratio',rsf.doc.rsfpar('float','5.','','''plot adjustment '''))
sfthplot.par('zmax',rsf.doc.rsfpar('float','','',''''''))
sfthplot.par('zmin',rsf.doc.rsfpar('float','','',''''''))
sfthplot.par('sz',rsf.doc.rsfpar('float','6.','','''vertical scale '''))
sfthplot.par('title',rsf.doc.rsfpar('string ',desc=''''''))
sfthplot.version('1.7')
sfthplot.synopsis('''sfthplot < in.rsf uflag=y dflag=y alpha=45. titlsz=9 axissz=6 plotfat=0 titlefat=2 axisfat=2 plotcolup=VP_YELLOW plotcoldn=VP_RED wanttitle=y axis=y axis1=y axis2=y axis3=y clip=0. pclip=100. gainstep=0.5+nx/256. bias=0. dclip=1. norm=y xc=1.5 zc=3 ratio=5. zmax= zmin= sz=6. title= > plot.vpl ''','''''')
rsf.doc.progs['sfthplot']=sfthplot

