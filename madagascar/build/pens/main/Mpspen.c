/* Vplot filter for Postscript. 

   output is in PostScript language; if not redirected, it is sent to
   lpr -Ppostscript   (override with $PSPRINTER environment variable.)
*/
/*
  Copyright (C) 1987 The Board of Trustees of Stanford University
  
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
*/

/*
 *
 *  source file:   ./filters/pslib/psarea.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Steve Cole (SEP), March 25 1988
 *      Wrote psarea.
 * Steve Cole (SEP), March 30 1988
 *      Routine now checks for "all black" and "all white" patterns and
 *      does the fill for these using setgray rather than messing with the
 *      halftone screen.
 *      Also, when the halftone screen has been altered, the routine now
 *      saves that state and avoids having to do all the work again if the
 *      same pattern is used to fill another area.
 * Steve Cole (SEP), March 31 1988
 *      Corrected orientation of pattern. Corrected scaling bug in
 *      call to setpattern.
 * Steve Cole (SEP), October 19 1988
 *      For mono=n case added a gsave to go with the grestore.
 * Joe Dellinger (Amoco), April 25 1996
 *	Use relative moves when they save space.
 */
/*
 *
 *  source file:   ./filters/pslib/psattr.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Steve Cole (SEP), March 27 1988
 *      Routine no longer modifies the current vplot color. It modifies
 *      postscript's current color definition only. This is the way
 *      it's supposed to be done.
 * Steve Cole (SEP), March 29 1988
 *      Clipping (the SET_WINDOW case) is now supported.
 * Steve Cole (SEP), March 31 1988
 *      Dashed lines (NEW_DASH) is now supported.
 * Steve Cole (SEP), June 20 1988
 *      Dashon was incorrectly used as a local variable here. Cleaned
 *      up the clipping code some.
 * Steve Cole (SEP), August 19 1988
 *      Added newpath after setting of clipping window. Otherwise when
 *      a stroke command came along, the clipping path would be drawn in.
 * Joe Dellinger (SEP), October 19 1988
 *	Added "grey" option.
 * Steve Cole (SEP), November 1 1991
 *      Replaced grey option with proper color support. Colors are
 *      shaded in grey (like the grey option) by default in PostScript
 *      on greyscale devices.
 * Joe Dellinger (SOEST), October 15 1992
 *	After setting a new clipping window the global plot parameters
 *	line width, dash pattern, and color were being lost. (Polygon
 *	fill pattern is apparently not lost.)
 * Joe Dellinger (SOEST), October 16 1992
 *	Postscript allows through everything STRICTLY INSIDE a clipping
 *	path; the path itself is not included. Thus we have to extend the
 *	postscript clipping box by one minimal coordinate unit in each
 *	direction, because vplot assumes the edges of the clipping window
 *	ARE included.
 * Steve Cole (SEP), November 30 1992
 *      Added color raster support.
 * Joe Dellinger (Amoco), April 24 1996
 *	Wrap the stuff that needs to be done after a grestore up into
 *	a subroutine so it can be called from other routines too.
 * Joe Dellinger (Amoco), March 20 1997
 *	Don't do a grestore without a preceding gsave to go with it.
 * Joe Dellinger (BP Amoco), Oct 5 1999
 *	pspen color=y force=y should just give you the colors you ask for,
 *	period. pspen color=y force=n should give you their complements,
 *	period. Don't try to get excessively tricky flipping some colors
 *	around and not others. Some of the color versus monochrome logic
 *	was entangled.
 */
/*
 *
 *  source file:   ./filters/pslib/psclose.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Steve Cole (SEP), March 29 1988
 *	Moved showpage to pserase.
 * Joe Dellinger (SOEST), Feb 18 1992
 *	Added option for "PSPRINTER" environment variable.
 * Steve Cole (SEP), October 22 1992
 *	Added color printer support.
 * Joe Dellinger (AMOCO), March 22 1995
 *      Added custom paper size support.
 *      Added comment for Amoco users so they can see where their plot
 *      is being spooled. If you don't like that, #define NOCOMMENTS
 * Hector Urdaneta (SEP), April 26 1996
 *      Added ifdef SGI64, define NOCOMMENTS, endif 
 *      Not compiling in the SGI
 */

/*
 *
 *  source file:   ./filters/pslib/pserase.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Steve Cole (SEP), March 29 1988
 *      Added plot label.
 * Steve Cole (SEP), March 31 1988
 *      Added support for ncopies and hold command line options.
 * Dave Nichols (SEP), May 22 1990
 *	Added a grestore at the end of the page to match the gsave at the start
 *	Modified output for tex=y to be compatible with /psfig macros in TeX.
 * Joe Dellinger (SOEST), Oct 15 1992
 *	Added a grestore/gsave pair just before printing the label
 *	to turn off any clipping window which may be in effect.
 * Joe Dellinger (AMOCO), April 24 1996
 *	Paper size was not set on pages after the first.
 *	Line join type was not set if tex=y, causing "fanged S syndrome".
 *	The variable "rotate" should not have been used here.
 *	Fatness (and some other variables) needed to be reset at the
 *	beginning of each new page.
 * Joe Dellinger (AMOCO), March 20 1997
 *	If we did a gsave for a clipping window, then do a grestore
 *	here so gsaves and grestores are properly paired.
 */
/*
 *
 *  source file:   ./filters/pslib/psopen.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Steve Cole (SEP), September 15 1987
 *	Added smart_raster, mono, dither, pixc, and greyc to attributes.
 * Steve Cole (SEP), January 10 1988
 *      Vplot pen font is now default font.
 * Steve Cole (SEP), March 23 1988
 *      Default font is now vplot default hardcopy font.
 * Steve Cole (SEP), March 29 1988
 *      Added an intial gsave so that the first clipping window call
 *      will not destroy the rotation and translation done here when
 *      it tries to back out the previous clipping call.
 *	Added need_end_erase for plotting label.
 *      Corrected definition of limits of device space.
 * Steve Cole (SEP), March 31 1988
 *      The vplot to PostScript units conversion factor is computed here
 *	instead of being hardwired in many different places.
 *      Scaling is done here so that all coordinates output by pspen
 *      can be integers.
 * Joe Dellinger (SEP), October 19 1988
 *	Added "grey" and "harddither" options, fixed bugs, use "move/draw"
 *	method of sending paths.
 * Joe Dellinger (SEP), January 19 1989
 *	This is a "page type" hardcopy device;
 *	size=relative makes more sense.
 * Joe Dellinger (SEP), April 17 1990
 *	Remove pointless calloc call; "getlogin" provides its own allocation.
 * Dave Nichols (SEP), May 22 1990
 *	Changed output for tex=y to be compatible with /psfig macros in TeX.
 * Dave Nichols (SEP), Aug 14 1990
 *	Changed size of page to be maximum possible and force size=ABSOLUTE
 *	for tex=y to prevent clipping of plots off the page.
 * Steve Cole (SEP), Nov 1 1991
 *	Added color support.
 * Dave Nichols (SEP) May 2 1992
 *      Allow VPLOTSPOOLDIR environment variable to override PEN_SPOOL
 * Joe Dellinger (SOEST) Oct 15 1992
 *	The Apple LaserWriter page limits are a little more generous
 *	than the SPARC printer allows.
 * Steve Cole (SEP), Nov 30 1992
 *      Added color raster support.
 *	Added limits for Tektronix color postscript printer. These are
 *      used if pspen is invoked by the alias tcprpen, or if
 *      wstype=tcpr.
 * Ray Abma (SEP) 3 Aug 1993
 *      changed getdate to dateget to avoid conflict with HP time.h
 * David Lumley (SEP) March 7 1994
 *	added translate call so tcpr printable area doesn't get clipped
 * Joe Dellinger (AMOCO) March 22 1995
 *	Added the ability to specify a page size from the command line.
 *	Added the ability to set the default page size either by the
 *	define DEFAULT_PAPER_SIZE at compile time or by setting an
 *	environmental variable of the same name.
 *	Corrected the bug (I hope?) that caused plots to sometimes be
 *	lost if pspen was run in background from a shell after the user
 *	logged out. Added more detail to error messages.
 *	Added "oyo" option to wstype.
 * Joe Dellinger (AMOCO) April 24 1996
 *	Set line join type when tex=y too.
 *	The variable "rotate" was always zero because it hadn't been
 *	properly set yet and shouldn't have been used here.
 * Joe Dellinger (AMOCO) April 25 1996
 *	Add "s" and "r" as shorthands for "stroke" and "rlineto", respectively.
 * Joe Dellinger (AMOCO) April 26 1996
 *	Add "x" as shorthand for "0 0 rlineto" (a dot).
 * Joe Dellinger (BP Amoco) Oct 5, 1999
 *	Set the actual colors when calling psattributes (changes made
 *	there to fix a bug required a change here).
 */

/*
 *
 *  source file:   ./filters/pslib/psplot.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Joe Dellinger (SEP), October 18 1988
 *	Stole imagplot.c to make psplot.c.
 * Joe Dellinger (SEP), October 19 1988
 *	Use "move/draw" method of sending paths.
 * Steve Cole (SEP), July 27 1989
 *      Added check on PATHLENGTH to avoid too many points/path.
 * Steve Cole (SEP), August 26 1990
 *      Removed check for staying at same point in addpath. Correct
 *	vplot behavior is to plot a point in this case, not ignore it.
 * Joe Dellinger (SOEST) June 23 1992
 *	The xold, yold variables in addpath were set but never used.
 * Joe Dellinger (Amoco) April 25 1996
 *	Use "s" instead of "stroke" to save a few bytes.
 *	Use "r" (short for "rlineto") when it uses less space than
 *	"d" (short for "lineto").
 * Joe Dellinger (Amoco) April 26 1996
 *	Jon has plots that consist of zillions of dots, so try to
 *	optimize that case a little bit better. ("x" is shorthand for "0 0 r")
 */

/*
 * 
 *  source file:   ./filters/pslib/psraster.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Steve Cole (SEP), September 11 1987
 *	Wrote smart version of psraster.c.
 * Steve Cole (SEP), February 10 1988
 *      Rewrote using readhexstring instead of creating procedure for image.
 *      This avoids possible size problems.
 *	Fixed orientation problems.
 * Steve Cole (SEP), March 28 1988
 *      Simplified the handling of the raster. In this routine we want
 *      always to output bytes and let PostScript do its own dithering.
 * Steve Cole (SEP), March 31 1988
 *      Corrected polarity of output raster.
 * Joe Dellinger (SEP), October 19 1988
 *	Added "harddither" option.
 * Steve Cole (SEP), November 30 1992
 *	Added color raster support.
 * Dave Nichols (SEP), April 7 1993
 *	Made grey rasters split their lines (like color ones do)
 * Joe Dellinger, David Lumley, 10-03-94
 * 	Check external variable ras_allgrey to decide if only gray raster
 *	is needed when color is requested by the pspen color=y option.
 */

/*
 *
 *  source file:   ./filters/pslib/psreset.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Joe Dellinger (SEP), October 19 1988
 *	Added "grey" option.
 * Joe Dellinger (BP Amoco) October 5 1999
 *	Grey-level stuff should only be done for mono=y case.
 */

/*
 *
 *  source file:   ./filters/pslib/pstext.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Steve Cole (SEP), September 16 1987
 *      Font 0 is now used if an undefined font is requested.
 * Steve Cole (SEP), March 23 1988
 *      For vplot fonts, added return after gentext call.
 * Steve Cole (SEP), April 2 1988
 *      Changed scaling to agree with other routines.
 * Steve Cole (SEP), June 20 1988
 *      Removed unused array "instruction".
 * Joe Dellinger (SOEST), March 1 1993
 *	Pspen hardware fonts were coming out too small due to a bug
 *	in this routine that used to not matter. This whole routine is
 *	full of bugs, though, and should be re-written from scratch!
 *	For example it should NOT attempt to use yscale and xscale itself.
 *	That is certainly WRONG! I took that part out; better to have
 *	text always come out square than have it scaled wrongly.
 *	(Talking to postscript in terms of "orient" and "size" is pointless
 *	and awkward in any case.) The "DIFFERENT_COORDINATES" stuff was not
 *	working and not worth saving, so I made it always "true".
 */

/*
 *
 *  source file:   ./filters/pslib/psvector.c
 *
 * Joe Dellinger (SEP), June 11 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Steve Cole (SEP), March 24 1988
 *      Corrected computation of linewidth.
 * Steve Cole (SEP), March 31 1988
 *	Added line dashing logic.
 * Joe Dellinger (SEP) October 17 1988
 *	Stole imagvector.c to create psvector.c that does things with
 *	paths.
 * Joe Dellinger (SEP), October 19 1988
 *	Fixed bugs, use "move/draw" method of sending paths.
 * Aritomo Shinozaki (Loomis Laboratory of Physics), February 25 1989
 *	The code which generates dash pattern lines was incorrect.
 * Joe Dellinger (SOEST) June 23 1992
 *	Added dumb_fat option
 * Joe Dellinger (SOEST) October 15 1992
 *	No need for extra space at start of "setlinewidth" command.
 *	If the dash pattern has been completely lost (because of a
 *	grestore) call ps_set_dash to recreate it.
 */

#define mask0 ((unsigned char) (((unsigned int) 1) << 7))

#include <stdlib.h>

extern int mkstemp (char *tmpl);

#include <stdio.h>
#include <string.h>
#include <time.h>

#include <unistd.h>
#include <sys/time.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <pwd.h>

#include <rsfplot.h>

#include "../include/vertex.h"
#include "../include/extern.h"
#include "../include/err.h"
#include "../include/params.h"
#include "../include/pat.h"
#include "../include/attrcom.h"
#include "../include/enum.h"
#include "../include/closestat.h"
#include "../include/erasecom.h"
#include "../include/round.h"

