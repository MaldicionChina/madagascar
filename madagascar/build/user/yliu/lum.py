sflum = rsf.doc.rsfprog('sflum','user/yliu/Mlum.c','''1D LUM filter''')
sflum.par('nfw',rsf.doc.rsfpar('int','','','''filter-window length (positive and odd integer)'''))
sflum.par('smnclip',rsf.doc.rsfpar('int','(nfw+1)/2','','''smoother tuning parameter (1 <= smnclip <= (nfw+1)/2, the default is (nfw+1)/2)'''))
sflum.par('shnclip',rsf.doc.rsfpar('int','(nfw+1)/2','','''sharpener tuning parameter (1 <= shnclip <= (nfw+1)/2, the default is (nfw+1)/2)'''))
sflum.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sflum.version('1.7 Mlum.c 7107 2011-04-10 02:04:14Z ivlad')
sflum.synopsis('''sflum < in.rsf > out.rsf nfw= smnclip=(nfw+1)/2 shnclip=(nfw+1)/2 boundary=n''','''''')
rsf.doc.progs['sflum']=sflum

