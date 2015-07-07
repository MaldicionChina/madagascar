sfintervalVTI = rsf.doc.rsfprog('sfintervalVTI','user/lcasasan/MintervalVTI.c','''Interval/Effective VTI parameters from Effective/Interval profiles ''')
sfintervalVTI.par('vH_out',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfintervalVTI.par('eta_out',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfintervalVTI.par('eta',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfintervalVTI.par('interval',rsf.doc.rsfpar('bool','y','','''output are interval [y] or effective [n] profiles '''))
sfintervalVTI.par('vH_out',rsf.doc.rsfpar('string ',desc='''output HOR vel(auxiliary output file name)'''))
sfintervalVTI.par('eta_out',rsf.doc.rsfpar('string ',desc='''output eta(auxiliary output file name)'''))
sfintervalVTI.par('eta',rsf.doc.rsfpar('string ',desc='''input eta(auxiliary input file name)'''))
sfintervalVTI.version('1.7')
sfintervalVTI.synopsis('''sfintervalVTI < vn.rsf > vn_out.rsf vH_out=vh_out.rsf eta_out=eta_out.rsf eta=eta.rsf interval=y''','''''')
rsf.doc.progs['sfintervalVTI']=sfintervalVTI