#include "dovplot.h"
#include "init_vplot.h"

#include "../genlib/genpen.h"
#include "../utilities/util.h"

#include "_ps.h"
#include "psdoc.h"
#include "pspen.h"

char            name[] = "pspen";

#include "_device.h"

extern int      ipat;
extern struct pat pat[];

static bool force_color, force_bw, force_raster;
static bool dumb_fat; 
static bool rgb_colorspace;
static char *label;
extern FILE *pltout;

static int      ps_oldx = 0, ps_oldy = 0;

static bool     corners = true; /* Leaver or remove corners (sfgrey3) */
static int      iscorners = 0; /* "corner" group is acrive */
static int      corners_group = -1; /* "corner" group number */

static void rgb_to_cmyk (int red, int green, int blue,
			 int *cyan, int *magenta, int *yellow, int *black);

void psarea (int npts, struct vertex  *verlist)
/*< area >*/
{
    unsigned char   mask, outchar;
    int             nx, ny, nxold, nyold, i, ix, iy;
    int            *bptr;
    struct vertex  *v;
    static int      ever_called = 0;
    static int      error_size = 0;
    static int      error_square = 0;
    int             all_black, all_white;
    static int      last_pattern = 0;
    extern float    ps_curcolor;

    char            stringd[80];
    char            stringr[80];

    if (!corners && iscorners)
        return; /* Ignore area filling, if "corner" group is active */

    endpath ();

    if (mono)
    {
/*
 * check for "all black" or "all white" patterns. It is a waste of time
 * to do these using the halftone screen method used below, since a
 * simple "setgray" call will work just as well.
 */
	nx = pat[ipat].xdim;
	ny = pat[ipat].ydim;
	bptr = pat[ipat].patbits;
	all_black = 1;
	all_white = 1;
	for (iy = 0; iy < ny; iy++)
	{
	    for (ix = 0; ix < nx; ix++)
	    {
		if (bptr[iy * nx + ix] != 0)
		    all_white = 0;
		if (bptr[iy * nx + ix] == 0)
		    all_black = 0;
	    }
	}
/*
 * This section of this routine is borrowed from the PostScript Language
 * Cookbook put out by Adobe Systems Incorporated, program 15 "Filling an Area
 * with a Pattern". I have commented the code to indicate the purpose
 * of each section and how the sections interact, but the Cookbook includes
 * more detailed comments that anyone attempting to modify this code
 * would certainly find useful.
 *
 * setuserscreendict allocates space for the routine setuserscreen.
 * ever_called is used to ensure that we only do all this initialization
 * once.
 * we don't need to do this initialization if the pattern is all black
 * or all white, because we use setgray rather than setscreen for those.
 */
	if (all_black == 0 && all_white == 0)
	{
	    if (ever_called == 0)
	    {
		fprintf (pltout, "/setuserscreendict 22 dict def\n");
		fprintf (pltout, "setuserscreendict begin\n");
		fprintf (pltout, " /tempctm matrix def\n");
		fprintf (pltout, " /temprot matrix def\n");
		fprintf (pltout, " /tempscale matrix def\n");
		fprintf (pltout, " /concatprocs\n");
		fprintf (pltout, " {/proc2 exch cvlit def\n");
		fprintf (pltout, "  /proc1 exch cvlit def\n");
		fprintf (pltout, "  /newproc proc1 length proc2 length add\n");
		fprintf (pltout, "   array def\n");
		fprintf (pltout, "  newproc 0 proc1 putinterval\n");
		fprintf (pltout, "  newproc proc1 length proc2 putinterval\n");
		fprintf (pltout, "  newproc cvx\n");
		fprintf (pltout, " } def\n");
		fprintf (pltout, "/resmatrix matrix def\n");
		fprintf (pltout, "/findresolution\n");
		fprintf (pltout, " {72 0 resmatrix defaultmatrix dtransform\n");
		fprintf (pltout, "  /yres exch def /xres exch def\n");
		fprintf (pltout, "  xres dup mul yres dup mul add sqrt\n");
		fprintf (pltout, " } def\n");
		fprintf (pltout, "end\n");
/*
 * setuserscreen takes the desired halftone cell size and angle in the current
 * user space from the procedure "setpattern" (defined below) and converts
 * them to device space values. Then it calls the postscript procedure
 * "setscreen" to re-define the halftone screen.
 */
		fprintf (pltout, "/setuserscreen\n");
		fprintf (pltout, " {setuserscreendict begin\n");
		fprintf (pltout, "  /spotfunction exch def\n");
		fprintf (pltout, "  /screenangle exch def\n");
		fprintf (pltout, "  /cellsize exch def\n");
		fprintf (pltout, "  /m tempctm currentmatrix def\n");
		fprintf (pltout, "  /rm screenangle temprot rotate def\n");
		fprintf (pltout, "  /sm cellsize dup tempscale scale def\n");
		fprintf (pltout, "  sm rm m m concatmatrix m concatmatrix pop\n");
		fprintf (pltout, "  1 0 m dtransform /y1 exch def /x1 exch def\n");
		fprintf (pltout, "  /veclength x1 dup mul y1 dup mul add sqrt def\n");
		fprintf (pltout, "  /frequency findresolution veclength div def\n");
		fprintf (pltout, "  /newscreenangle y1 x1 atan def\n");
		fprintf (pltout, "  m 2 get m 1 get mul m 0 get m 3 get mul sub\n");
		fprintf (pltout, "   0 gt\n");
		fprintf (pltout, "  {{neg} /spotfunction load concatprocs\n");
		fprintf (pltout, "    /spotfunction exch def\n");
		fprintf (pltout, "  } if\n");
		fprintf (pltout, "  frequency newscreenangle /spotfunction load\n");
		fprintf (pltout, "   setscreen\n");
		fprintf (pltout, " end\n");
		fprintf (pltout, " } def\n");
/*
 * setpatterndict allocates space for the procedure setpattern.
 * bitpatternspotfunction is an entry in this dictionary that defines
 * the pattern. setpattern will load this and pass it to setuserscreen.
 */
		fprintf (pltout, "/setpatterndict 18 dict def\n");
		fprintf (pltout, "setpatterndict begin\n");
		fprintf (pltout, " /bitison\n");
		fprintf (pltout, "  {/ybit exch def /xbit exch def\n");
		fprintf (pltout, "   /bytevalue bstring ybit bwidth mul xbit 8 idiv\n");
		fprintf (pltout, "    add get def\n");
		fprintf (pltout, "   /mask 1 7 xbit 8 mod sub bitshift def\n");
		fprintf (pltout, "   bytevalue mask and 0 ne\n");
		fprintf (pltout, "  } def\n");
		fprintf (pltout, "end\n");
		fprintf (pltout, "/bitpatternspotfunction\n");
		fprintf (pltout, " {setpatterndict begin\n");
		fprintf (pltout, " /y exch def /x exch def\n");
		fprintf (pltout, " /xindex x 1 add 2 div bpside mul cvi def\n");
		fprintf (pltout, " /yindex y 1 add 2 div bpside mul cvi def\n");
		fprintf (pltout, " xindex yindex bitison\n");
		fprintf (pltout, "  {/onbits onbits 1 add def 1}\n");
		fprintf (pltout, "  {/offbits offbits 1 add def 0}\n");
		fprintf (pltout, "  ifelse\n");
		fprintf (pltout, " end\n");
		fprintf (pltout, "} def\n");
/*
 * setpattern sets up the halftone screen given the parameters passed
 * from showpattern and sends this definition to setuserscreen.
 */
		fprintf (pltout, "/setpattern\n");
		fprintf (pltout, " {setpatterndict begin\n");
		fprintf (pltout, "  /cellsz exch def\n");
		fprintf (pltout, "  /angle exch def\n");
		fprintf (pltout, "  /bwidth exch def\n");
		fprintf (pltout, "  /bpside exch def\n");
		fprintf (pltout, "  /bstring exch def\n");
		fprintf (pltout, "  /onbits 0 def /offbits 0 def\n");
		fprintf (pltout, "  cellsz angle /bitpatternspotfunction load\n");
		fprintf (pltout, "   setuserscreen\n");
		fprintf (pltout, "  {} settransfer\n");
		fprintf (pltout, "  offbits offbits onbits add div setgray\n");
		fprintf (pltout, " end\n");
		fprintf (pltout, "} def\n");
		ever_called = 1;
	    }
/*
 * The following code uses the definitions made above to set the
 * halftone screen to represent the user's requested pattern.
 * If the previous area fill was also done with this pattern, however,
 * the necessary transfer function has been saved in the postscript
 * procedure "vplottransfer", and we can just re-load it.
 */
	    if (last_pattern == ipat && ipat != 0)
	    {
		fprintf (pltout, "vplottransfer settransfer\n");
	    }
	    else
	    {
/*
 * Here's where the vplot work begins.
 * Define the fill pattern. It must be square and it must be a
 * multiple of 16 bits wide.
 */
		nxold = pat[ipat].xdim;
		nx = nxold;
		if (nx % 16 != 0)
		{
		    nx = ((nx + 15) / 16) * 16;
		    if (error_size == 0)
		    {
			ERR (WARN, name, "Pspen pattern must be a multiple of 16 bits wide, so partially replicating");
			error_size = 1;
		    }
		}
		nyold = pat[ipat].ydim;
		ny = nyold;
		if (ny % 16 != 0)
		{
		    ny = ((ny + 15) / 16) * 16;
		    if (error_size == 0)
		    {
			ERR (WARN, name, "Pspen pattern must be a multiple of 16 bits wide, so partially replicating");
			error_size = 1;
		    }
		}
		if (nx != ny)
		{
		    if (error_square == 0)
		    {
			ERR (WARN, name, "Pspen pattern must be square, so partially replicating");
			error_square = 1;
		    }
		    if (nx > ny)
			ny = nx;
		    if (ny > nx)
			nx = ny;
		}
		bptr = pat[ipat].patbits;
		fprintf (pltout, "/pattern <");
		mask = mask0;
		outchar = 0;
		for (iy = 0; iy < ny; iy++)
		{
		    for (ix = 0; ix < nx; ix++)
		    {
			if (bptr[(nyold - 1 - (iy % nyold)) * nxold + (ix % nxold)] != 0)
			{
			    outchar |= mask;
			}
			if (mask == 1)
			{
			    fprintf (pltout, "%2.2x", outchar);
			    mask = mask0;
			    outchar = 0;
			}
			else
			{
			    mask >>= 1;
			}
		    }
		}

		fprintf (pltout, "> def\n");
/*
 * Save the graphics state (because we're going to destroy the halftone
 * screen, etc.) Construct the polygon and fill it by calling setpattern.
 * Then restore the graphics state.
 * arguments to setpattern:
 * number of bits on a side of the pattern
 * number of bytes on a side of the pattern
 * size of the pattern in PostScript units.
 */
		fprintf (pltout, "gsave\n");
		fprintf (pltout, "pattern %d %d 0 %d setpattern\n", nx, nx / 8, nx);
/*
 * Save the transfer function (this is the modified halftone screen)
 * so that if another area is filled with the same pattern we can avoid
 * all the work of computing the transfer function.
 */
		fprintf (pltout, "/vplottransfer currenttransfer def\n");
	    }
	}
/*
 * For all-black or all-white patterns, we simply use setgray.
 */
	else
	{
	    fprintf (pltout, "gsave\n");
	    if (all_white == 1 && ps_curcolor != PS_WHITE)
		fprintf (pltout, "1 setgray\n");
	    if (all_black == 1 && ps_curcolor != PS_BLACK)
		fprintf (pltout, "0 setgray\n");
	}
	fprintf (pltout, "np\n");

	v = verlist;
	fprintf (pltout, "%d %d m\n", v->x, v->y);

	ps_oldx = v->x;
	ps_oldy = v->y;
	v++;

	for (i = 1; i < npts; i++)
	{
	    /*
	     * A bit brute force, but a sure way of using whichever is
	     * shorter: absolute or relative draws.
	     */
	    sprintf (stringd, "%d %d d\n", v->x, v->y);
	    sprintf (stringr, "%d %d r\n", v->x - ps_oldx, v->y - ps_oldy);

	    if (strlen (stringd) <= strlen (stringr))
		fprintf (pltout, "%s", stringd);
	    else
		fprintf (pltout, "%s", stringr);

	    ps_oldx = v->x;
	    ps_oldy = v->y;
	    v++;
	}
	fprintf (pltout, "cf\n");
	fprintf (pltout, "gr\n");
    }
    else
    {
	fprintf (pltout, "gsave\n");
	fprintf (pltout, "np\n");

	v = verlist;
	fprintf (pltout, "%d %d m\n", v->x, v->y);

	ps_oldx = v->x;
	ps_oldy = v->y;
	v++;

	for (i = 1; i < npts; i++)
	{
	    /*
	     * A bit brute force, but a sure way of using whichever is
	     * shorter: absolute or relative draws.
	     */
	    sprintf (stringd, "%d %d d\n", v->x, v->y);
	    sprintf (stringr, "%d %d r\n", v->x - ps_oldx, v->y - ps_oldy);

	    if (strlen (stringd) <= strlen (stringr))
		fprintf (pltout, "%s", stringd);
	    else
		fprintf (pltout, "%s", stringr);

	    ps_oldx = v->x;
	    ps_oldy = v->y;
	    v++;
	}
	fprintf (pltout, "cf\n");
	fprintf (pltout, "gr\n");
    }

}

