sfkdmig2d = rsf.doc.rsfprog('sfkdmig2d','su/main/kdmig2d.c','''2-D Prestack Kirchhoff depth migration (SU version). ''')
sfkdmig2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfkdmig2d.par('dxm',rsf.doc.rsfpar('float','0.5*ds','','''sampling interval of midpoints '''))
sfkdmig2d.par('rscale',rsf.doc.rsfpar('float','RSCALE_KDMIG','','''scaling for roundoff error suppression '''))
sfkdmig2d.par('nxo',rsf.doc.rsfpar('int','(nxt-1)*2+1','','''number of output traces '''))
sfkdmig2d.par('fxo',rsf.doc.rsfpar('float','fxt','','''x-coordinate of first output trace '''))
sfkdmig2d.par('dxo',rsf.doc.rsfpar('float','dxt*0.5','','''horizontal spacing of output trace '''))
sfkdmig2d.par('nzo',rsf.doc.rsfpar('int','(nzt-1)*5+1','','''number of points in output trace '''))
sfkdmig2d.par('fzo',rsf.doc.rsfpar('float','fzt','','''z-coordinate of first point in output trace '''))
sfkdmig2d.par('dzo',rsf.doc.rsfpar('float','dzt*0.2','','''vertical spacing of output trace '''))
sfkdmig2d.par('v0',rsf.doc.rsfpar('float','1.5','','''reference velocity value at surface '''))
sfkdmig2d.par('dvz',rsf.doc.rsfpar('float','0','','''reference velocity vertical gradient '''))
sfkdmig2d.par('angmax',rsf.doc.rsfpar('float','60.','','''migration angle aperature from vertical '''))
sfkdmig2d.par('aperx',rsf.doc.rsfpar('float','0.5*nxt*dxt','','''migration lateral aperature '''))
sfkdmig2d.par('offmax',rsf.doc.rsfpar('float','3.0','','''maximum absolute offset allowed in migration '''))
sfkdmig2d.par('fmax',rsf.doc.rsfpar('float','0.25/dt','','''frequency-highcut for input traces '''))
sfkdmig2d.par('noff',rsf.doc.rsfpar('int','1','','''number of offsets in output '''))
sfkdmig2d.par('off0',rsf.doc.rsfpar('float','0.','','''first offest in output '''))
sfkdmig2d.par('doff',rsf.doc.rsfpar('float','0.1','','''offset increment in output '''))
sfkdmig2d.par('ls',rsf.doc.rsfpar('int','1','','''flag for line source '''))
sfkdmig2d.par('absoff',rsf.doc.rsfpar('int','0','','''1 - use absolute value of offset, 0 - use offset =gx-sx '''))
sfkdmig2d.par('limoff',rsf.doc.rsfpar('int','0','','''1 - limit traces used by offset, 0 - use all traces '''))
sfkdmig2d.par('ntr',rsf.doc.rsfpar('int','sf_leftsize (infp, 1)','','''maximum number of input traces to be migrated '''))
sfkdmig2d.par('mtr',rsf.doc.rsfpar('int','100','','''print verbal information at every mtr traces '''))
sfkdmig2d.par('npv',rsf.doc.rsfpar('int','0','','''1 - compute quantities for velocity analysis '''))
sfkdmig2d.par('ttfile',rsf.doc.rsfpar('string ',desc='''input traveltime tables '''))
sfkdmig2d.par('tvfile',rsf.doc.rsfpar('string ',desc='''input file of traveltime variation tables '''))
sfkdmig2d.par('csfile',rsf.doc.rsfpar('string ',desc='''input file of cosine tables '''))
sfkdmig2d.par('outfile1',rsf.doc.rsfpar('string ',desc='''file containning additional migration output '''))
sfkdmig2d.version('1.7')
sfkdmig2d.synopsis('''sfkdmig2d < infp.rsf > outfp.rsf verb=n dxm=0.5*ds rscale=RSCALE_KDMIG nxo=(nxt-1)*2+1 fxo=fxt dxo=dxt*0.5 nzo=(nzt-1)*5+1 fzo=fzt dzo=dzt*0.2 v0=1.5 dvz=0 angmax=60. aperx=0.5*nxt*dxt offmax=3.0 fmax=0.25/dt noff=1 off0=0. doff=0.1 ls=1 absoff=0 limoff=0 ntr=sf_leftsize (infp, 1) mtr=100 npv=0 ttfile= tvfile= csfile= outfile1=''','''''')
rsf.doc.progs['sfkdmig2d']=sfkdmig2d

