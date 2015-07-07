sftti2dpseudop = rsf.doc.rsfprog('sftti2dpseudop','user/chengjb/Mtti2dpseudop.c','''2-D two-components wavefield modeling using pseudo-pure mode P-wave equation in TTI media.''')
sftti2dpseudop.par('vs0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti2dpseudop.par('epsi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti2dpseudop.par('del',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti2dpseudop.par('the',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftti2dpseudop.par('PseudoPurePz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudop.par('PseudoPureP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudop.par('apvx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudop.par('apvz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudop.par('apvxx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudop.par('apvzz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudop.par('PseudoPureSepP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftti2dpseudop.par('ns',rsf.doc.rsfpar('int','301','',''''''))
sftti2dpseudop.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sftti2dpseudop.par('isep',rsf.doc.rsfpar('int','0','','''if isep=1, separate wave-modes '''))
sftti2dpseudop.par('ihomo',rsf.doc.rsfpar('int','0','','''if ihomo=1, homogeneous medium '''))
sftti2dpseudop.par('nstep',rsf.doc.rsfpar('int','1','','''grid step to calculate operators: 1<=nstep<=5 '''))
sftti2dpseudop.par('tapertype',rsf.doc.rsfpar('string ',desc='''taper type'''))
sftti2dpseudop.version('1.7')
sftti2dpseudop.synopsis('''sftti2dpseudop < Fvp0.rsf vs0=Fvs0.rsf epsi=Feps.rsf del=Fdel.rsf the=Fthe.rsf > Fo1.rsf PseudoPurePz=Fo2.rsf PseudoPureP=Fo3.rsf apvx=Fo4.rsf apvz=Fo5.rsf apvxx=Fo6.rsf apvzz=Fo7.rsf PseudoPureSepP=Fo8.rsf ns=301 dt=0.001 isep=0 ihomo=0 nstep=1 tapertype=''','''
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
rsf.doc.progs['sftti2dpseudop']=sftti2dpseudop

