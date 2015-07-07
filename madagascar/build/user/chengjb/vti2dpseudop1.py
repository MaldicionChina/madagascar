sfvti2dpseudop1 = rsf.doc.rsfprog('sfvti2dpseudop1','user/chengjb/Mvti2dpseudop1.c','''2-D two-components wavefield modeling using pseudo-pure mode P-wave equation in VTI media.''')
sfvti2dpseudop1.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2dpseudop1.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2dpseudop1.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2dpseudop1.par('PseudoPurePz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('PseudoPureP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('adx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('adz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('apx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('apz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('apvx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('apvz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('adxx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('adzz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('apxx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('apzz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('apvxx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('apvzz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('PseudoPureSepP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudop1.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sfvti2dpseudop1.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sfvti2dpseudop1.par('isep',rsf.doc.rsfpar('int','0','','''if isep=1, separate wave-modes '''))
sfvti2dpseudop1.par('ihomo',rsf.doc.rsfpar('int','0','','''if ihomo=1, homogeneous medium '''))
sfvti2dpseudop1.par('itaper',rsf.doc.rsfpar('int','0','','''if itaper=1, taper the wavenumber domain p=operators'''))
sfvti2dpseudop1.par('nstep',rsf.doc.rsfpar('int','2','',''''''))
sfvti2dpseudop1.par('tapertype',rsf.doc.rsfpar('string ',desc='''taper type'''))
sfvti2dpseudop1.version('1.7')
sfvti2dpseudop1.synopsis('''sfvti2dpseudop1 < Fvp0.rsf vs0=Fvs0.rsf epsi=Feps.rsf del=Fdel.rsf > Fo1.rsf PseudoPurePz=Fo2.rsf PseudoPureP=Fo3.rsf adx=Fo4.rsf adz=Fo5.rsf apx=Fo6.rsf apz=Fo7.rsf apvx=Fo8.rsf apvz=Fo9.rsf adxx=Fo10.rsf adzz=Fo11.rsf apxx=Fo12.rsf apzz=Fo13.rsf apvxx=Fo14.rsf apvzz=Fo15.rsf PseudoPureSepP=Fo16.rsf ns=301 dt=0.001 isep=0 ihomo=0 itaper=0 nstep=2 tapertype=''','''
   Copyright (C) 2012 Tongji University, Shanghai, China 
   Authors: Jiubing Cheng, Wei Kang and Tengfei Wang
     
   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2 of the License, or
   (at your option) any later version.
             
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
                   
   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sfvti2dpseudop1']=sfvti2dpseudop1

