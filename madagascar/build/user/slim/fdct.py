sffdct = rsf.doc.rsfprog('sffdct','user/slim/Mfdct.py','''''')
sffdct.par('nbs',rsf.doc.rsfpar('int','4','','''number of scale for the decomposition'''))
sffdct.par('nba',rsf.doc.rsfpar('int','8','','''number of angle at the 2nd coarsest scale'''))
sffdct.par('ac',rsf.doc.rsfpar('bool','1','','''curvelets at finest scale'''))
sffdct.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint transform'''))
sffdct.version('1.7')
sffdct.synopsis('''sffdct nbs=4 nba=8 ac=1 adj=n''','''Madagascar wrapper to the Fast Discrete Curvelet Transform (FDCT)

Requirements:
- Python API enable in Madagascar
- PyCurveLab (https://wave.eos.ubc.ca/Software/Licenced/)
- CurveLab (http://www.curvelet.org/)
''')
rsf.doc.progs['sffdct']=sffdct