/* Is a dash pattern currently in effect? */
int             ps_dash_pattern_set = NO;
/* Is there a dash pattern saved in postscript's memory? */
int             ps_dash_pattern_exists = NO;
float           psscale;

/* black, blue, red, magenta, green, cyan, yellow, white, ... */
int             red[32768] = {0, 0, 255, 255, 0, 0, 255, 255};
int             green[32768] = {0, 0, 0, 0, 255, 255, 255, 255};
int             blue[32768] = {0, 255, 0, 255, 0, 255, 0, 255};

int             cmyk_cyan, cmyk_magenta, cmyk_yellow, cmyk_black;

int             ps_grey_ras[32768];

float           ps_curcolor = 0.;	/* Only used for mono */
static float    new_ps_curcolor;	/* Only used for mono */
static int      ps_curcolor_no = 7;
static int      new_ps_curcolor_no;
static int      ps_curcolor_set = NO;

static int      ps_done_clipping_gsave = NO;

void psattributes (int command, int value, int v1, int v2, int v3)
/*< attributes >*/
{
    int             xmin, ymin, xmax, ymax;

/*
 * Are we in the middle of a move - draw - draw - draw ... sequence?
 * If so, wrap it up into a path and draw it, so we can move on and do
 * whatever needs to be done here!
 */
    endpath ();

    switch (command)
    {
	case SET_COLOR:
	    ps_set_color (value);
	    break;

	case SET_COLOR_TABLE:
/*
 * Note this will never be called if monochrome.
 */
	    red[value] = v1;
	    green[value] = v2;
	    blue[value] = v3;

#ifdef PSDEBUG
	    fprintf (stderr, "Color %d is now %d %d %d\n", value, v1, v2, v3);
#endif

/*
 * Used for greyscale raster
 */
	    ps_grey_map (value);

/*
 * Check to see if the color they've just redefined is the one we're
 * currently using!
 */
	    if (ps_curcolor_no == value)
	    {
		ps_curcolor_set = NO;
		ps_set_color (ps_curcolor_no);
	    }
	    break;

/*
 * It is important that the clipping code begins with a grestore
 * and does a gsave just before setting the clipping path.
 * In PostScript, the clipping path is defined relative to the
 * current clipping path. So if you clipped with some path, then
 * tried to clip with a path that didn't overlap with the original
 * clipping region, you would get nothing. So we gsave before setting
 * the clipping window, then grestore just before re-setting it.
 * The first time through, there is no saved graphics state to restore.
 * Note: we have to check for an "inside out" clipping window
 * (xmin > xmax or ymin > ymax) here, because PostScript will not
 * catch this case.
 */
	case SET_WINDOW:
/*
 * We have to bump the box out by one unit in each direction, because
 * postscript doesn't include the boundary, but vplot does. At least, so says
 * the postscript reference manual. HOWEVER, the SPARC version of postscript
 * doesn't seem to actually do that: it includes the boundary at the
 * upper end, but doesn't at the lower end!!!! Under SPARC's interpretation
 * the clipping windows vary depending on the ORIENTATION of the same
 * postscript plot on the physical page, so I'm going to do it "the right way"
 * here. This allows an extra pixel width of stuff on each axis to sneak
 * through when plotting on the SPARC, unfortunately, but this seems the
 * best compromise to me. -- Joe D.
 */
	    xmin = value - 1;
	    ymin = v1 - 1;
	    xmax = v2 + 1;
	    ymax = v3 + 1;

/*
 * Inside-out clipping window test. We use (value,v1) and (v2,v3) instead
 * of (xmin,ymin) and (xmax,ymax), because we need to do the test according
 * to vplot's idea of how clipping windows work, not Postscript's.
 */
	    if (value > v2)
		xmin = xmax;
	    if (v1 > v3)
		ymin = ymax;

	    if (ps_done_clipping_gsave == YES)
		fprintf (pltout, "grestore\n");

	    fprintf (pltout, "/clippingpath\n");
	    fprintf (pltout, " {newpath\n");
	    fprintf (pltout, " %d %d m\n", xmin, ymin);
	    fprintf (pltout, " %d %d d\n", xmax, ymin);
	    fprintf (pltout, " %d %d d\n", xmax, ymax);
	    fprintf (pltout, " %d %d d\n", xmin, ymax);
	    fprintf (pltout, " closepath} def\n");

	    fprintf (pltout, "gsave clippingpath eoclip\n");
	    ps_done_clipping_gsave = YES;

	    fprintf (pltout, "newpath\n");

	    /*
	     * The grestore caused postscript to forget most of the current
	     * state. Set it all back up again.
	     */
	    ps_fixup_after_grestore ();

	    /* Global plot parameters fixed; we can exit now. */
	    break;

	case NEW_DASH:
	    ps_set_dash (value);
	    break;

	case BEGIN_GROUP:
	    if (!corners && 0 == strcmp (group_name, "corner")) {
	        corners_group = value;
	        iscorners = 1;
	    }
	    break;

	case END_GROUP:
	    if (!corners && iscorners && corners_group == value) {
	        iscorners = 0;
	        corners_group = -1;
	    }
	    break;

	default:
	    break;
    }
}

int             ps_last_fat = -1;

void ps_fixup_after_grestore (void)
/*< restore postscript state >*/
{
/*
 * Alas, when we did the "gerestore" above ALL GLOBAL PLOT SETTINGS WERE LOST!
 * So go back and tidy up. The current fatness is easy; we just need to let
 * psvector know that the current value is the default (0) again. As for the
 * dash pattern, the variable ps_dash_pattern_exists tells psvector it's been
 * lost and the routine ps_set_dash provides a way for psvector to recreate it
 * when needed. The current color has to be reset right away.
 */

    /* The current fatness reverts to 0 */
    ps_last_fat = 0;

    /* No dash pattern is in effect */
    ps_dash_pattern_set = NO;
    /* No dash pattern remains in memory */
    ps_dash_pattern_exists = NO;

    /*
     * The current color got reset to the default. We could try to be tricky
     * and not reset the color if the default is OK, but it's safer and
     * simpler to force the color to be explicitly reset right away.
     */
    ps_curcolor_set = NO;
    ps_set_color (ps_curcolor_no);
}

void ps_grey_map (int coltab)
/*< grey map >*/
{
    int             grey;

    /*
     * Calculate the grey level that goes with this color.
     */
    grey = (blue[coltab] * 1 + red[coltab] * 2 + green[coltab] * 4 + 6) / 7;

    /*
     * For raster, apply appropriate gamma corrections and invert as
     * necessary.
     */
    ps_grey_ras[coltab] = greycorr (grey);
}

void ps_set_color (int value)
/*< set color >*/
{
    bool force;
    new_ps_curcolor_no = value;


#ifdef PSDEBUG
    fprintf (stderr, "Set? %d, Change Color to %d from %d\n",
	     ps_curcolor_set, new_ps_curcolor_no, ps_curcolor_no);
#endif


    if (mono)
    {
	if (new_ps_curcolor_no > 0)
	    new_ps_curcolor = PS_BLACK;
	else
	    new_ps_curcolor = PS_WHITE;

	if (new_ps_curcolor != ps_curcolor || !ps_curcolor_set)
	{
	    fprintf (pltout, "%.2g setgray\n", new_ps_curcolor);

	    ps_curcolor = new_ps_curcolor;
	    ps_curcolor_no = new_ps_curcolor_no;
	    ps_curcolor_set = YES;
	}
    }
    else
    {
	if (new_ps_curcolor_no != ps_curcolor_no || !ps_curcolor_set)
	{

	    force = force_color && (!force_bw || ((  0!=red[new_ps_curcolor_no] ||   0!=green[new_ps_curcolor_no] ||   0!=blue[new_ps_curcolor_no]) &&
						  (255!=red[new_ps_curcolor_no] || 255!=green[new_ps_curcolor_no] || 255!=blue[new_ps_curcolor_no])));


            if (rgb_colorspace)
            {
	        if (force)
	        {
		    fprintf (pltout, "%.2g %.2g %.2g setrgbcolor\n", red[new_ps_curcolor_no] / 255., green[new_ps_curcolor_no] / 255., blue[new_ps_curcolor_no] / 255.);
	        }
	        else
	        {
		    fprintf (pltout, "%.2g %.2g %.2g setrgbcolor\n", 1. - red[new_ps_curcolor_no] / 255., 1. - green[new_ps_curcolor_no] / 255., 1. - blue[new_ps_curcolor_no] / 255.);
	        }
            }
            else
            {
	        if (force)
	        {
		    rgb_to_cmyk(red[new_ps_curcolor_no], green[new_ps_curcolor_no], blue[new_ps_curcolor_no], &cmyk_cyan, &cmyk_magenta, &cmyk_yellow, &cmyk_black);
                }
	        else
	        {
		    rgb_to_cmyk(255 - red[new_ps_curcolor_no], 255 - green[new_ps_curcolor_no], 255 - blue[new_ps_curcolor_no], &cmyk_cyan, &cmyk_magenta, &cmyk_yellow, &cmyk_black);
                }


		/*
		 * Use the setcmykcolor command instead of the setrgbcolor command.
		 * Note, the setcmykcolor command is not guaranteed to
		 * to be supported in Level 1 postscript interpreters.
		 */
	        fprintf (pltout, "%.2g %.2g %.2g %.2g setcmykcolor\n", cmyk_cyan / 255., cmyk_magenta / 255., cmyk_yellow / 255., cmyk_black / 255.);
            }

	    ps_curcolor_no = new_ps_curcolor_no;
	    ps_curcolor_set = YES;
	}
    }
}

void ps_set_dash (int value)
/*< set dash >*/
{
/*
 * A local variable named dashon. This routine has no business resetting
 * the global variable of the same name.
 */
    int             dashon;
    int             ii;

    dashon = value;

/*
 * No need to erase the pattern; psvector knows not to use it if dashon==0.
 */
    if (dashon == 0)
	return;

    fprintf (pltout, "[");
    for (ii = 0; ii < dashon * 2; ii++)
    {
	fprintf (pltout, "%.2f ", dashes[ii] * PSPERIN / psscale);
    }
    fprintf (pltout, "] 0 setdash\n");

    /* A dash pattern is now in postscript's memory. */
    ps_dash_pattern_exists = YES;
    /* And it is currently active, too. */
    ps_dash_pattern_set = YES;
}

static float           ps_xlength, ps_ylength;
static int             ps_set_papersize = NO;
static char            psprintertype[80] = "default";
static int             file_created = NO;
static char            *scratch_file;
static bool            tex = false;

void psclose (int status)
/*< Routine to finish up >*/
{
    char            system_call[120];
    char            printer[40];
    char            *printer0;
    char           *stringptr;
    int             ecode;

    endpath ();

    switch (status)
    {
	case CLOSE_NORMAL:
	    /*
	     * if(tex == YES) fprintf(pltout, "%c", POP);
	     */

#ifndef NOCOMMENTS
	    if ((strcmp (psprintertype, "default") != 0)
		|| (dev.pixels_per_inch != DEFAULT_PIXELS_PER_INCH))
	    {
		ERR (COMMENT, name,
		     "Printer is of type \"%s\", with %g pixels per inch.",
		     psprintertype, dev.pixels_per_inch);
	    }
#endif

	    /*
	     * If we created a temporary file, spool it.
	     */
	    if (file_created)
	    {
		fclose (pltout);

		if ((stringptr = getenv ("PSPRINTER")) != NULL)
		    strcpy (printer, stringptr);
		else if (mono)
		    strcpy (printer, "postscript");
		else
		    strcpy (printer, "colorps");

		if (NULL != (printer0 = sf_getstring ("printer"))) 
		    strcpy(printer,printer0);
		/* what printer to send it to */

		if (ps_set_papersize)
		{
		    sprintf (system_call,
			     "lpr -r -s -P%s -CX%.2f,Y%.2f %s",
			     printer, ps_ylength, ps_xlength, scratch_file);
		}
		else
		{
		    sprintf (system_call,
			     "lpr -r -s -P%s %s", printer, scratch_file);
	
		}

#ifndef NOCOMMENTS
		if (ps_set_papersize)
		{
		    ERR (COMMENT, name,
			 "Spooling plot using command \"%s\".", system_call);
		}
		else
		{
		    ERR (COMMENT, name,
			 "Spooling plot to printer \"%s\".", printer);
		}
#endif
		ecode = system (system_call);

		/*
		 * Shift 8 bits over; what's left contains the exit code from lpr
		 */
		if ((ecode & 0xFF) != 0)
		{
		    ERR (WARN, name,
			 "Signal stopped or killed system call \"%s\".", system_call);
		    ERR (WARN, name,
			 "Output postscript file may have been left behind in \"%s\".",
			 scratch_file);
		}
		else
		{
		    ecode = (ecode > 8);
		    if (ecode != 0)
		    {
			ERR (WARN, name,
			     "Exit code %d from lpr. Is \"%s\" a valid printer?",
			     ecode, printer);
			if (stringptr == NULL)
			{
			    ERR (COMMENT, name,
				 "Perhaps you need to do \"setenv PSPRINTER printer_name\"?");
			}
			else
			{
			    ERR (COMMENT, name,
				 "Is your environment variable $PSPRINTER = \"%s\" correct?",
				 printer);
			}
			ERR (WARN, name,
			     "The output postscript file may have been left behind in \"%s\".",
			     scratch_file);
		    }
		}
	    }
	    file_created = NO;
	    break;
	case CLOSE_ERROR:
	case CLOSE_NOTHING:
	case CLOSE_INTERRUPT:
	    break;
	case CLOSE_DONE:
	    /*
	     * If we created a temporary file, remove it
	     */
	    if (file_created)
		unlink (scratch_file);
	    break;
	case CLOSE_FLUSH:
	    fflush (pltout);
	    break;
	case CLOSE_PAUSE:
	    break;
	default:			/* not meant for us, ignore */
	    break;
    }
}


