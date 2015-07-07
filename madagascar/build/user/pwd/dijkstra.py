sfdijkstra = rsf.doc.rsfprog('sfdijkstra','user/pwd/Mdijkstra.c','''Dijkstra shortest-path algorithm in 2-D ''')
sfdijkstra.par('fin1',rsf.doc.rsfpar('ints','','',''' [nf]'''))
sfdijkstra.par('fin2',rsf.doc.rsfpar('ints','','','''final points  [nf]'''))
sfdijkstra.par('paths',rsf.doc.rsfpar('strings','','',''' [nf]'''))
sfdijkstra.par('ref1',rsf.doc.rsfpar('int','0','',''''''))
sfdijkstra.par('ref2',rsf.doc.rsfpar('int','0','','''source point '''))
sfdijkstra.par('nf',rsf.doc.rsfpar('int','0','','''number of final points '''))
sfdijkstra.version('1.7')
sfdijkstra.synopsis('''sfdijkstra < cost.rsf > out.rsf fin1= fin2= paths= ref1=0 ref2=0 nf=0''','''''')
rsf.doc.progs['sfdijkstra']=sfdijkstra

