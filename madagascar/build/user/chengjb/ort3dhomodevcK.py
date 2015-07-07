sfort3dhomodevcK = rsf.doc.rsfprog('sfort3dhomodevcK','user/chengjb/Mort3dhomodevcK.c','''Correct projection deviation in K-domian for 3-D pseudo-pure P-wave field in homogeneous ORT media.''')
sfort3dhomodevcK.par('apvy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3dhomodevcK.par('apvz',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3dhomodevcK.par('PseudoPurePx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3dhomodevcK.par('PseudoPurePy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3dhomodevcK.par('PseudoPurePz',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfort3dhomodevcK.par('PseudoPureSepP',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfort3dhomodevcK.version('1.7')
sfort3dhomodevcK.synopsis('''sfort3dhomodevcK < Fix.rsf apvy=Fiy.rsf apvz=Fiz.rsf PseudoPurePx=Fi1.rsf PseudoPurePy=Fi2.rsf PseudoPurePz=Fi3.rsf > Fo1.rsf PseudoPureSepP=Fo2.rsf''','''
   Refernces:
             Cheng et al. (15th IWSA, 2012);
             Cheng and Kang (SEG Abstract, 2012);
             Kang and Cheng (SEG Abstract, 2012)
             Wang et al.(SEG Abstract, 2012)      

   Copyright (C) 2012 Tongji University, Shanghai, China 

   Authors: Jiubing Cheng, Tengfei Wang and Wei Kang
     
   This code is first written by Tengfei Wang at Tongji University,
   and then optimzied by Jiubing Cheng for Madagascar version at BEG,
   University of Texas at Austin.

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
rsf.doc.progs['sfort3dhomodevcK']=sfort3dhomodevcK