/*
 * Location and height of label and surrounding box in ps coordinates
 */
#define TEXT_YPOS	100
#define TEXT_HEIGHT	50
#define TEXT_PAD	18

static float    ps_ypapersize;
static int      ncopies_document = 1;
static int      hold;

void pserase (int command)
/*< erase >*/
{
    char            full_label[100];
    static int      page_count = 1;

    endpath ();

    switch (command)
    {
	case ERASE_MIDDLE:
	case ERASE_END:
/*
 * put on label if desired
 */
	    if (label[0] != '\0')
	    {
		if (page_count == 1 && command == ERASE_END)
		{
		    sprintf (full_label, "%s", label);
		}
		else
		{
		    sprintf (full_label, "%s : Page %d.", label, page_count);
		}
		/*
		 * Do a grestore so any clipping window currently in force won't
		 * clip away the plot label. Also do a gsave, because by
		 * convention the plot ends with a grestore.
		 */
		fprintf (pltout, "grestore gsave\n");
		fprintf (pltout, "/labelshow\n");
		fprintf (pltout, " {dup stringwidth pop\n");
		fprintf (pltout, "  dup dup %d exch sub\n", dev.xmax - 50);
		fprintf (pltout, "  newpath %d m\n", TEXT_YPOS);
		fprintf (pltout, "  gsave 0 %d rlineto\n", -TEXT_PAD);
		fprintf (pltout, "  0 rlineto\n");
		fprintf (pltout, "  0 %d rlineto\n", TEXT_HEIGHT + TEXT_PAD);
		fprintf (pltout, "  neg 0 rlineto\n");
		fprintf (pltout, "  closepath 1 setgray fill grestore\n");
		fprintf (pltout, "  gsave 0 setgray\n");
		fprintf (pltout, "  show grestore} def\n");

		if (serifs_OK)
		{
		    fprintf (pltout, "/Helvetica-BoldOblique findfont %d scalefont setfont\n", TEXT_HEIGHT);
		}
		else
		{
		    /* SEG doesn't like bold or oblique fonts either */
		    fprintf (pltout, "/Helvetica findfont %d scalefont setfont\n", TEXT_HEIGHT);
		}
		fprintf (pltout, "(%s) labelshow\n", full_label);
	    }
	    if (!tex)
	    {
		if (ncopies_document != 1)
		{
		    fprintf (pltout, "/#copies %d def\n", ncopies_document);
		}
		if (hold == YES)
		{
		    fprintf (pltout, "statusdict begin\n");
		    fprintf (pltout, "/manualfeed true def\n");
		    fprintf (pltout, "/manualfeedtimeout 300 def\n");
		    fprintf (pltout, "end\n");
		}
	    }

	    if (ps_done_clipping_gsave == YES)
		fprintf (pltout, "grestore\n");
	    ps_done_clipping_gsave = NO;

	    fprintf (pltout, "grestore\n");
	    fprintf (pltout, "showpage\n");

	    if (command == ERASE_MIDDLE)
	    {
		if (!tex)
		{
		    fprintf (pltout, "initgraphics 1 setlinecap 1 setlinejoin\n");
		    fprintf (pltout, "%d rotate", 90);
		    fprintf (pltout, " 0 %.2f translate %.2f %.2f scale gsave\n",
			     -ps_ypapersize * PSPERIN, psscale, psscale);
		}
		else
		{
		    fprintf (pltout, " %.2f %.2f scale gsave\n", psscale, psscale); 
		    fprintf (pltout, " 1 setlinecap 1 setlinejoin\n");
		}

		/*
		 * Postscript has forgetten most of the current state. Set it all
		 * back up again.
		 */
		ps_fixup_after_grestore ();
	    }
	    page_count++;
	    break;
	case ERASE_START:
	default:
	    break;
    }
}

#ifndef DEFAULT_PAPER_SIZE
#define DEFAULT_PAPER_SIZE	"letter"
#endif

#ifndef DEFAULT_PAPER_UNITS
#define DEFAULT_PAPER_UNITS	'i'
#endif


char            ps_paper[80];

char            mapfile[100] = "default";
int             default_ps_font = DEFAULT_HARDCOPY_FONT;

extern int      red[], green[], blue[];

float           ps_xmin, ps_xmax, ps_ymin, ps_ymax;
float           ps_xborder, ps_yborder;

