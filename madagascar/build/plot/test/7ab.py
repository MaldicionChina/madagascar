vp7ab = rsf.doc.rsfprog('vp7ab','plot/test/7ab.c','''''')
vp7ab.par('c',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
vp7ab.par('d',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
vp7ab.par('top',rsf.doc.rsfpar('float','5.','',''''''))
vp7ab.par('c1',rsf.doc.rsfpar('float','0.5','',''''''))
vp7ab.par('c2',rsf.doc.rsfpar('float','5.','',''''''))
vp7ab.par('c',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
vp7ab.par('d',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
vp7ab.version('1.7 7ab.c 7107 2011-04-10 02:04:14Z ivlad')
vp7ab.synopsis('''vp7ab c=c.rsf d=d.rsf > plot.vpl top=5. c1=0.5 c2=5.''','''''')
rsf.doc.progs['vp7ab']=vp7ab

