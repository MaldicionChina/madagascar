sfshotprop = rsf.doc.rsfprog('sfshotprop','system/seismic/Mshotprop.c','''Shot propagation. ''')
sfshotprop.par('ns',rsf.doc.rsfpar('int','','','''number of shots '''))
sfshotprop.par('ds',rsf.doc.rsfpar('float','','','''shot sampling '''))
sfshotprop.par('eps',rsf.doc.rsfpar('float','0.1','','''regularization parameter '''))
sfshotprop.par('positive',rsf.doc.rsfpar('bool','y','','''initial offset orientation '''))
sfshotprop.version('1.7')
sfshotprop.synopsis('''sfshotprop < in.rsf > out.rsf ns= ds= eps=0.1 positive=y''','''''')
rsf.doc.progs['sfshotprop']=sfshotprop