void opendev (int argc, char* argv[])
/*< open >*/
{
    char           *user_name;
    char            date[50];
    int             i;
    char            units;
    float           unitscale=1.;
    extern int      isafile ();
    struct stat     statbuf;
    int             creatafile;
    bool             yesget;
    char           *paperstring;
    
    bool             ps_color; 
    
    size_t len;

    dev.reset = psreset;
    dev.erase = pserase;
    dev.close = psclose;

    dev.vector = psvector;
    dev.text = pstext;
    dev.area = psarea;
    dev.raster = smart_psraster;
    dev.attributes = psattributes;

    dev.plot = psplot;

    strcpy (psprintertype, "default");

/*
 * physical device parameters
 */

/* For HP printer engines, the usual default */

    pixc = 0.6;
    greyc = -0.5;

    dev.pixels_per_inch = DEFAULT_PIXELS_PER_INCH;

    strcpy (ps_paper, DEFAULT_PAPER_SIZE);

/*
 * For now, elsewhere in the code we just ignore aspect_ratio,
 * implicitly assuming it will always be 1.
 */
    dev.aspect_ratio = 1.0;


/*
 * Allow override of pixels_per_inch from the command line. (If we used
 * GETPAR here it would also search the incoming history file... I think
 * it's safer to require them to be on the command line.)
 */
    sf_getfloat ("ppi",&dev.pixels_per_inch); /* pixels per inch */


/*
 * based on the number of pixels per inch and PostScript's units
 * of length, we compute a PostScript scale factor here that will allow us to
 * send vplot coordinates (integers) directly to PostScript.
 */
    psscale = PSPERIN / ((float) dev.pixels_per_inch);


/*
 * American paper sizes
 *
 * letter: 8.5 by 11 inch page; imageable region of 8.0 by 10.92 inches.
 * legal: 8.5 by 13 inch page; imageable region of 6.72 by 13 inches.
 * (these limits are imposed by the apple laserwriter).
 */


/*
 * Default units for custom paper sizes.
 */
    units = DEFAULT_PAPER_UNITS;

/*
 * Environment variable can override default paper size...
 */
    if ((paperstring = getenv ("DEFAULT_PAPER_SIZE")) != NULL)
	strcpy (ps_paper, paperstring);

/*
 * but GETPAR has the very last say.
 */
    if (NULL != (paperstring = sf_getstring("paper")))
	strcpy (ps_paper, paperstring);

    if (strcmp (ps_paper, "letter") == 0)
    {
/* Empirically determined limits for SPARC printers with letter-size paper */
	dev.xmin = .19 * dev.pixels_per_inch + .5;
	dev.ymin = .26666 * dev.pixels_per_inch + .5;
	dev.xmax = 10.88333 * dev.pixels_per_inch + .5;
	dev.ymax = 8.23333 * dev.pixels_per_inch + .5;
	ps_ypapersize = 8.5;
    }
    else if (strcmp (ps_paper, "legal") == 0)
    {
/* Empirically determined limits for SPARC printers with legal-size paper */
	dev.xmin = .50333 * dev.pixels_per_inch + .5;
	dev.ymin = .89 * dev.pixels_per_inch + .5;
	dev.xmax = 13.49666 * dev.pixels_per_inch + .5;
	dev.ymax = 7.61 * dev.pixels_per_inch + .5;
	ps_ypapersize = 8.5;
    }
    else if (strcmp (ps_paper, "a5") == 0 || strcmp (ps_paper, "A5") == 0)
    {
	/*
	 * For our European friends, A5 paper
	 * 
	 * For now, use (DEFAULT_BORDER * CMPERIN) as the best guess for a
	 * nonimageable area at the edges of the paper all around.
	 */

	dev.xmin = (DEFAULT_BORDER * CMPERIN) * (1. / CMPERIN) * dev.pixels_per_inch + .5;
	dev.ymin = (DEFAULT_BORDER * CMPERIN) * (1. / CMPERIN) * dev.pixels_per_inch + .5;
	dev.xmax = (21.0 - (DEFAULT_BORDER * CMPERIN)) * (1. / CMPERIN) * dev.pixels_per_inch + .5;
	dev.ymax = (14.85 - (DEFAULT_BORDER * CMPERIN)) * (1. / CMPERIN) * dev.pixels_per_inch + .5;
	ps_ypapersize = 14.85 * (1. / CMPERIN);
    }
    else if (strcmp (ps_paper, "a4") == 0 || strcmp (ps_paper, "A4") == 0)
    {
	/*
	 * For our European friends, A4 paper
	 * 
	 * For now, use (DEFAULT_BORDER * CMPERIN) as the best guess for a
	 * nonimageable area at the edges of the paper all around.
	 */

	dev.xmin = (DEFAULT_BORDER * CMPERIN) * (1. / CMPERIN) * dev.pixels_per_inch + .5;
	dev.ymin = (DEFAULT_BORDER * CMPERIN) * (1. / CMPERIN) * dev.pixels_per_inch + .5;
	dev.xmax = (29.7 - (DEFAULT_BORDER * CMPERIN)) * (1. / CMPERIN) * dev.pixels_per_inch + .5;
	dev.ymax = (21.0 - (DEFAULT_BORDER * CMPERIN)) * (1. / CMPERIN) * dev.pixels_per_inch + .5;
	ps_ypapersize = 21.0 * (1. / CMPERIN);
    }
    else if (strcmp (ps_paper, "a3") == 0 || strcmp (ps_paper, "A3") == 0)
    {
	/*
	 * For our European friends, A3 paper
	 * 
	 * For now, use (DEFAULT_BORDER * CMPERIN) as the best guess for a
	 * nonimageable area at the edges of the paper all around.
	 */

	dev.xmin = (DEFAULT_BORDER * CMPERIN) * (1. / CMPERIN) * dev.pixels_per_inch + .5;
	dev.ymin = (DEFAULT_BORDER * CMPERIN) * (1. / CMPERIN) * dev.pixels_per_inch + .5;
	dev.xmax = (42.0 - (DEFAULT_BORDER * CMPERIN)) * (1. / CMPERIN) * dev.pixels_per_inch + .5;
	dev.ymax = (29.7 - (DEFAULT_BORDER * CMPERIN)) * (1. / CMPERIN) * dev.pixels_per_inch + .5;
	ps_ypapersize = 29.7 * (1. / CMPERIN);
    }
    else
    {
	ps_xborder = -1.;
	ps_yborder = -1.;

	if (sscanf (ps_paper, "%fx%f%c,%f,%f",
		    &ps_ylength, &ps_xlength,
		    &units,
		    &ps_yborder, &ps_xborder) >= 2)
	{
	    if (units == 'i')
	    {
		/* Inches */
		unitscale = 1.;
	    }
	    else if (units == 'c')
	    {
		/* Centimeters */
		unitscale = 1. / CMPERIN;
	    }
	    else
	    {
		ERR (FATAL, name,
		     "Sorry, don't recognize units of type \"%c\"!", units);
	    }

	    /*
	     * Use a default border of DEFAULT_BORDER inches if they didn't
	     * specify it.
	     */
	    if (ps_xborder < 0.)
		ps_xborder = DEFAULT_BORDER / unitscale;

	    if (ps_yborder < 0.)
		ps_yborder = DEFAULT_BORDER / unitscale;


	    if (ps_xlength <= 0.)
	    {
		if (ps_ylength <= 0.)
		{
		    ERR (FATAL, name,
			 "Height and width of paper are both negative or zero!");
		}
		else
		    ps_xlength = 2. * ps_xborder + (ps_ylength - 2. * ps_yborder) / VP_SCREEN_RATIO;
	    }
	    else if (ps_ylength <= 0.)
	    {
		ps_ylength = 2. * ps_yborder + (ps_xlength - 2. * ps_xborder) * VP_SCREEN_RATIO;
	    }


	    ps_xlength *= unitscale;
	    ps_ylength *= unitscale;
	    ps_xborder *= unitscale;
	    ps_yborder *= unitscale;

	    ps_xmin = ps_xborder;
	    ps_ymin = ps_yborder;
	    ps_xmax = (ps_xlength - ps_xborder);
	    ps_ymax = (ps_ylength - ps_yborder);
	}
	else if (sscanf (ps_paper, "%f,%f,%fx%f,%f,%f%c",
			 &ps_ymin,
			 &ps_ymax,
			 &ps_ylength,
			 &ps_xmin,
			 &ps_xmax,
			 &ps_xlength,
			 &units) >= 6)
	{
	    if (units == 'i')
	    {
		/* Inches */
		unitscale = 1.;
	    }
	    else if (units == 'c')
	    {
		/* Centimeters */
		unitscale = 1. / CMPERIN;
	    }
	    else
	    {
		ERR (FATAL, name,
		     "Sorry, don't recognize units of type \"%c\"!", units);
	    }

	    ps_xmin *= unitscale;
	    ps_ymin *= unitscale;
	    ps_xmax *= unitscale;
	    ps_ymax *= unitscale;
	    ps_xlength *= unitscale;
	    ps_ylength *= unitscale;
	}
	else
	{
	    if (paperstring != NULL)
	    {
		ERR (COMMENT, name,
		     "Is your environmental variable \"$DEFAULT_PAPER_SIZE\" correct?");
	    }

	    ERR (FATAL, name,
		 "Don't recognize requested paper type \"%s\"!", ps_paper);
	}


	dev.xmin = ps_xmin * dev.pixels_per_inch + .5;
	dev.ymin = ps_ymin * dev.pixels_per_inch + .5;
	dev.xmax = ps_xmax * dev.pixels_per_inch + .5;
	dev.ymax = ps_ymax * dev.pixels_per_inch + .5;
	ps_ypapersize = ps_ylength;

	if (dev.xmin >= dev.xmax || dev.ymin >= dev.ymax)
	{
	    ERR (FATAL, name,
		 "Custom paper size has no plotting area.");
	}

	ps_set_papersize = YES;
    }


/*
 * device capabilities
 */
    if (!sf_getbool("dumbfat",&dumb_fat)) dumb_fat=false;
    if (!sf_getbool("color",&ps_color)) ps_color=false;
    /* use color */
    if (!sf_getbool("force",&force_color)) force_color=false;
    /* if y, don't replace colors with their compliments */
    if (!sf_getbool("forcebw",&force_bw)) force_bw=false;
    /* if y, don't replace black and white colors with their compliments */
    if (!sf_getbool("force_raster",&force_raster)) force_raster=true;
    /* if y, don't replace raster colors with their compliments */

/*
 * GEOPHYSICS now requires the cmyk color space. However,
 * older level 1 postscript interpreters will not understand that,
 * and it makes for a longer postscript file as well.
 * So for now the default is to keep using the RGB color space.
 * For figures turned into GEOPHYSICS, use "rgb=no".
 */
    if (!sf_getbool("rgb",&rgb_colorspace)) rgb_colorspace=true;
    /* For figures turned into GEOPHYSICS, use "rgb=no". */

/*
 * If we can't use serifs for labels, go ahead and change
 * the default font to a non-serif one.
 */
    if (! serifs_OK) default_ps_font = DEFAULT_SANSSERIF_FONT;

    if (ps_color)
    {
	mono = false;
	dev.num_col = 256;
    }
    else
    {
	mono = true;
	dev.num_col = 0;
    }

    dev.smart_raster = true;
    dev.need_end_erase = true;

    dither = 3;
    dev.txfont = default_ps_font;
    dev.txprec = DEFAULT_HARDCOPY_PREC;

    if (NULL == (label = sf_getstring ("label")))
	/*( label for pages (default is user name and date) )*/
    {
	if ((user_name = getlogin ()) == NULL)
	    user_name = getpwuid (getuid ())->pw_name;
	dateget (date);

	len = strlen(user_name)+strlen(date)+3;
	label = sf_charalloc(len);

	snprintf (label, len, "%s, %s", user_name, date);
    }
    else
    {
	if ((strcmp (label, "no") == 0) || (strcmp (label, "n") == 0)
	    || (strcmp (label, " ") == 0) || (strcmp (label, "") == 0))
	    label[0] = '\0';
    }


/*
 *   Get the output file for the device
 */

    if (isatty (fileno (pltout)))
    {
/*
 * If it's a tty, then we certainly don't want to write to it!
 */
	creatafile = YES;
    }
    else
    {
/*
 *   If it's not a tty, they MAY be running pspen in a script
 *   and have logged out. In that case they want us to spool the plot,
 *   even though the output may not be a tty. (It may be /dev/null.)
 */
	if (fstat (fileno (pltout), &statbuf) != 0)
	{
	    ERR (WARN, name,
		 "Can't stat plot output! Trying to create a spool file instead.");

	    creatafile = YES;
	}
	else
	{
	    if (S_ISREG (statbuf.st_mode) || S_ISSOCK (statbuf.st_mode) ||
		S_ISFIFO (statbuf.st_mode))
	    {
		creatafile = NO;
	    }
	    else
	    {
		creatafile = YES;
	    }
	}
    }


    if (creatafile)
    {
	file_created = YES;
	pltout = sf_tempfile(&scratch_file,"w");
    }

    if (!sf_getbool("tex",&tex)) tex=false;

    if (tex)
    {
	/*
	 * allow as big a plot as we can and make sure our plot is in
	 * absolute coordinates. This prevents any clipping of the image. If
	 * tex=y is specified this plot will be scaled by TeX to fit whatever
	 * size we want, so don't clip it to page boundaries.
	 */
	dev.xmax = VP_MAX * RPERIN;
	dev.ymax = VP_MAX * RPERIN * VP_SCREEN_RATIO;
	dev.xmin = 0;
	dev.ymin = 0;
	size = VP_ABSOLUTE;
	label[0] = '\0';
    }

    if (!sf_getbool("hold",&yesget)) yesget=false;
    /* tells the printer to not print the job until you
       add paper through the manual feed slot */

    if (yesget)
	hold = YES;
    else
	hold = NO;
    
    if (!sf_getint("copies",&ncopies_document)) ncopies_document = 1;
    /* number of copies */

    if (!sf_getbool("corners",&corners)) corners=true;
    /* n - remove "corner" group. */

/*
 * Initialize the PostScript file
 */
    if (!tex)
    {
	fprintf (pltout, "%%!\n");

	fprintf (pltout, "initgraphics 1 setlinecap 1 setlinejoin\n");
	fprintf (pltout, "%d rotate", 90);
	fprintf (pltout, " 0 %.2f translate %.2f %.2f scale gsave\n",
		 -ps_ypapersize * PSPERIN, psscale, psscale);
    }
    else
    {
	/*
	 * changed to work with psfig macros in TeX. Take the rotation and
	 * translation out. Now all we need is a shell that puts the
	 * BoundingBox stuff on the front.
	 */

	fprintf (pltout, " \n");
	fprintf (pltout, "%% Start of pspen output\n");
	fprintf (pltout, " \n");
	fprintf (pltout, " %.2f %.2f scale gsave\n", psscale, psscale);
	/*
	 * Make sure postscript uses the correct line join type to avoid
	 * "fanged S syndrome", though!
	 */
	fprintf (pltout, " 1 setlinecap 1 setlinejoin\n");
    }

    /* in case colorimage command is not known by this device */
    if (rgb_colorspace)
    {
	/*
	 * If they require the CMYK color space we just have to hope
	 * the colorimage command is known.
	 */
        fprintf (pltout, " \n");
        fprintf (pltout, "systemdict /colorimage known not { \n");
        fprintf (pltout, "  /colortograyscale { \n");
        fprintf (pltout, "    dup /rgbdata exch store \n");
        fprintf (pltout, "    length 3 idiv \n");
        fprintf (pltout, "    /npixls exch store \n");
        fprintf (pltout, "    /indx 0 store \n");
        fprintf (pltout, "    /pixls npixls string store \n");
        fprintf (pltout, "    0 1 npixls -1 add { \n");
        fprintf (pltout, "      pixls exch \n");
        fprintf (pltout, "      rgbdata indx get .3 mul \n");
        fprintf (pltout, "      rgbdata indx 1 add get .59 mul add \n");
        fprintf (pltout, "      rgbdata indx 2 add get .11 mul add \n");
        fprintf (pltout, "      cvi \n");
        fprintf (pltout, "  put \n");
        fprintf (pltout, "      /indx indx 3 add store \n");
        fprintf (pltout, "    } for \n");
        fprintf (pltout, "    pixls \n");
        fprintf (pltout, "  } bind def \n");
        fprintf (pltout, "  /mergeprocs { \n");
        fprintf (pltout, "    dup length \n");
        fprintf (pltout, "    3 -1 roll \n");
        fprintf (pltout, "    dup \n");
        fprintf (pltout, "    length \n");
        fprintf (pltout, "    dup \n");
        fprintf (pltout, "    5 1 roll \n");
        fprintf (pltout, "    3 -1 roll \n");
        fprintf (pltout, "    add \n");
        fprintf (pltout, "    array cvx \n");
        fprintf (pltout, "    dup \n");
        fprintf (pltout, "    3 -1 roll \n");
        fprintf (pltout, "    0 exch \n");
        fprintf (pltout, "    putinterval \n");
        fprintf (pltout, "    dup \n");
        fprintf (pltout, "    4 2 roll \n");
        fprintf (pltout, "    putinterval \n");
        fprintf (pltout, "  } bind def \n");
        fprintf (pltout, "  /colorimage { \n");
        fprintf (pltout, "     pop \n");
        fprintf (pltout, "     pop \n");
        fprintf (pltout, "     {colortograyscale} \n");
        fprintf (pltout, "     mergeprocs \n");
        fprintf (pltout, "     image \n");
        fprintf (pltout, "  } bind def \n");
        fprintf (pltout, "} if \n");
        fprintf (pltout, " \n");
    }

    /* Some abbreviations to make the files more compact */
    fprintf (pltout, "/m { moveto } bind def\n");
    fprintf (pltout, "/d { lineto } bind def\n");
    fprintf (pltout, "/r { rlineto } bind def\n");
    fprintf (pltout, "/x { 0 0 rlineto } bind def\n");
    fprintf (pltout, "/s { stroke } bind def\n");
    fprintf (pltout, "/gr { grestore } bind def\n");
    fprintf (pltout, "/np { newpath } bind def\n");
    fprintf (pltout, "/cf { closepath eofill } bind def\n");
    fprintf (pltout, " \n");

    if (!mono)
    {
	/*
	 * Begin by setting standard 7 colors. (The monochrome equivalent
	 * takes place in "psreset.c" for the monochrome case.)
	 */
	for (i = 0; i < 8; i++)
	{
	    psattributes (SET_COLOR_TABLE, i, red[i], green[i], blue[i]);
	}
	psattributes (SET_COLOR, 7, 0, 0, 0);
    }

    fflush (pltout);

    epause = 0;
    endpause = false;
/*
 * This turns out not to be a good default for this hardcopy device,
 * since people think of it more as a screen-type device.
 *
 *  size = ABSOLUTE;
 */
}


void dateget (char *date)
/*< get the date >*/
{
    time_t          clock;

    clock = time (0);
    sprintf (date, "%.16s", asctime (localtime (&clock)));
}

static int      where = -1;

void psplot (int x, int y, int draw)
/*< plot >*/
{
    if (draw == 0)
    {
	startpath ();
	dev.lost = 0;
    }
    addpath (x, y);
}

void startpath (void)
/*< start path >*/
{
    if (where > 0)
    {
	endpath ();
    }
    where = 0;
}

void addpath (int x,int y)
/*< add path >*/
{
    /*
     * Just in case, allow lots of extra room
     */
    char            stringd[80];
    char            stringr[80];

    /* If where is -1 here it is a BUG! */
    if (where)
    {
	/*
	 * Important special case: a dot.
	 */
	if (x - ps_oldx == 0 && y - ps_oldy == 0)
	{
	    fprintf (pltout, "x\n");
	}
	else
	{
	    /*
	     * A bit brute force, but a sure way of using whichever is
	     * shorter: absolute or relative draws.
	     */
	    sprintf (stringd, "%d %d d\n", x, y);
	    sprintf (stringr, "%d %d r\n", x - ps_oldx, y - ps_oldy);

	    if (strlen (stringd) <= strlen (stringr))
		fprintf (pltout, "%s", stringd);
	    else
		fprintf (pltout, "%s", stringr);

	    fflush(pltout);
	}
    }
    else
	fprintf (pltout, "%d %d m\n", x, y);

    ps_oldx = x;
    ps_oldy = y;

    where++;
    if (where == PATHLENGTH - 1)
    {
	/* path reached maximum postscript pathlength; restart path */
	endpath ();
    }
}

void endpath (void)
/*< end path >*/
{
    if (where > 0)
    {
	fprintf (pltout, "s\n");
	where = -1;
    }
    dev.lost = 1;
}

extern int      ps_grey_ras[];
extern int	red[], green[], blue[];
extern int	ras_allgrey;

void smart_psraster (int xpix, int ypix, int xmin, int ymin, int xmax, int ymax, 
		     unsigned char **raster_block, int orient, int dither_it)
