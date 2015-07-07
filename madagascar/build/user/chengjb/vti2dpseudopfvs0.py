sfvti2dpseudopfvs0 = rsf.doc.rsfprog('sfvti2dpseudopfvs0','user/chengjb/Mvti2dpseudopfvs0.c','''2-D two-components wavefield modeling using pseudo-pure mode P-wave equation in VTI media.''')
sfvti2dpseudopfvs0.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2dpseudopfvs0.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvti2dpseudopfvs0.par('PseudoPurePz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudopfvs0.par('PseudoPureP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudopfvs0.par('Fvs0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudopfvs0.par('apvx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudopfvs0.par('apvz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudopfvs0.par('apvxx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudopfvs0.par('apvzz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudopfvs0.par('PseudoPureSepP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvti2dpseudopfvs0.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sfvti2dpseudopfvs0.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sfvti2dpseudopfvs0.par('isep',rsf.doc.rsfpar('int','0','','''if isep=1, separate wave-modes '''))
sfvti2dpseudopfvs0.par('ihomo',rsf.doc.rsfpar('int','0','','''if ihomo=1, homogeneous medium '''))
sfvti2dpseudopfvs0.par('itaper',rsf.doc.rsfpar('int','0','','''if itaper=1, taper the operator '''))
sfvti2dpseudopfvs0.par('nstep',rsf.doc.rsfpar('int','1','','''grid step to calculate operators: 1<=nstep<=5 '''))
sfvti2dpseudopfvs0.par('tapertype',rsf.doc.rsfpar('string ',desc='''taper type'''))
sfvti2dpseudopfvs0.version('1.7')
sfvti2dpseudopfvs0.synopsis('''sfvti2dpseudopfvs0 < Fvp0.rsf epsi=Feps.rsf del=Fdel.rsf > Fo1.rsf PseudoPurePz=Fo2.rsf PseudoPureP=Fo3.rsf Fvs0=Fo4.rsf apvx=Fo5.rsf apvz=Fo6.rsf apvxx=Fo7.rsf apvzz=Fo8.rsf PseudoPureSepP=Fo9.rsf ns=301 dt=0.001 isep=0 ihomo=0 itaper=0 nstep=1 tapertype=''','''   with finite nonzero vs0

   Copyright (C) 2012 Tongji University, Shanghai, China 
   Authors: Jiubing Cheng and Wei Kang
     
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
rsf.doc.progs['sfvti2dpseudopfvs0']=sfvti2dpseudopfvs0

