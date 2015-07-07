sfstoltstretch = rsf.doc.rsfprog('sfstoltstretch','system/seismic/Mstoltstretch.c','''Stolt stretch. ''')
sfstoltstretch.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfstoltstretch.par('inv',rsf.doc.rsfpar('bool','n','','''if y, inverse stretch '''))
sfstoltstretch.par('nstretch',rsf.doc.rsfpar('int','1','','''number of steps '''))
sfstoltstretch.par('pad',rsf.doc.rsfpar('int','nt','','''time axis padding '''))
sfstoltstretch.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfstoltstretch.par('vel',rsf.doc.rsfpar('float','','','''reference velocity '''))
sfstoltstretch.version('1.7')
sfstoltstretch.synopsis('''sfstoltstretch < in.rsf > st.rsf velocity=vel.rsf inv=n nstretch=1 pad=nt eps=0.01 vel=''','''''')
rsf.doc.progs['sfstoltstretch']=sfstoltstretch

