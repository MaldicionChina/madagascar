sfjacobi = rsf.doc.rsfprog('sfjacobi','system/generic/Mjacobi.c','''Find eigenvalues of a symmetric matrix by Jacobi's iteration. ''')
sfjacobi.par('eig',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfjacobi.par('niter',rsf.doc.rsfpar('int','10','',''''''))
sfjacobi.par('eig',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfjacobi.version('1.7')
sfjacobi.synopsis('''sfjacobi < mat.rsf > val.rsf eig=eig.rsf niter=10''','''''')
rsf.doc.progs['sfjacobi']=sfjacobi