/*< raster >*/
{
    int             i,j;
    int             xshift, yshift;
    int             rxscale, ryscale;
    int             rangle;
    unsigned char   ci = 8;

    endpath ();

    rxscale = xmax - xmin;
    ryscale = ymax - ymin;

    switch (orient) {
	case 0:
	    xshift = xmin;
	    yshift = ymin;
	    rangle = 0;
	    break;
	case 1:
	    xshift = xmin;
	    yshift = ymax;
	    rangle = 270;
	    break;
	case 2:
	    xshift = xmax;
	    yshift = ymax;
	    rangle = 180;
	    break;
	case 3:
	default:
	    xshift = xmax;
	    yshift = ymin;
	    rangle = 90;
	    break;
    }

    fprintf (pltout, "gsave /picstr %d string def\n", xpix);

    fprintf (pltout, "%d %d translate %d %d scale %d rotate\n", 
	     xshift, yshift, rxscale, ryscale, rangle);

    fflush(pltout);

    if (!corners) {
        if (mono || ras_allgrey)
            fprintf (pltout, "/DeviceGray setcolorspace\n");
        else if (rgb_colorspace)
            fprintf (pltout, "/DeviceRGB setcolorspace\n");
        else
            fprintf (pltout, "/DeviceCMYK setcolorspace\n");
        fprintf (pltout, "<<\n");
        fprintf (pltout, "  /ImageType 4\n");
        fprintf (pltout, "  /Width %d\n", xpix);
        fprintf (pltout, "  /Height %d\n", ypix);
        fprintf (pltout, "  /ImageMatrix [ %d 0 0 %d 0 %d ]\n", xpix, -ypix, ypix);
        fprintf (pltout, "  /MultipleDataSources false\n");
        fprintf (pltout, "  /DataSource currentfile /ASCIIHexDecode filter\n");
        fprintf (pltout, "  /BitsPerComponent 8\n");
/*	for (j = 0; j < xpix*ypix; j+=80)
	{
	    for (i=j; (i<j+80 && i<xpix*ypix); i++)
	    {
	        if (raster_block[0][i] < ci)
	            ci = raster_block[0][i];
	    }
	}*/
    }

    if ( mono || ras_allgrey ) {
        if (corners) {
            fprintf (pltout, "/raster {%d %d 8 [ %d 0 0 %d 0 %d ] {currentfile picstr readhexstring pop} image} def\n", xpix, ypix, xpix, -ypix, ypix);
	    fprintf (pltout, "raster\n");
	} else {
            fprintf (pltout, "  /Decode [ 0 1 ]\n");
            fprintf (pltout, "  /MaskColor [ 0 0 ]\n");
            fprintf (pltout, ">> image\n");
	}

	if (dither_it)
	{
	    for (j = 0; j < xpix*ypix; j+=80)
	    {
	   	for (i=j; (i<j+80 && i<xpix*ypix); i++)
	   	{
	            if (!corners && ci == (int) raster_block[0][i])
	                fprintf (pltout, "%2.2x", 0);
	            else
		        fprintf (pltout, "%2.2x", 255 - (int) raster_block[0][i]);
	   	}
    	   	fprintf (pltout, "\n");
	    }
	}
	else
	{
	    for (j = 0; j < xpix*ypix; j+=80)
	    {
	   	for (i=j; (i<j+80 && i<xpix*ypix); i++)
	   	{
	            if (!corners && ci == (int) raster_block[0][i])
	                fprintf (pltout, "%2.2x", 0);
	            else
		        fprintf (pltout,"%2.2x", 255 - ps_grey_ras[(int) raster_block[0][i]]);
	   	}
    	   	fprintf (pltout, "\n");
	    }
	}
    } else if (rgb_colorspace) {
        if (corners) {
            fprintf (pltout, "/colraster {%d %d 8 [ %d 0 0 %d 0 %d ] {currentfile picstr readhexstring pop } false 3 colorimage} def\n", xpix, ypix, xpix, -ypix, ypix);
            fprintf (pltout, "colraster\n");
	} else {
            fprintf (pltout, "  /Decode [ 0 1 0 1 0 1 ]\n");
            fprintf (pltout, "  /MaskColor [ 0 0 0 0 0 0 ]\n");
            fprintf (pltout, ">> image\n");
	}

	for (j = 0; j < xpix*ypix; j+=80)
	{
	    for (i=j; (i<j+80 && i<xpix*ypix); i++)
	    {
	        if (!corners && ci == (int) raster_block[0][i])
		    if (force_raster) 
			fprintf (pltout, "%2.2x%2.2x%2.2x", 0, 0, 0);
		    else
			fprintf (pltout, "%2.2x%2.2x%2.2x", 255, 255, 255);
	        else
		    if (force_raster) 
			fprintf (pltout, "%2.2x%2.2x%2.2x", red[(int) raster_block[0][i]],green[(int) raster_block[0][i]],blue[(int) raster_block[0][i]]);
		    else
			fprintf (pltout, "%2.2x%2.2x%2.2x", 255 - red[(int) raster_block[0][i]],255 - green[(int) raster_block[0][i]],255 - blue[(int) raster_block[0][i]]);
	    }
	    fprintf (pltout, "\n");
	}
    } else {
        /* RGB=no. Use CMYK colorspace */
/*
 * The "colorimage" command uses RGB if 3 bytes per pixel are specified,
 * but CMYK if 4 bytes per pixel are specified.
 */
        if (corners) {
            fprintf (pltout, "/colraster {%d %d 8 [ %d 0 0 %d 0 %d ] {currentfile picstr readhexstring pop } false 4 colorimage} def\n", xpix, ypix, xpix, -ypix, ypix);
            fprintf (pltout, "colraster\n");
	} else {
            fprintf (pltout, "  /Decode [ 0 1 0 1 0 1 0 1 ]\n");
            rgb_to_cmyk(0, 0, 0,
                        &cmyk_cyan, &cmyk_magenta, &cmyk_yellow, &cmyk_black);
            fprintf (pltout, "  /MaskColor [ %d %d %d %d %d %d %d %d ]\n",
                     cmyk_cyan, cmyk_cyan, cmyk_magenta, cmyk_magenta,
                     cmyk_yellow, cmyk_yellow, cmyk_black, cmyk_black);
            fprintf (pltout, ">> image\n");
	}

	for (j = 0; j < xpix*ypix; j+=80)
	{
	    for (i=j; (i<j+80 && i<xpix*ypix); i++)
	    {
	        if (!corners && ci == (int) raster_block[0][i]) {
		    if (force_raster)
			rgb_to_cmyk(0, 0, 0,
				    &cmyk_cyan, &cmyk_magenta, &cmyk_yellow, &cmyk_black);
		    else
			rgb_to_cmyk(255, 255, 255,
				    &cmyk_cyan, &cmyk_magenta, &cmyk_yellow, &cmyk_black);
		    fprintf (pltout, "%2.2x%2.2x%2.2x%2.2x",
			     cmyk_cyan, cmyk_magenta, cmyk_yellow, cmyk_black);
                } else {
		    if (force_raster)
			rgb_to_cmyk(red[(int) raster_block[0][i]],green[(int) raster_block[0][i]],blue[(int) raster_block[0][i]],
				    &cmyk_cyan, &cmyk_magenta, &cmyk_yellow, &cmyk_black);
		    else
			rgb_to_cmyk(255 - red[(int) raster_block[0][i]],255 - green[(int) raster_block[0][i]],255 - blue[(int) raster_block[0][i]],
				    &cmyk_cyan, &cmyk_magenta, &cmyk_yellow, &cmyk_black);
		    fprintf (pltout, "%2.2x%2.2x%2.2x%2.2x",
			     cmyk_cyan, cmyk_magenta, cmyk_yellow, cmyk_black);
                }
	    }
	    fprintf (pltout, "\n");
	}
    }

    fprintf (pltout, "grestore\n");
}

void psreset (void)
/*< reset >*/
{
    int             ii;

    if (mono)
    {
	for (ii = 0; ii < 8; ii++)
	{
	    ps_grey_map (ii);
	}

	psattributes (SET_COLOR, 7, 0, 0, 0);
    }
}

/*
 *  font name definitions
 *  font numbers start with 100
 */
static const char *psfonts[] = {
    "Courier-Bold",
    "Courier-BoldOblique",
    "Courier-Oblique",
    "Courier",
    "Helvetica-Bold",
    "Helvetica-BoldOblique",
    "Helvetica-Oblique",
    "Helvetica",
    "Symbol",
    "Times-Bold",
    "Times-BoldItalic",
    "Times-Italic",
    "Times-Roman",
    "AvantGarde-Book",
    "AvantGarde-BookOblique",
    "AvantGarde-Demi",
    "AvantGarde-DemiOblique",
    "Bookman-Demi",
    "Bookman-DemiItalic",
    "Bookman-Light",
    "Bookman-LightItalic",
    "Helvetica-Narrow-Bold",
    "Helvetica-Narrow-BoldOblique",
    "Helvetica-Narrow-Oblique",
    "Helvetica-Narrow",
    "NewCenturySchlbk-Bold",
    "NewCenturySchlbk-BoldItalic",
    "NewCenturySchlbk-Italic",
    "NewCenturySchlbk-Roman",
    "Palatino-Bold",
    "Palatino-BoldItalic",
    "Palatino-Roman",
    "Palatino-Italic",
    "ZapfChancery-MediumItalic",
    "ZapfDingbats"
};

int psmaxfont = {(sizeof(psfonts) / sizeof(psfonts[0])) + 100};

extern int      default_ps_font;

void pstext (char *string, float pathx, float pathy, float upx, float upy)
/*< text >*/
{
    double          fpathx, fpathy; /* fupx, fupy; */
    double          path;
    int             txsize, orient;
    double          yfact, xfact;
    static char     last_size = 0, last_font;

    endpath ();

    if (*string == '\0')
	return;

    if (dev.txfont > psmaxfont)
    {
	dev.txfont = default_ps_font;
    }

    if (dev.txfont < 100)
    {
	gentext (string, pathx, pathy, upx, upy);
	return;
    }

/*
 * Set the inital parameters
 */
    fpathx = (double) pathx;
    fpathy = (double) pathy;
/*    fupx = (double) upx;
      fupy = (double) upy; */

    path = sqrt ((double) (fpathx * fpathx + fpathy * fpathy));
    /* up = sqrt ((double) (fupx * fupx + fupy * fupy)); */

    path_orient_dx = fpathx / path;

/*
 * Postscript manual says height of "700 units" for the default
 * "1000 unit high" font is a typical "cap height". Vplot scales
 * by cap height, so we have to rescale by (1000./700.).
 * But I find that 570 is a better number!
 */
    txsize = ROUND (path * 1000. / 570.);
    orient = ROUND (acos (path_orient_dx) * 180 / SF_PI);
    if (pathy < 0)
	orient *= -1;

/*
 *   Set the font and size
 */
    if ((txsize != last_size) || (dev.txfont != last_font))
    {
	fprintf (pltout, "/%s findfont %d scalefont setfont\n",
		 psfonts[dev.txfont - 100], txsize);
	last_size = txsize;
	last_font = dev.txfont;
    }

    /*
     * SAVE THE CURRENT GRAPHICS STATE, ROTATE AND/OR SCALE THE COORDINATE
     * SYSTEM BEFORE MOVING
     */
    fprintf (pltout, "gsave\n");

    fprintf (pltout, "%d  %d translate\n", xold, yold);
    fprintf (pltout, "%d rotate\n", orient);


/*
 *  SET THE PROPER ALIGNMENT FROM THE CALCULATED LENGTH OF THE
 *  TEXT STRING
 */
    fprintf (pltout, "(%s) stringwidth pop\n", string);

    switch (txalign.ver)
    {
	case TV_TOP:
	    yfact = -0.81 * (float) txsize;	/* was -1.0 */
	    break;
	case TV_CAP:
	    yfact = -0.654 * (float) txsize;	/* was -0.8 */
	    break;
	case TV_SYMBOL:		/* CHECK THIS!!! */
	case TV_HALF:
	    yfact = -0.327 * (float) txsize;	/* was -0.45 */
	    break;
	case TV_BOTTOM:
	    yfact = .1666666667 * (float) txsize;	/* was - */
	    break;
	case TV_BASE:
	default:
	    yfact = 0.0;
	    break;
    }

    switch (txalign.hor)
    {
	case TH_RIGHT:
	    xfact = -1.;
	    break;
	case TH_NORMAL:
	case TH_LEFT:
	    xfact = 0.;
	    break;
	case TH_CENTER:
	case TH_SYMBOL:
	default:
	    xfact = -.5;
	    break;
    }
    fprintf (pltout, "%.2f mul\n", xfact);
    fprintf (pltout, "%.2f m\n", yfact);

    fprintf (pltout, "(%s) show\n", string);

    fprintf (pltout, "grestore\n");
}

void psvector (int x1, int y1, int x2, int y2, int nfat, int dashon)
/*< vector >*/
{
    static int      xlst, ylst;

/* Negative fatness? Skip it. */
    if (nfat < 0)
	return;

/* Clipped away? Skip it. */
    if (clip (&x1, &y1, &x2, &y2))
	return;

/*
 * ALAS, some postscript devices cannot be trusted to do their own
 * fattening. So we provide an option to do it all in the vplot
 * driver.
 */
    if (dumb_fat)
    {
	/* Have to dash FIRST */
	if (dashon)
	{
	    dashvec (x1, y1, x2, y2, nfat, dashon);
	    return;
	}

	/* Then fatten the resulting line segments SECOND */
	if (nfat)		/* Recursively calls itself to make fat lines */
	{
	    fatvec (x1, y1, x2, y2, nfat, dashon);
	    return;
	}

	/*
	 * (Unfortunately this means that if we do fattening in software we
	 * also have to do dashing in software.)
	 */
    }

/*
 *--------------------------------------------------------------------------
 * If dumb_fat == YES, then if we get to this point we must be
 * dealing with thin undashed lines. Just let the default code handle it;
 * it'll keep track of everything properly and won't try to do
 * anything because it will never need to be done.
 *--------------------------------------------------------------------------
 */

/*
 * set the fatness for the path
 */
    if (nfat != ps_last_fat)
    {
	endpath ();
	fprintf (pltout, "%d setlinewidth\n", nfat);
	ps_last_fat = nfat;
    }

/*
 * Make sure line dashing style is set correctly. The dashing pattern
 * was set in psattr, but it may or may not be turned on because
 * vplot can draw solid lines at any time without warning. Also,
 * if a new clipping window has been defined the dash pattern will have
 * been completely forgotten. So we have five cases to deal with:
 *
 * dashon=0 and !ps_dash_pattern_set -> thin line is default; just draw
 * dashon>0 and  ps_dash_pattern_set -> ready to draw dashed; just draw
 * dashon=0 and  ps_dash_pattern_set -> save the dash pattern
 *				        set solid line
 *				        ps_dash_pattern_set = NO
 *				        draw
 * dashon>0 and !ps_dash_pattern_set ->
 *				if (ps_dash_pattern_exists) then
 *					reload saved dash pattern
 *				        ps_dash_pattern_set = YES
 *				        draw
 *				else
 *					recreate lost pattern (ps_set_dash)
 *				        (sets ps_dash_pattern_set = YES)
 *				        (sets ps_dash_pattern_exists = YES)
 *					draw
 *				endif
 */
    if (dashon == 0 && ps_dash_pattern_set)
    {
	endpath ();
	fprintf (pltout, "currentdash\n");
	fprintf (pltout, "/vplotoffset exch def\n");
	fprintf (pltout, "/vplotdash exch def\n");
	fprintf (pltout, "[] 0 setdash\n");
	ps_dash_pattern_set = NO;
    }
    else if (dashon != 0 && !ps_dash_pattern_set)
    {
	if (ps_dash_pattern_exists)
	{
	    endpath ();
	    fprintf (pltout, "vplotdash vplotoffset setdash\n");
	    ps_dash_pattern_set = YES;
	}
	else
	{
	    endpath ();
	    /* This will set ps_dash_pattern_set and ps_dash_pattern_exists */
	    ps_set_dash (dashon);
	}
    }

    if ((x1 != xlst) || (y1 != ylst) || dev.lost == 1)
    {
	/* Make sure it is a move, not a draw */
	psplot (x1, y1, 0);
    }
    psplot (x2, y2, 1);
    xlst = x2;
    ylst = y2;
}

