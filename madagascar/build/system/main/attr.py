sfattr = rsf.doc.rsfprog('sfattr','system/main/attr.c','''Display dataset attributes.''')
sfattr.par('lval',rsf.doc.rsfpar('int','2','','''norm option, lval is a non-negative integer, computes the vector lval-norm '''))
sfattr.par('want',rsf.doc.rsfpar('string ',desc=''''all'(default), 'rms', 'mean', 'norm', 'var', 
       'std', 'max', 'min', 'nonzero', 'samples', 'short' 
        want=   'rms' displays the root mean square
        want=   'norm' displays the square norm, otherwise specified by lval.
        want=   'var' displays the variance
        want=   'std' displays the standard deviation
        want=   'nonzero' displays number of nonzero samples
        want=   'samples' displays total number of samples
        want=   'short' displays a short one-line version
     '''))
sfattr.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfattr')
sfattr.version('1.7')
sfattr.synopsis('''sfattr < in.rsf lval=2 want=''','''
Sample output from "sfspike n1=100 | sfbandpass fhi=60 | sfattr"
*******************************************
     rms =      0.992354
    mean =      0.987576
  2-norm =       9.92354
variance =    0.00955481
 std dev =     0.0977487
     max =       1.12735 at 97
     min =      0.151392 at 100
nonzero samples = 100
  total samples = 100
*******************************************

rms                = sqrt[ sum(data^2) / n ]
mean               = sum(data) / n
norm               = sum(abs(data)^lval)^(1/lval)
variance           = [ sum(data^2) - n*mean^2 ] / [ n-1 ]
standard deviation = sqrt [ variance ]
''')
rsf.doc.progs['sfattr']=sfattr

