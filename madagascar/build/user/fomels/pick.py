sfpick = rsf.doc.rsfprog('sfpick','user/fomels/Mpick.c','''Automatic picking  from semblance-like panels. ''')
sfpick.par('vel0',rsf.doc.rsfpar('float','o2','','''surface velocity '''))
sfpick.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfpick.par('an',rsf.doc.rsfpar('float','1.','','''axes anisotropy '''))
sfpick.par('gate',rsf.doc.rsfpar('int','3','','''picking gate '''))
sfpick.par('smooth',rsf.doc.rsfpar('bool','y','','''if apply smoothing '''))
sfpick.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfpick.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfpick')
sfpick.version('1.7')
sfpick.synopsis('''sfpick < scn.rsf > pik.rsf vel0=o2 niter=100 an=1. gate=3 smooth=y rect#=(1,1,...) rect1=1 rect2=1 ...''','''rectN defines the size of the smoothing stencil in N-th dimension.

Theory in Appendix B of:
S. Fomel, 2009, 
Velocity analysis using AB semblance: Geophysical Prospecting, v. 57, 311-321.
Reproducible version in RSFSRC/book/tccs/avo 
http://ahay.org/RSF/book/tccs/avo/paper_html/

August 2012 program of the month:
http://ahay.org/rsflog/index.php?/archives/302-Program-of-the-month-sfpick.html
''')
rsf.doc.progs['sfpick']=sfpick