/*
 * Convert from RGB (what vplot uses) to CMYK (required by some
 * noncompliant postscript interpreters that can't convert from RGB
 * to CMYK themselves).
 * Input and output values range between 0 and 255.
 * This version maximizes the amount of black used.
 */
void rgb_to_cmyk (int red, int green, int blue,
                  int *cyan, int *magenta, int *yellow, int *black)
{
/*
 * First, calculate the color using just Cyan, Magenta, and Yellow
 * ink.
 */
    *cyan = 255 - red;
    *magenta = 255 - green;
    *yellow = 255 - blue;

/*
 * Find the minimum of the three.
 */
    *black = 255;
    if (*black > *cyan) *black = *cyan;
    if (*black > *magenta) *black = *magenta;
    if (*black > *yellow) *black = *yellow;

    if (*black == 255)
    {
/* Their color is black. So just use black ink with no color inks. */
	*cyan = 0;
	*magenta = 0;
	*yellow = 0;
    }
    else
    {
/* Use as much black as possible, then as much of other colors as needed */
	*cyan    = (int) (.5 + 255. * (float) (*cyan - *black) / (float) (255 - *black));
	*magenta = (int) (.5 + 255. * (float) (*magenta - *black) / (float) (255 - *black));
	*yellow  = (int) (.5 + 255. * (float) (*yellow - *black) / (float) (255 - *black));
    }
}
/*
  Copyright (C) 1987 The Board of Trustees of Stanford University
  
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
*/

/*
 *
 *  source file:   ./filters/init_vplot.c
 *
 * Joe Dellinger (SEP), Feb 18 1988
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Joe Dellinger, Feb 20 1988
 *	#define GETPAR to be fetch if SEPlib version.
 * Joe Dellinger Feb 24 1988
 * 	Moved gen_do_dovplot to genlib, where it belongs.
 *	txfont, txprec, txovly, overlay defaults remembered.
 * Joe Dellinger Feb 28 1988
 *	Changed fatness to scale with size of screen and scale,
 *	like any regular geometric attribute.
 * Joe Dellinger Mar 4 1988
 *	Fixed slight bug with fatness scaling and style=old.
 * Joe Dellinger Mar 17 1988
 *	Added "colormask" option.
 * Joe Dellinger April 15 1988
 *	Check for illegal colormask values.
 * Joe Dellinger Oct 28 1988
 *	Put in "no_stretch_text" flag.
 * Steve Cole Feb 2 1989
 *      Added default x and y scale parameters for use by vppen.
 * Joe Dellinger May 7 1989
 *	Added break=ignore option.
 *	Made txsquare=yes the default.
 * Joe Dellinger May 20 1989
 *	"/dev/tty" may NOT be openable. Behave gracefully in this case.
 * Joe Dellinger August 2 1989
 *	Put in redpow, greenpow, bluepow, redmap, greenmap, bluemap
 * W. Bauske IBM 03-26-91 
 *	Apply the SysV fixes to the code for the RS/6000
 *	Removed re-declare of system alloc routines for RS/6000
 * Dave Nichols 9-17-92
 *      Include stdlib.h if it is available instead of defining malloc.  
 * Stew Levin  2/27/95 
 *	Solaris mods.
 * Bob Clapp 1/24/96
 *      Changed a whole bunch of fetches to getches
 * Bob Clapp 10/98 
 *      Changed signals from bsd to posix1 for linux
 */

#include	<stdio.h>
#include	<math.h>

extern FILE * fdopen (int fd, const char *mode);

#include	<sys/ioctl.h>
#include	<sys/types.h>
#include	<sys/stat.h>
#include <fcntl.h>

#include <unistd.h>

#include	<ctype.h>
#include	<string.h>

#include <rsfplot.h>
/*^*/

#include	"../include/params.h"	/* for machine dependencies */
#include	"../include/enum.h"
#include	"../include/err.h"
#include	"../include/attrcom.h"
#include	"../include/intcom.h"
#include	"../include/mesgcom.h"
#include	"../include/erasecom.h"
#include	"../include/closestat.h"
#include	"../include/pat.h"
#include	"../include/vertex.h"
#include	"../include/round.h"
#include	"../include/extern.h"

#include "../utilities/util.h"
#include "../genlib/genpen.h"

#include "init_vplot.h"

#define		OPEN_ERROR	-1

/*
 * Other things that may need to be reset in dev.open
 * (Can't reset them some of them in dev.reset, because the user may
 * override from the command line.)
 */
/* should pipes be allowed for input? */
int             allow_pipe = YES;

/*
 * These may be reset to device-dependent defaults.
 */
float           fatmult = 1.;
float           patternmult = 1.;

/*
 * Look in extern.h for a better-organized list of the preceding.
 * Here I have left things which are also filter options with the
 * other filter options, even though they also belong in the above
 * categories.
 */

/*
 * flags and variables
 */
char            callname[25];
int             xcenterflag, ycenterflag;
int             ever_called = NO;
int             first_time = YES;
int             device_open = NO;	/* used by ERR */
int             out_isatty = YES;	/* If NO, output is a file or pipe */
int             nplots = 0;	/* number of plots made */
bool             no_stretch_text = true;	/* Don't allow stretched text? */

/*
 * coordinate variables
 */
int             xwmax, xwmin, ywmax, ywmin;	/* window */
int             xnew, ynew;	/* new pen location */
int             xold, yold;	/* old pen location */
char           *txbuffer;
int             txbuflen, vxbuflen;
struct vertex  *vxbuffer;
int             xret, yret;
float           mxx, mxy, myx, myy;
/*
 * This is so the device can throw in a coordinate transformation
 * for its convenience ON TOP OF whatever transformation the user
 * wants.
 */
int             default_rotate = 0, default_hshift = 0, default_vshift = 0;
float           default_scale = 1., default_xscale = 1., default_yscale = 1.;

/*
 * attribute variables
 */
int             linestyle;
int             cur_color = DEFAULT_COLOR;
int             pat_color = DEFAULT_COLOR + 1;
int             next_color;

int             default_txfont, default_txprec, default_txovly;
int             fat = 0;
int             afat = 0;
int             ipat = 0;	/* currently loaded pattern */
struct pat      pat[NPAT + 1];
float           dashsum = 0.;
int             dashon = NO;	/* Dashed lines? */
float           dashes[MAXDASH * 2];
float           dashpos = 0.;	/* Position in current dashing pattern */
int             color_set[MAX_COL + 1][_NUM_PRIM];
int             num_col_8;


/*
 * filter options - flags
 */

/*
 * Invras determines the polarity of dithered raster.
 * invras=n means raster works the same way as vectors; what is normally
 * WHITE on most devices is BLACK on a hardcopy black and white device.
 * invras=y is the proper default to make dithered images not come out as negatives
 */
bool             invras = true;
bool             window = true;
bool             shade = true;
bool             framewindows = false;
bool             endpause = false;
bool             honor_background = true;

bool             wantras = true;
bool             colormask[5];

/*
 * filter options - enumerated
 */
vp_plotstyle    style = VP_NO_STYLE_YET;
vp_plotstyle    default_style = VP_STANDARD;
int             rotate;
int             size = RELATIVE;
int             erase = FORCE_INITIAL | DO_LITERALS;

/*
 * filter options - valued
 */
int             xcenter, ycenter;	/* Vplot of point to force as center */
int             fatbase = 0;
int             epause = 0;	/* time to pause before erasing screen */
bool            overlay = false;	/* 1=overlay 0=replace */
int             default_overlay;
bool		serifs_OK = true;  /* If false, substitute serif fonts */

/*
 * 0 = none
 * 1 = random
 * 2 = Ordered
 * 3 = Floyd-Steinberg
 * 4 = Halftone
 */
int             dither = 1;	/* Dithering type */

int             xWmax, xWmin, yWmax, yWmin;
float           hshift, vshift;	/* Allow global translation of plot */
float           scale;	/* global scale */
float           xscale;	/* global x-scale */
float           yscale;	/* global y-scale */
float           hdevscale;	/* Vplot units to device units for x */
float           vdevscale;	/* Vplot units to device units for y */
float           txscale;/* global text scale */
float           mkscale;/* global marker scale */
float           dashscale;	/* global dashed line scale */
char            *interact=NULL;	/* Where to store coordinate
						 * file */
float           greyc = 1.;	/* Nonlinear correction */
float           pixc = 1.;	/* Pixel overlap correction */
float           redpow = 1., redmap[4] = {1., 0., 0., 0.};
float           greenpow = 1., greenmap[4] = {0., 1., 0., 0.};
float           bluepow = 1., bluemap[4] = {0., 0., 1., 0.};

/* filter options - resettable between plots */
int             user_rotate;
float           user_txscale;
float           user_mkscale;
float           user_dashscale;
float           user_scale;
float           user_xscale;
float           user_yscale;
int             user_size;
float           user_hshift;
float           user_vshift;
bool             user_xwmax_flag;
float           user_xwmax;
bool             user_ywmax_flag;
float           user_ywmax;
bool             user_xwmin_flag;
float           user_xwmin;
bool            user_ywmin_flag;
float           user_ywmin;

int             ifat = 0;
float           fatmult_orig;

bool mono;

/*
 * file and terminal control variables
 */
int             pltoutfd, stderrfd, controlfd;
FILE *pltout;

void  (*message) (int command, const char* string) = genmessage;
struct stat     stderrstat;
struct stat     pltoutstat;
FILE           *pltin;

FILE           *controltty;
char            outbuf[BUFSIZ];

#include <stdlib.h>

char            group_name[MAXFLEN + 1];
int             group_number = 0;
FILE           *pltinarray[MAXIN];
char            pltinname[MAXIN][MAXFLEN + 1];
char            pltname[MAXFLEN + 1] = "";

extern void reset_windows (void);

