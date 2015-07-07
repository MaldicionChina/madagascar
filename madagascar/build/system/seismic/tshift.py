sftshift = rsf.doc.rsfprog('sftshift','system/seismic/Mtshift.c','''Compute angle gathers for time-shift imaging condition ''')
sftshift.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftshift.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftshift.par('na',rsf.doc.rsfpar('int','nv','',''''''))
sftshift.par('da',rsf.doc.rsfpar('float','1./(nv-1)','',''''''))
sftshift.par('a0',rsf.doc.rsfpar('float','0.','',''''''))
sftshift.par('extend',rsf.doc.rsfpar('int','4','','''tmp extension '''))
sftshift.par('cos',rsf.doc.rsfpar('bool','n','','''if n, convert pseudo-v to pseudo-tan(theta); 
       if y, compute cos(theta) from 1/|pm| '''))
sftshift.version('1.7')
sftshift.synopsis('''sftshift < Fstk.rsf velocity=Fvel.rsf dip=Fdip.rsf > Fang.rsf na=nv da=1./(nv-1) a0=0. extend=4 cos=n''','''''')
rsf.doc.progs['sftshift']=sftshift

