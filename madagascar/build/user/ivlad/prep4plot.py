sfprep4plot = rsf.doc.rsfprog('sfprep4plot','user/ivlad/Mprep4plot.py','''Resamples a 2-D dataset to the desired picture resolution, with antialias''')
sfprep4plot.par('inp',rsf.doc.rsfpar('string','','','''input file'''))
sfprep4plot.par('out',rsf.doc.rsfpar('string','','','''output file'''))
sfprep4plot.par('verb',rsf.doc.rsfpar('bool','n','','''if y, print system commands, outputs'''))
sfprep4plot.par('h',rsf.doc.rsfpar('int','768','','''output height'''))
sfprep4plot.par('w',rsf.doc.rsfpar('int','1024','','''output width'''))
sfprep4plot.par('h',rsf.doc.rsfpar('string','','',''''''))
sfprep4plot.par('w',rsf.doc.rsfpar('string','','',''''''))
sfprep4plot.par('unit',rsf.doc.rsfpar('string','px','','''unit of h and w. Can be: px, mm, cm, in'''))
sfprep4plot.par('ppi',rsf.doc.rsfpar('int','','','''outp. resolution (px/in). Necessary when unit!=px'''))
sfprep4plot.par('prar',rsf.doc.rsfpar('bool','y','','''if y, PReserve Aspect Ratio of input'''))
sfprep4plot.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfprep4plot')
sfprep4plot.version('1.7')
sfprep4plot.synopsis('''sfprep4plot inp= out= verb=n h=768 w=1024 h= w= unit=px ppi= prar=y''','''Only one of the h and w parameters needs to be specified.
If prar=n, no action will be taken on axis for which h/w was not specified
If prar=y and only one par (h or w) is specified, the picture will scale
along both axes until it is of the specified dimension.''')
rsf.doc.progs['sfprep4plot']=sfprep4plot

