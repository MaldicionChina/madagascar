#ifndef __ASG_SELFDOC__
#define __ASG_SELFDOC__

const char * sdoc[] = {
  " Acoustic variable density staggered grid finite difference modeling, ",
  " linearized modeling, and adjoint linearized modeling (RTM) in 2D or 3D.", 
  " ",
  " Authors: Igor Terentyev, Tanya Vdovina, Xin Wang, Rami Nammour, Dong Sun,",
  "   Mario J. Bencomo, Muhong Zhou, Yin Huang, and William W. Symes",
  " ",
  " Typical parameter list. May be copied, edited, and used for input: either",
  " include parameters on command line (for example in Flow), or place",
  " in file <foo> and include \"par=<foo>\" on command line. Any parameter",
  " included explicitly in command line overrides parameter with same key",
  " in par file.",
  " ",
  "  Invoke single threaded execution by ",
  " ",
  " \"sfacd [parameters]  [Madagascar install - scons in $RSFSRC]\"",
  " ",
  " or ",
  " ",
  " \"$RSFSRC/trip/iwave/asg/main/asg.x [parameters] [standalone",
  "    install - scons in $RSFSRC/trip]\"",
  " ",
  " where $RSFSRC is the path to the Madagascar source directory.",
  " Multi-threaded execution using interactive or batch MPI requires,",
  " standalone install with MPI enabled - see examples in $RSFSRC/trip/admin.",
  " ",
  " Given parameter values are defaults; non-optional values indicated by corner",
  " brackets.",
  " ",
  " --------------------------- begin parameters ---------------------------",
  " Mapping Selection:",
  " ",
  "          deriv = 0           order of derivative of forward map to compute",
  "        adjoint = 0           0: forward, 1: adjoint  ",
  " ",
  " ------------------------------------------------------------------------",
  " FD info:",
  " ",
  "          order = 2           spatial half-order",
  "            cfl = 0.75        proportion of max dt/dx",
  "           cmin = 1.0         min permitted velocity (m/ms) - sanity check",
  "           cmax = 4.5         max permitted velocity (m/ms) - used in dt comp",
  "           dmin = 0.8         min permitted density (g/cm^3) - sanity check",
  "           dmax = 3.0         min permitted density (g/cm^3) - sanity check",
  " ",
  " ------------------------------------------------------------------------",
  " Source info:",
  " ",
  "         source = <path>      path to input source data file (traces), ",
  "                              SU format, source position(s) indicated by",
  "                              RECEIVER coordinates (gx, gy, gelev) - may",
  "                              prepare input source with correct headers",
  "                              using trace/main/towed_array.x. Source acts",
  "                              as constitutive law defect, in pressure update.",
  "        sampord = 1           spatial interp order for sampling or adjoint",
  "                              sampling trace data to/from grid - 0 (nr nbr) ",
  "                              or 1 (multilin)",
  " ",
  " ------------------------------------------------------------------------",
  " Trace output - none, some, or all of the following options may be specified.",
  "   Traces are stored in SU format. Files must exist prior to execution. Trace",
  "   headers establish acquisition geometry. Data segments are overwritten for ",
  "   output for forward modeling (including all orders of derivative), used as",
  "   input for adjoint modeling.",
  " ",
  " NOTE: at least one fwd output file (trace or movie) must be specified.",
  " ",
  "        data_p  = <path>      pressure",
  "        data_v0 = <path>      z component of velocity",
  "        data_v1 = <path>      x component of velocity",
  "        data_v2 = <path>      y component of velocity",
  " ",
  " ------------------------------------------------------------------------",
  " Movie output - none, some, or all of the following options may be specified.",
  "   Movies are stored in RSF format. Files must exist prior to execution. For n",
  "   dimensional simulation, first n axes should be spatial, in same order and",
  "   with same step (but possibly different origin and length) as spatial axes",
  "   of primary model grid. Axis n is time, specifies movie frame time interval",
  "   time of first frame, and duration of simulation.",
  " ",
  " NOTE: at least one fwd output file (trace or movie) must be specified.",
  " ",
  "       movie_p  = <path>      pressure",
  "       movie_v0 = <path>      z component of velocity",
  "       movie_v1 = <path>      x component of velocity",
  "       movie_v2 = <path>      y component of velocity",
  " ",
  " ------------------------------------------------------------------------",
  " Model info:",
  " ",
  "   Basic modeling input:",
  "        bulkmod = <path>      input bulk modulus reference file, ",
  "                              determines simulation spatial grid,",
  "       buoyancy = <path>      input buoyancy (1/density) reference file, ",
  "                              must us same spatial grid as bulkmod",
  "   Derivatives: ",
  "     Forward derivative (linearized modeling): supply input model perturbations,",
  "     one for each component for first derivative, two for second derivative.",
  "     Keys for input perturbation files append _d1, _d2, etc. Thus second derivative",
  "     requires bulkmod_d1, bulkdmod_d2, buoyancy_d1, buoyancy_d2, for example.",
  "  ",
  "     Adjoint derivatives (adjoint modeling, RTM): supply output model perturbations,",
  "     one for each component for the first derivative, two for the second derivative.",
  "     Keys for output perturbation files append _b1, _b2, etc.",
  " ",
  "   NOTE: file format is RSF, and files (even output files!) must exist prior to ",
  "     execution - header file supplies geometry, data file is input (forward) or ",
  "     overwritten (adjoint)",
  " ",
  " ------------------------------------------------------------------------",
  " PML info:",
  " ",
  "  nl[d], nr[d]  = 0.0         left, right PML layer widths in dimension",
  "                              d = 1, 2, 3. If layer width on a face of the",
  "                              simulation hypercube is = 0, then Dirichlet",
  "                              (zero pressure) boundary condition is applied",
  "                              on that face. Effective absorption appears to",
  "                              require roughly 1/2 longest significant wave-",
  "                              length. Unit = m",
  "        pmlampl = 1.0         multiplier of PML absorption profile. 1.0 ",
  "                              appears to work well with 1/2 wavelength layer.",
  " ",
  " ------------------------------------------------------------------------",
  " MPI info:",
  " ",
  "        mpi_np1 = 1           number of subdomains along axis 1",
  "        mpi_np2 = 1           number of subdomains along axis 2",
  "        mpi_np3 = 1           number of subdomains along axis 3",
  "        partask = 1           number of shots to execute in parallel",
  " ",
  " ------------------------------------------------------------------------",
  " Output info:",
  " ",
  " FD ouput - written to coutxxx.txt on rank xxx",
  "       printact = 0           output at every time step",
  "                              0 - none",
  "                              1 - time step index",
  "                              2 - diagnostic messages from main routines",
  "                              > 2 - much more, useful only for serious ",
  "                                 debugging",
  "        dump_pi = 0           dump parallel/dom. decomp info",
  "       dump_lda = 0           dump grid data for allocated arrays",
  "       dump_ldc = 0           dump grid data for computational arrays",
  "       dump_ldr = 0           dump grid data for receive buffers",
  "       dump_lds = 0           dump grid data for send buffers",
  "      dump_term = 0           dump trace header data",
  " ",
  " ---------------------------end parameters ------------------------------",
  NULL };

#endif
