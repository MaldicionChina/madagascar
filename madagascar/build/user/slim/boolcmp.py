sfboolcmp = rsf.doc.rsfprog('sfboolcmp','user/slim/Mboolcmp.c','''Element-wise boolean comparison of values. For int/float/complex data-sets.''')
sfboolcmp.par('right_f',rsf.doc.rsfpar('float','','','''compare input (left) to a single float value (right) '''))
sfboolcmp.par('eps',rsf.doc.rsfpar('float','0','','''comparing within this range epsilon '''))
sfboolcmp.par('right',rsf.doc.rsfpar('string ',desc='''the rsf file you will be comparing to '''))
sfboolcmp.par('sign',rsf.doc.rsfpar('string ',desc=''''eq'(default),'gt','ge','lq','lt','ne'
        sign=   'eq' equal-to ( == )
        sign=   'gt' greater-than ( > )
        sign=   'ge' greater-than or equal-to ( >= )
        sign=   'lq' less-than or equal-to ( <= )
        sign=   'lt' less-than ( < )
        sign=   'ne' not-equal ( != )
	sign=   'and' the values are both non-zero ( && )
	sign=   'or' one value is non-zero ( !! )
    '''))
sfboolcmp.version('1.7')
sfboolcmp.synopsis('''sfboolcmp < in.rsf > out.rsf right_f= eps=0 right= sign=''','''This program will solve the solution to this problem:
    - [input] [sign] [right]
    - sfboolcmp <left.rsf sign=ge right=right.rsf 
    - left.rsf >= right.rsf
This will return a vector of same length as left and return 0's or 1's depending on the result of the inequality.  Optionally you can supply a right_f parameter to compare the input data to a single value.

Written by: C. Brown, UBC
Created: Nov 2007
''')
rsf.doc.progs['sfboolcmp']=sfboolcmp