void init_vplot (int argc, char* argv[])
/*< Initialize and declare global variables. >*/
{
    char           *stringptr;
    int             ii;
    char            *string;
    float           ftemp;


    txbuffer = (char *) malloc (TXBUFLEN);
    txbuflen = TXBUFLEN;
/*
 * Sun III lint complains about "pointer alignment problem" here,
 * although the documentation makes it sound like that shouldn't
 * be possible.
 */
    vxbuffer = (struct vertex *) malloc (sizeof (struct vertex) * VXBUFLEN);
    vxbuflen = VXBUFLEN;

    /*
     * If the device can't do color, it can set mono to YES If device is
     * mono, this overrides the user's insistence that it isn't. So GETPAR
     * before we call dev.open. 
     */
    if (!sf_getbool ("mono",&mono)) mono=false;
    /* no color */

    /*
     * Initialize all patterns to be undefined. (device can create a
     * device-dependent default set if it wishes) 
     */
    for (ii = 0; ii <= NPAT; ii++)
    {
	pat[ii].patbits = NULL;
    }

/*
 * The device-independent code MAY NOT actually read from
 * the terminal itself. However, these variables are 
 * declared so that the device-dependent routines can use
 * them if they wish as a courtesy.
 */
    controlfd = open ("/dev/tty", 0);
    if (controlfd == OPEN_ERROR)
    {
	controltty = NULL;
    }
    else
    {
	controltty = fdopen (controlfd, "r");
    }

    pltout = stdout;

    /*
     * Call device open before doing anything else. this finalizes pltout 
     */
    dev.open (argc,argv);
    device_open = YES;

    /*
     * If graphics output going to control terminal, disable echoing and
     * arrange for use of device's message routine 
     */
    pltoutfd = fileno (pltout);
    stderrfd = fileno (stderr);
    out_isatty = isatty (pltoutfd);

    sf_getbool ("endpause", &endpause);
    sf_getbool ("cachepipe",&dev.cachepipe);
    sf_getbool ("shade", &shade);
    sf_getbool ("wantras", &wantras);
    sf_getbool ("window", &window);
    sf_getbool ("frame", &framewindows);
    sf_getbool ("overlay", &overlay);
    default_overlay = overlay;
    sf_getbool ("invras", &invras);
    sf_getbool ("txsquare", &no_stretch_text);
    sf_getbool ("serifs", &serifs_OK);
    sf_getbool ("background",&honor_background);

    if (!sf_getbools ("colormask",colormask,5)) 
	colormask[0] = colormask[1] = colormask[2] = 
	    colormask[3] = colormask[4] = true;
    if (!colormask[4] && colormask[3]) colormask[4] = true;

    if (!sf_getfloat ("redpow",  &redpow)) redpow=1.0;
    if (!sf_getfloat ("greenpow",  &greenpow)) greenpow=1.0;
    if (!sf_getfloat ("bluepow",  &bluepow)) bluepow=1.0;

    if (redpow <= 0. || greenpow <= 0. || bluepow <= 0.)
	ERR (FATAL, name, "Invalid color pow option.");
    
    sf_getfloats ("red",  redmap, 4);
    sf_getfloats ("green",  greenmap, 4);
    sf_getfloats ("blue",  bluemap, 4);

    sf_getint ("dither",  &dither); /* dithering to improve raster display, see "man vplotraster"
                    0    No dither,
                    1    Random Dither
                    2    Ordered Dither
                    3    Minimized Average Error Method
                    4    Digital Halftoning */
    sf_getfloat ("greyc",  &greyc); /* "grey correction" modifies the grey scale used to display a raster to simulate the nonlinearity of displays, see "man vplotraster" */
    sf_getfloat ("pixc",  &pixc);   /* "pixel  correction" controls  alteration of the grey scale, see "man vplotraster". */

    sf_getint ("txfont",  &dev.txfont);
    sf_getint ("txprec",  &dev.txprec);
    sf_getint ("txovly",  &dev.txovly);

    if (! serifs_OK)
    {
        if (dev.txfont == DEFAULT_HARDCOPY_FONT) dev.txfont = DEFAULT_SANSSERIF_FONT;
        if (dev.txfont == GREEK_SERIF_FONT) dev.txfont = GREEK_SANSSERIF_FONT;
    }

    default_txfont = dev.txfont;
    default_txprec = dev.txprec;
    default_txovly = dev.txovly;

    if (NULL != (string = sf_getstring ("erase")))
    {
	if ((string[0] == 'n') || (string[0] == 'N'))
	    erase = NO;
	else
	if ((string[0] == 'o') || (string[0] == 'O'))
	    erase = FORCE_INITIAL;
	else
	if ((string[0] == 'l') || (string[0] == 'L'))
	    erase = DO_LITERALS;
	else
	    erase = FORCE_INITIAL | DO_LITERALS;
    }

    if (NULL != (string = sf_getstring ("break")))
    {
	if (string[0] == 'b')
	    dev.brake = BREAK_BREAK;
	else
	if (string[0] == 'e')
	    dev.brake = BREAK_ERASE;
	else
	    dev.brake = BREAK_IGNORE;
    }

    xcenter = 0;
    ycenter = 0;
    xcenterflag = NO;
    ycenterflag = NO;
    if (sf_getfloat ("xcenter",  &ftemp))
    {
	xcenterflag = YES;
	xcenter = ROUND (ftemp * RPERIN);
    }
    if (sf_getfloat ("ycenter",  &ftemp))
    {
	ycenterflag = YES;
	ycenter = ROUND (ftemp * RPERIN);
    }

    if ((stringptr = getenv ("PATTERNMULT")) != NULL)
    {
	sscanf (stringptr, "%f", &patternmult);
    }
    if (!sf_getfloat ("patternmult",  &patternmult)) patternmult = 1.;

    interact = sf_getstring ("interact");
    if (!sf_getint ("pause",  &epause)) epause=0;

    if (NULL != interact)
    {
	epause = 0;		/* interact makes it own sort of pausing */
	endpause = false;
    }

    /*
     * Find the default style 
     */
    stringptr = NULL;
    if (NULL != (string = sf_getstring ("style")))
	stringptr = string;
    else
	stringptr = getenv ("PLOTSTYLE");
    if (stringptr != NULL)
    {
	if ((stringptr[0] == 'r') || (stringptr[0] == 'R') ||
	    (stringptr[0] == 'm') || (stringptr[0] == 'M'))
	    default_style = VP_ROTATED;
	else
	if ((stringptr[0] == 'o') || (stringptr[0] == 'O'))
	    default_style = VP_OLD;
	else
	if ((stringptr[0] == 'a') || (stringptr[0] == 'A'))
	    default_style = VP_ABSOLUTE;
	else
	    default_style = VP_STANDARD;
    }

/*
 * Options changeable between calls to dovplot
 * (By calling reset_parameters or reset())
 * Dovplot calls reset every time it starts. It only calls
 * reset_parameters the first time.
 *
 * Things in this category:
 * user_*
 * fatmult_orig, fatbase
 */

    if (!sf_getfloat ("fatmult",  &fatmult)) {
	if ((stringptr = getenv ("FATMULT")) != NULL)
	{
	    sscanf (stringptr, "%f", &fatmult);
	}
    }

    fatmult_orig = fatmult;

    if (!sf_getint ("rotate",  &user_rotate)) user_rotate = 0;

    if (!sf_getfloat ("txscale",  &user_txscale)) user_txscale = 1.0;
    if (!sf_getfloat ("mkscale",  &user_mkscale)) user_mkscale = 1.0;
    if (!sf_getfloat ("dashscale",  &user_dashscale)) user_dashscale = 1.0;

    if (!sf_getfloat ("scale",  &user_scale)) user_scale = 1.0;
    if (!sf_getfloat ("xscale",  &user_xscale)) user_xscale = 1.0;
    if (!sf_getfloat ("yscale",  &user_yscale)) user_yscale = 1.0;

    user_size = size;
    if (NULL != (string = sf_getstring ("size")))
    {
	if ((string[0] == 'a') || (string[0] == 'A'))
	    user_size = VP_ABSOLUTE;
	else
	    user_size = RELATIVE;
    }

    if (!sf_getfloat ("hshift",  &user_hshift) &&
	!sf_getfloat ("xshift",  &user_hshift)) user_hshift = 0.;
    if (!sf_getfloat ("vshift",  &user_vshift) &&
	!sf_getfloat ("yshift",  &user_vshift)) user_vshift = 0.;

    user_xwmax_flag = sf_getfloat ("xwmax",  &user_xwmax);
    user_ywmax_flag = sf_getfloat ("ywmax",  &user_ywmax);
    user_xwmin_flag = sf_getfloat ("xwmin",  &user_xwmin);
    user_ywmin_flag = sf_getfloat ("ywmin",  &user_ywmin);

    if (!sf_getint ("fat",  &fatbase)) fatbase = 0;
    /* base line fatness */


/*
 *  These parameters can simply be changed at any time with no
 *  need for re-initialization of anything else:
 *
 *  shade, wantras
 *
 */

}

void init_colors (void)
/*< init colors >*/
{
int             ii;

    /*
     * Set up the default color table 
     */

/*
 * First 7 colors are assumed to map to the standard 7 pen colors
 * on ALL devices, even those with no settable colors!
 */
    for (ii = 0; ii < 8; ii++)
    {
/*     if(color_set[ii][STATUS]!=SET){*/
	    color_set[ii][STATUS] = SET;
	    color_set[ii][_RED] = MAX_GUN * ((ii & 2) / 2);
	    color_set[ii][_GREEN] = MAX_GUN * ((ii & 4) / 4);
	    color_set[ii][_BLUE] = MAX_GUN * ((ii & 1) / 1);
	    color_set[ii][_GREY] = greycorr ((int) ((MAX_GUN * ii) / 7));
/*   }*/
    }

    if (mono)
    {
	/* Monochrome devices are assumed to have no settable colors */
	dev.num_col = 0;
    }

    num_col_8 = (dev.num_col > 8) ? dev.num_col : 8;

    if (mono)
    {
	color_set[0][MAP] = 0;
	for (ii = 1; ii <= MAX_COL; ii++)
	{
/*     if(color_set[ii][STATUS]!=SET)*/
	    color_set[ii][MAP] = 7;
	}
	for (ii = num_col_8; ii < 256; ii++)
	{
/*     if(color_set[ii][STATUS]!=SET)*/
	    color_set[ii][_GREY] = color_set[((ii - 8) % 7) + 1][_GREY];
	}
	/* Put a grey scale in the upper half of the color table */
	for (ii = 256; ii <= MAX_COL; ii++)
	{
/*     if(color_set[ii][STATUS]!=SET)*/
	    color_set[ii][_GREY] = greycorr (ii - 256);
	}
    }
    else
    {
	/*
	 * Unmapped colors shouldn't be mapped; ie, they map to themselves 
	 */

	for (ii = 0; ii < num_col_8; ii++)
	{
	    color_set[ii][MAP] = ii;
	 }
	/*
	 * Colors outside the range of this terminal map cyclically back into
	 * colors 1 through 7 
	 */
	for (ii = num_col_8; ii <= MAX_COL; ii++)
	{
	    color_set[ii][MAP] = ((ii - 8) % 7) + 1;
	}
    }
}

void setstyle (vp_plotstyle new_style)
/*< set style >*/
{
    /*
     * Check to see if the style has changed 
     */
    if (new_style == style)
	return;

    style = new_style;
    reset_parameters ();
}

void reset_parameters (void)
/*< reset parameters >*/
{
    float           inches;	/* scaling base for y axis */
    float           screenheight, screenwidth;	/* true size of the screen */
    int             ix, iy;

    dev.xorigin = 0;
    dev.yorigin = 0;

    rotate = default_rotate;
    rotate += user_rotate;

    txscale = user_txscale;
    mkscale = user_mkscale;
    dashscale = user_dashscale;

    scale = default_scale * user_scale;
    xscale = default_xscale * user_xscale;
    yscale = default_yscale * user_yscale;

    fatmult = fatmult_orig;

    size = user_size;

    switch (style)
    {
/*
 * The old standard on the machine erebus.
 * Pretty much dead now. Still useful for some old programs nobody's
 * wanted to update.
 */
	case VP_OLD:
	    txscale /= 3.;
	    fatmult /= 3.;
	    scale *= 3.;
	    inches = VP_STANDARD_HEIGHT;
	    break;
/*
 * The old standard on the machine mazama. A useful coordinate system
 * for geological sorts of plots. 
 * The Y axis goes the long way, across the screen, which is the device's
 * horizontal axis.
 */
	case VP_ROTATED:
	    rotate += 90;
	    inches = VP_ROTATED_HEIGHT;
	    break;
	case VP_ABSOLUTE:
	    size = VP_ABSOLUTE;
	case VP_STANDARD:
	default:
	    inches = VP_STANDARD_HEIGHT;
	    break;
    }

    if (rotate >= 0)
	rotate = rotate % 360;
    else
	rotate = ((rotate % 360) + 360) % 360;

    mxx = cosf (SF_PI * rotate / 180.);
    myy = cosf (SF_PI * rotate / 180.);
    mxy = sinf (SF_PI * rotate / 180.);
    myx = -sinf (SF_PI * rotate / 180.);

    if (size == VP_ABSOLUTE)
    {
	vdevscale = dev.pixels_per_inch / (float) (RPERIN * dev.aspect_ratio);
	hdevscale = dev.pixels_per_inch / (float) RPERIN;
    }
    else
    {
	/*
	 * Fit the inches x inches unit square into a displayable box with
	 * aspect ratio SCREEN_RATIO 
	 */
	screenwidth = (dev.xmax - dev.xmin) * dev.pixels_per_inch;
	screenheight =
	 (dev.ymax - dev.ymin) * dev.pixels_per_inch * dev.aspect_ratio;
	if ((screenheight / screenwidth) > VP_SCREEN_RATIO)
	{
	    vdevscale = (VP_SCREEN_RATIO * ((dev.xmax - dev.xmin) / dev.aspect_ratio)) /
	     (inches * RPERIN);
	    hdevscale = vdevscale * dev.aspect_ratio;
	}
	else
	{
	    vdevscale = (dev.ymax - dev.ymin) / (inches * RPERIN);
	    hdevscale = vdevscale * dev.aspect_ratio;
	}
    }

    hshift = default_hshift;
    vshift = default_vshift;

    if (style == VP_ROTATED)
    {
	vshift += dev.ymax - dev.ymin;
    }

    yscale *= scale;
    xscale *= scale;
    mkscale *= scale;

/*
 * Set up fatness multiplication factor
 */
    fatmult *= scale * hdevscale * RPERIN / FATPERIN;

    /*
     * The point (xcenter,ycenter) in vplot coordinates is to be centered in
     * the screen. 
     */
    if (xcenterflag || ycenterflag)
    {
	vptodevxy (xcenter, ycenter, &ix, &iy);
	if (xcenterflag)
	{
	    hshift += (dev.xmax + dev.xmin) / 2 - ix;
	}
	if (ycenterflag)
	{
	    vshift += (dev.ymax + dev.ymin) / 2 - iy;
	}
    }

    hshift += user_hshift * dev.pixels_per_inch;
    vshift += user_vshift * dev.pixels_per_inch / dev.aspect_ratio;

/* plot window parameters defaulted */
/* to maximum size */

    devtovpw (dev.xmin, dev.ymin, dev.xmax, dev.ymax,
	      &xWmin, &yWmin, &xWmax, &yWmax);

    if (user_xwmax_flag)
	xWmax = ROUND (user_xwmax * RPERIN);
    if (user_ywmax_flag)
	yWmax = ROUND (user_ywmax * RPERIN);
    if (user_xwmin_flag)
	xWmin = ROUND (user_xwmin * RPERIN);
    if (user_ywmin_flag)
	yWmin = ROUND (user_ywmin * RPERIN);

    vptodevw (xWmin, yWmin, xWmax, yWmax, &xWmin, &yWmin, &xWmax, &yWmax);

    wlimit (dev.xmin, dev.xmax, &xWmin, &xWmax);
    wlimit (dev.ymin, dev.ymax, &yWmin, &yWmax);

    xwmax = xWmax;		/* plot window parameters defaulted */
    xwmin = xWmin;		/* to maximum size 		 */
    ywmax = yWmax;
    ywmin = yWmin;
    reset_windows ();
}

void wlimit (int min, int max, int *xmin, int *xmax)
/*< wlimit >*/
{
    if (*xmin < min)
	*xmin = min;

    if (*xmax > max)
	*xmax = max;
}
