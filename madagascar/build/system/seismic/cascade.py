sfcascade = rsf.doc.rsfprog('sfcascade','system/seismic/Mcascade.c','''Velocity partitioning for cascaded migrations. ''')
sfcascade.par('ntcut',rsf.doc.rsfpar('ints','','',''' [ncut]'''))
sfcascade.par('tcut',rsf.doc.rsfpar('floats','','','''time cuts  [ncut]'''))
sfcascade.par('ncut',rsf.doc.rsfpar('int','1','','''number of cuts '''))
sfcascade.version('1.7')
sfcascade.synopsis('''sfcascade < in.rsf > out.rsf ntcut= tcut= ncut=1''','''''')
rsf.doc.progs['sfcascade']=sfcascade

