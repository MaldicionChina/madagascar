[sfboolcmp]
Cat:    RSF/user/slim
Desc:   Element-wise boolean comparison of values. For int/float/complex data-sets
DocCmd: sfboolcmp | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eps float  -  0 		comparing within this range epsilon 
Param:  right string  -   -  		the rsf file you will be comparing to 
Param:  right_f float  -   -  		compare input (left) to a single float value (right) 
Param:  sign string  -   -  		'eq'(default),'gt','ge','lq','lt','ne'
LDesc:          sign=   'eq' equal-to ( == )
LDesc:          sign=   'gt' greater-than ( > )
LDesc:          sign=   'ge' greater-than or equal-to ( >= )
LDesc:          sign=   'lq' less-than or equal-to ( <= )
LDesc:          sign=   'lt' less-than ( < )
LDesc:          sign=   'ne' not-equal ( != )
LDesc:  	sign=   'and' the values are both non-zero ( && )
LDesc:  	sign=   'or' one value is non-zero ( !! )
LDesc:      

