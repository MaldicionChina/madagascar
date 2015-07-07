/* Vplot filter for the virtual vplot device.

Although it is perhaps not obvious, this program can be used to
"Capture the screen". Ie, you play with Pen options until you
get something you like, and then you can use those options with
this program to make a new vplot file that without any options
will draw the same thing.
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
 *  source file:   ./filters/vplib/vpattr.c
 *
 * Joe Dellinger (SEP), Dec 19 1987
 *	Inserted this sample edit history entry.
 *	Please log any further modifications made to this file:
 * Joe Dellinger (AMOCO), Nov 19 1994
 *	Keep track of what color table entries have been used.
 *	Don't bother to re-write out color table entries if
 *	doing so would have no effect.
 */

#include <stdio.h>

#include <rsfplot.h>

#include "../include/attrcom.h"
#include "../include/params.h"
#include "../include/extern.h"
#include "../include/round.h"
#include "../include/enum.h"
#include "../include/pat.h"
#include "../include/closestat.h"
#include "../include/err.h"
#include "../include/erasecom.h"
#include "../include/mesgcom.h"

#include "../genlib/genpen.h"
#include "../utilities/util.h"

#include "dovplot.h"
#include "init_vplot.h"

#include "_vp.h"
#include "vpdoc.h"

#include "vppen.h"

#include "_device.h"

extern int      allow_pipe;
extern int      first_time;
extern FILE *pltout;

bool             vpbig = true;
bool             vpdumb = false;
int             vpstat = NO;
int             vpfit = NO;
float           xsize = 0., ysize = 0.;
int             vpalign = NO;
bool             vpstyle = true;
bool             vpblast = true;
int             vpbit = 0;
const char     *vpaligns;
int             vparray[2] = {0, 0};
int             vpasize[2] = {0, 0};
int             vpframe = -1;

int             vpsetflag;

char            name[] = "vppen";

int             vpcolor = VP_WHITE;
int             vpfat = 0;

int		vpscoltabinfo[VPPEN_NUM_COL][4];
int		vpsetcoltabanyway = NO;

static int vpopen_name (int num);
static void vp_check_filep (FILE *plot);

void vpattributes (int command, int value, int v1, int v2, int v3)
/*< attributes >*/
{
    static float    vpdash[MAXDASH];
    static float    vpgap[MAXDASH];
    static int      vpndash;
    static int     *vpattrarray;
    static int      vpxwmin, vpywmin, vpxwmax, vpywmax;
    static int      vpfont1, vpfont2, vpfont3;
    static int      vpjust1, vpjust2;
    static int      vpcolt1, vpcolt2, vpcolt3, vpcolt4;
    static int      vpovly;
    int             ii, jj;

    dev.lost = YES;

    if (!vpdumb)
    {
	switch (command)
	{
	    case SET_COLOR:
		if (vpsetflag & F_COL)
		{
		    if (vpcolor == value)
			break;
		}
		vp_color (value);
		vpcolor = value;
		vpsetflag |= F_COL;
		break;

	    case SET_COLOR_TABLE:
		if (vpsetflag & F_COLT)
		{
		    if (vpcolt1 == value &&
			vpcolt2 == v1 &&
			vpcolt3 == v2 &&
			vpcolt4 == v3)
			break;
		}
/*
 * The only global attribute in vplot that stays set across
 * erases is the color table. If we're about to re-set this
 * color to the same thing it's already set to, then don't
 * bother! (Unless we've been told to do it anyway.)
 */
		if (vpsetcoltabanyway ||
		    vpscoltabinfo[value][ISITSET] != YES ||
		    vpscoltabinfo[value][1] != v1 ||
		    vpscoltabinfo[value][2] != v2 ||
		    vpscoltabinfo[value][3] != v3)
		{
		    vp_coltab (value,
			       (float) v1 / (float) MAX_GUN,
			       (float) v2 / (float) MAX_GUN,
			       (float) v3 / (float) MAX_GUN);
/*
 * A new one! Save it.
 */
		    vpscoltabinfo[value][ISITSET] = YES;
		    vpscoltabinfo[value][1] = v1;
		    vpscoltabinfo[value][2] = v2;
		    vpscoltabinfo[value][3] = v3;
		}

		vpcolt1 = value;
		vpcolt2 = v1;
		vpcolt3 = v2;
		vpcolt4 = v3;
		vpsetflag |= F_COLT;

		break;

	    case SET_WINDOW:

		if (vpsetflag & F_CLIP)
		{
		    if (value == vpxwmin &&
			v1 == vpywmin &&
			v2 == vpxwmax &&
			v3 == vpywmax)
			break;
		}

		vp_clip ((float) (value) / RPERIN, (float) (v1) / RPERIN,
			 (float) (v2) / RPERIN, (float) (v3) / RPERIN);
		vpxwmin = value;
		vpywmin = v1;
		vpxwmax = v2;
		vpywmax = v3;
		vpsetflag |= F_CLIP;
		break;

	    case NEW_DASH:
		if (vpsetflag & F_DASH)
		{
		    if (value == vpndash)
		    {
			jj = YES;
			for (ii = 0; ii < value; ii++)
			{
			    if (vpdash[ii] != dashes[2 * ii] ||
				vpgap[ii] != dashes[2 * ii + 1])
				jj = NO;
			}
			if (jj)
			    break;
		    }
		}

		for (ii = 0; ii < value; ii++)
		{
		    vpdash[ii] = dashes[2 * ii];
		    vpgap[ii] = dashes[2 * ii + 1];
		}
		vp_setdash (vpdash, vpgap, value);
		vpndash = value;
		vpsetflag |= F_DASH;
		break;

	    case NEW_PAT:
		vpattrarray = (int *) malloc ((unsigned)
					      (pat[value].xdim * pat[value].ydim * sizeof (int)));

		if (vpattrarray != NULL)
		{
		    for (ii = 0; ii < pat[value].xdim * pat[value].ydim; ii++)
			vpattrarray[ii] = pat[value].patbits[ii];

		    vp_patload ((int) RPERIN,
				pat[value].xdim, pat[value].ydim,
				value - 1, vpattrarray);

		    free ((char *) vpattrarray);
		}
		break;

	    case NEW_FONT:
		if (value == -1)
		    value = vpfont1;
		if (v1 == -1)
		    v1 = vpfont2;
		if (v2 == -1)
		    v2 = vpfont3;

		if (vpsetflag & F_FONT)
		{
		    if (vpfont1 == value &&
			vpfont2 == v1 &&
			vpfont3 == v2)
			break;
		}

		vp_tfont (value, v1, v2);
		vpfont1 = value;
		vpfont2 = v1;
		vpfont3 = v2;
		vpsetflag |= F_FONT;
		break;

	    case NEW_OVERLAY:
		if (vpsetflag & F_OVLY)
		{
		    if (vpovly == value)
			break;
		}
/*
 * Another libvplot command that doesn't exist but should.
 * XXXXXX
 *		vp_overlay(value);
 */
		vpsetflag |= F_OVLY;
		vpovly = value;
		break;

	    case NEW_ALIGN:
		if (vpsetflag & F_JUST)
		{
		    if (vpjust1 == value &&
			vpjust2 == v1)
			break;
		}
		vp_tjust (value, v1);
		vpjust1 = value;
		vpjust2 = v1;
		vpsetflag |= F_JUST;
		break;

	    case NEW_FAT:
		if (vpsetflag & F_FAT)
		{
		    if (vpfat == value)
			break;
		}

		vp_fat (ROUND (value * FATPERIN / RPERIN));
		vpfat = value;
		vpsetflag |= F_FAT;
		break;

	    case BEGIN_GROUP:
		if (value > 0)
		    vp_bgroup (group_name);
		break;

	    case END_GROUP:
		if (value > 0)
		    vp_egroup ();
		break;

	    default:
		break;
	}
    }
    else
    {
	switch (command)
	{
	    case SET_COLOR:
		if (vpsetflag & F_COL)
		{
		    if (vpcolor == value)
			break;
		}
		vp_color (value);
		vpcolor = value;
		vpsetflag |= F_COL;
		break;

	    default:
		break;
	}
    }
}

extern int      first_time;
extern int      style;
extern int      default_style;

int             vpxmax, vpxmin, vpymax, vpymin;
static int      vpxmaxs, vpxmins, vpymaxs, vpymins;

void vp_do_dovplot (int nn, FILE **inpltin, char *innames[])
/*< do vplot >*/
{
    int             ii;
    bool             save_wantras;
    bool             save_shade;
    char            string[80];
    static int      it_got_clipped;
    float           hh, ww;
    float           rescale_x, rescale_y;
    char            format_string[80];

    if (nn == 0)
	return;

/*
 * If they want statistics, make one "dummy" pass through first
 * before you really do it.
 * The align and fit options need these statistics to do their work.
 */
    if (vpalign || vpfit)
    {
	/*
	 * Turn on automatic processing 
	 */
	dev.smart_clip = false;
	dev.smart_raster = false;

	/*
	 * Just outline polygons and raster with vectors 
	 */
	save_wantras = wantras;
	save_shade = shade;

	wantras = false;
	shade = false;

	/*
	 * Turn off any actual output 
	 */
	dev.reset = nulldev;
	dev.message = vplogmessage;
	message = dev.message;
	dev.erase = vpderase;
	dev.close = nullclose;
	dev.vector = vplogvector;
	dev.marker = genmarker;
	dev.text = gentext;
	dev.area = nullarea;
	dev.raster = nullraster;
	dev.point = genpoint;
	dev.attributes = nullattributes;


/*
 * Now do the trial pass
 */

	vpxmaxs = dev.xmin;
	vpxmins = dev.xmax;
	vpymaxs = dev.ymin;
	vpymins = dev.ymax;

	it_got_clipped = NO;

	if (vpstat)
	{
	    if (vpstat == YES)
	    {
		strcpy (format_string,
			"%17s: h=%6.2f w=%6.2f; x=(%6.2f,%6.2f) y=(%6.2f,%6.2f)\n");
	    }
	    else
	    {
		strcpy (format_string,
			"%17s: h= %6.2f w= %6.2f ;  x=( %6.2f , %6.2f ) y=( %6.2f , %6.2f ) ");
	    }
	}

	for (ii = 0; ii < nn; ii++)
	{
	    vpxmax = dev.xmin;
	    vpxmin = dev.xmax;
	    vpymax = dev.ymin;
	    vpymin = dev.ymax;

	    pltin = inpltin[ii];
	    strcpy (pltname, innames[ii]);
	    dovplot ();
	    rewind (pltin);

	    if (vpxmaxs < vpxmax)
		vpxmaxs = vpxmax;
	    if (vpymaxs < vpymax)
		vpymaxs = vpymax;
	    if (vpxmins > vpxmin)
		vpxmins = vpxmin;
	    if (vpymins > vpymin)
		vpymins = vpymin;

/*
 * For vpstat=y, write out the statistics. Also note if any
 * parts of the plot got clipped.
 */
	    if (vpstat)
	    {
		hh = (float) (vpymax - vpymin) / RPERIN;
		ww = (float) (vpxmax - vpxmin) / RPERIN;

		if (hh < 0. || ww < 0.)
		{
		    printf ("%17s: clipped away. ",
			    innames[ii]);
		}
		else
		{
		    printf (format_string,
			    innames[ii],
			    hh, ww,
			    (float) vpxmin / RPERIN,
			    (float) vpxmax / RPERIN,
			    (float) vpymin / RPERIN,
			    (float) vpymax / RPERIN);
		}

		if (vpxmax == dev.xmin || vpxmax == dev.xmax ||
		    vpxmin == dev.xmax || vpxmin == dev.xmin ||
		    vpymax == dev.ymin || vpymax == dev.ymax ||
		    vpymin == dev.ymax || vpymin == dev.ymin)
		{
		    printf ("*\n");
		    it_got_clipped = YES;
		}
		else
		{
		    printf ("\n");
		}
	    }
	}

	if (vpstat && nn > 1)
	{
	    sprintf (string, "All %d", nn);
	    printf (format_string,
		    string,
		    (float) (vpymaxs - vpymins) / RPERIN,
		    (float) (vpxmaxs - vpxmins) / RPERIN,
		    (float) vpxmins / RPERIN,
		    (float) vpxmaxs / RPERIN,
		    (float) vpymins / RPERIN,
		    (float) vpymaxs / RPERIN);
	}

	if (vpstat)
	{
	    if (vpframecount == 0)
	        printf(
		    "            Total %d plot frame.\n", vpframecount + 1);
	    else
	        printf(
		    "            Total %d plot frames.\n", vpframecount + 1);

	    if (it_got_clipped)
	    {
		if (vpbig)
		{
		    printf (
			"\nA * indicates a plot that has been clipped.\n");
		    printf (
			"Remember rotated style or relative size plots go to the top\n");
		    printf (
			"of the \"screen\", which is infinitely far away if big=y.\n");
		}
		else
		{
		    printf (
			"\nA * indicates a plot that has been clipped at the\n");
		    printf (
			"virtual screen boundaries. You may not want this.\n");
		    printf (
			"This clipping can be disabled by the big=y option.\n");
		}
	    }

	    for (ii = 0; ii < nn; ii++)
	    {
		pltin = inpltin[ii];
		fclose (pltin);
	    }
/*
 * Statistics get changed by re-aligning anyways,
 * So might as well just exit if we're doing vpstat=y.
 */
	    return;
	}

/*
 * Compute scale factors for vpfit option.
 * These are passed to dovplot as default scales.
 * The user may have specified both xsize and ysize, or just one.
 * Specifying one but not both is a signal that vppen should choose
 * the other scale factor to preserve the plot's aspect ratio.
 */
	if (vpfit)
	{
	    if (xsize == 0.)
	    {
		xsize = ysize * (vpxmaxs - vpxmins) / (vpymaxs - vpymins);
	    }
	    if (ysize == 0.)
	    {
		ysize = xsize * (vpymaxs - vpymins) / (vpxmaxs - vpxmins);
	    }

	    rescale_x = xsize * RPERIN / (vpxmaxs - vpxmins);
	    vpxmaxs *= rescale_x;
	    vpxmins *= rescale_x;
	    default_xscale *= rescale_x;

	    rescale_y = ysize * RPERIN / (vpymaxs - vpymins);
	    vpymaxs *= rescale_y;
	    vpymins *= rescale_y;
	    default_yscale *= rescale_y;

/*
 * Scale fatness according to whichever dimension is more compressed
 */
	    if (rescale_x > rescale_y)
		fatmult_orig *= rescale_y;
	    else
		fatmult_orig *= rescale_x;

	}
/*
 * Compute shifts for vpalign and vpfit options.
 * These are passed to dovplot as the default shifts.
 */
	switch (vpaligns[0])
	    /*
	     * horizontal 
	     */
	{
	    case 'l':
		default_hshift += (0 - vpxmins);
		break;
	    case 'r':
		default_hshift += (0 - vpxmaxs);
		break;
	    case 'c':
		default_hshift += (0 - ((vpxmaxs + vpxmins) / 2));
		break;
	    case 'u':
		break;
	    default:
		ERR (WARN, name, "Unknown left-right alignment type %c.",
		     vpaligns[0]);
		break;
	}


	switch (vpaligns[1])
	    /*
	     * vertical 
	     */
	{
	    case 'b':
		default_vshift += (0 - vpymins);
		break;
	    case 't':
		default_vshift += (0 - vpymaxs);
		break;
	    case 'c':
		default_vshift += (0 - ((vpymaxs + vpymins) / 2));
		break;
	    case 'u':
		break;
	    default:
		ERR (WARN, name, "Unknown top-bottom alignment type %c.",
		     vpaligns[1]);
		break;
	}

	style = default_style;

	reset_parameters ();

	/*
	 * Lie to dovplot, tell it to start from scratch again 
	 */
	first_time = YES;

	/*
	 * Undo the damage from the first pass 
	 */
	wantras = save_wantras;
	shade = save_shade;

	dev.reset = vpreset;
	dev.message = vpmessage;
	message = dev.message;
	dev.erase = vperase;
	dev.close = nullclose;
	dev.vector = vpvector;
	dev.marker = vpmarker;
	dev.text = vptext;
	dev.area = genarea;
	dev.raster = vpraster;
	dev.point = genpoint;
	dev.attributes = vpattributes;
    }

/*
*********************************************************************
* "Real" pass
*********************************************************************
*/

    if (vpdumb)
    {
	dev.message = genmessage;
	dev.vector = genvector;
	dev.marker = genmarker;
	dev.text = gentext;
	dev.area = vecarea;
	dev.raster = genraster;
	dev.smart_clip = false;
	dev.smart_raster = false;
    }
    else
    {
	dev.smart_clip = true;
	dev.smart_raster = true;
    }
    dev.smart_background = true;

/* Second (or first) pass */
    for (ii = 0; ii < nn; ii++)
    {
	pltin = inpltin[ii];
	strcpy (pltname, innames[ii]);
	dovplot ();
	fclose (pltin);
    }
}

int      vpframecount = -1;

void vperase (int command)
/*< erase >*/
{
    int newout, ii;
    extern int vpsetcoltabanyway;


    if (vparray[0] == 0)
    {
	switch (command)
	{
	    case ERASE_START:
		vpframecount = 0;
		break;
	    case ERASE_MIDDLE:
		vpframecount++;
		newout = vpopen_name (vpframecount);
		vp_erase ();
		if (!vpdumb && vpstyle)
		{
		    vp_style (VP_ABSOLUTE);
		}
		dev.lost = YES;
		vpsetflag = NO;

		if (!vpdumb && newout)
		{
/*
 * If this is a new output file, then explicitly set the entire
 * color table to its current state.
 */
		    vpsetcoltabanyway = YES;
		    for (ii=0; ii < VPPEN_NUM_COL; ii++)
		    {
			if (vpscoltabinfo[ii][ISITSET])
			{
			    vpattributes (SET_COLOR_TABLE, ii,
					  vpscoltabinfo[ii][1],
					  vpscoltabinfo[ii][2],
					  vpscoltabinfo[ii][3]);
			}
		    }
		    vpsetcoltabanyway = NO;

		    dev.lost = YES;
		    vpsetflag = NO;
		}

		break;
	    case ERASE_BREAK:
		vp_break ();
		if (!vpdumb && vpstyle)
		{
		    vp_style (VP_ABSOLUTE);
		}
		dev.lost = YES;
		vpsetflag = NO;
		break;
	    case ERASE_BACKGROUND:
		if (!vpdumb)
		    vp_background();
		break;
	    default:
		break;
	}
    }
    else
    {
	switch (command)
	{
	    case ERASE_START:
		vpframecount = 0;
		dev.ymin = VP_STANDARD_HEIGHT * RPERIN;
	    case ERASE_MIDDLE:
		if (vpframecount < 0)
		    ERR (FATAL, name, "Must have initial erase with gridnum");
		if ((vpframecount % vparray[0]) == 0)
		{
		    dev.xmin = 0;
		    dev.ymin -= vpasize[1];
		}
		else
		{
		    dev.xmin += vpasize[0];
		}
		dev.xmax = dev.xmin + vpasize[0];
		dev.ymax = dev.ymin + vpasize[1];

		if (command == ERASE_MIDDLE)
		    vp_break ();

		dev.lost = YES;
		vpsetflag = NO;
		reset_parameters ();
		vpframecount++;

		if (vpframe >= 0)
		{
		    vp_color (VP_WHITE);
		    vp_fat (vpframe);

		    vp_move ((float) dev.xmin / RPERIN, (float) dev.ymin / RPERIN);
		    vp_draw ((float) dev.xmax / RPERIN, (float) dev.ymin / RPERIN);
		    vp_draw ((float) dev.xmax / RPERIN, (float) dev.ymax / RPERIN);
		    vp_draw ((float) dev.xmin / RPERIN, (float) dev.ymax / RPERIN);
		    vp_draw ((float) dev.xmin / RPERIN, (float) dev.ymin / RPERIN);

		    vp_color (vpcolor);
		    vp_fat (ROUND (vpfat * FATPERIN / RPERIN));
		}
		break;
	    case ERASE_BREAK:
		break;
	    case ERASE_BACKGROUND:
		if (!vpdumb)
		    vp_background();
		break;
	    default:
		break;
	}
    }
}

void vpderase (int command)
/*< Dummy erase command; does nothing but count frames. >*/
{
    switch (command)
    {
	case ERASE_START:
	    vpframecount = 0;
	    break;
	case ERASE_MIDDLE:
	    vpframecount++;
	    break;
	case ERASE_BREAK:
	    break;
	default:
	    break;
    }
}

static int      saveitlog;

void vplogmessage (int command, const char *string)
/*< logged message >*/ 
{
    switch (command)
    {
	case MESG_READY:
	    saveitlog = YES;
	    break;
	case MESG_MESSAGE:
	    saveitlog = NO;
	    break;
	case MESG_TEXT:
	    if (saveitlog)
		fprintf (stderr, "%s", string);
	    break;
	default:
	    break;
    }
}

extern int      vpxmax, vpxmin, vpymax, vpymin;

void vplogvector (int x1, int y1, int x2, int y2, int nfat, int vpdashon)
/*< log vector >*/
{
    if (clip (&x1, &y1, &x2, &y2))
	return;

    if (x1 > vpxmax)
	vpxmax = x1;
    if (x1 < vpxmin)
	vpxmin = x1;

    if (y1 > vpymax)
	vpymax = y1;
    if (y1 < vpymin)
	vpymin = y1;

    if (x2 > vpxmax)
	vpxmax = x2;
    if (x2 < vpxmin)
	vpxmin = x2;

    if (y2 > vpymax)
	vpymax = y2;
    if (y2 < vpymin)
	vpymin = y2;
}

void vpmarker (int npts, int type, int size, int *pvec)
/*< marker >*/
{
    float          *xp;
    float          *yp;
    int             ii;

    vpsetflag = NO;
    dev.lost = YES;

    xp = (float *) malloc ((unsigned) (npts * sizeof (float)));
    yp = (float *) malloc ((unsigned) (npts * sizeof (float)));

    for (ii = 0; ii < npts; ii++)
    {
	xp[ii] = (float) pvec[2 * ii] / RPERIN;
	yp[ii] = (float) pvec[2 * ii + 1] / RPERIN;
    }

    size = ROUND (size * TXPERIN / RPERIN);

    vp_pmark (npts, type, size, xp, yp);

    free ((char *) xp);
    free ((char *) yp);

}

static int      saveit;
static char     savestring[80 * 24];

void vpmessage (int command, const char *string)
/*< message >*/
{
    switch (command)
    {
	case MESG_READY:
	    saveit = NO;
	    break;
	case MESG_MESSAGE:
	    saveit = YES;
	    strcpy (savestring, "");
	    break;
	case MESG_DONE:
	    if (saveit && !vpdumb)
	    {
		vp_message (savestring);
	    }
	    break;
	case MESG_TEXT:

	    if (saveit)
	    {
		if (strcmp (string, CRLF) != 0)
		    (void) strcat (savestring, string);
	    }
	    else
	    {
		fprintf (stderr, "%s", string);
	    }

	    break;
	default:
	    break;
    }
}

void opendev (int argc, char* argv[])
/*< open >*/
{
    float           atemp[2];
    char            *vpstat_string;
    int		ii;
    
    dev.reset = vpreset;
    dev.message = vpmessage;
    dev.erase = vperase;

    dev.vector = vpvector;
    dev.marker = vpmarker;
    dev.text = vptext;
    dev.raster = vpraster;	
    dev.attributes = vpattributes;

    dev.reader = vp_do_dovplot;

    dev.plot = vpplot;
    dev.startpoly = vpstartpoly;
    dev.midpoly = vpmidpoly;
    dev.endpoly =vpendpoly;

    first_time = YES;
    
    
/*
 * Reset the saved global color table information array.
 */
    for (ii=0; ii < VPPEN_NUM_COL; ii++)
    {
	vpscoltabinfo[ii][ISITSET] = NO;
	vpscoltabinfo[ii][1] = 0;
	vpscoltabinfo[ii][2] = 0;
	vpscoltabinfo[ii][3] = 0;
    }

/*
 * Special options
 */
    if (!sf_getbool ("dumb", &vpdumb)) vpdumb=false;
    /* if y, causes output to only be vectors, erases, and color changes */
    if (!sf_getbool ("blast", &vpblast)) vpblast=true;
    /* if y, don't try to compact the output.  If n, compaction will
       be done.  Compaction does run-length encoding and compacts repeated
       lines.  Compaction can make the vplot file considerably smaller, but
       it also takes longer to create the file. */
    if (!sf_getint ("bit", &vpbit)) vpbit=0;
    /* if > 0,  then bit raster is used with bit the color */
    if (!sf_getint ("grid", &vpframe)) vpframe=-1;
    /* turns on drawing a grid, with the specified fatness */ 

    if (NULL != (vpstat_string = sf_getstring ("stat")))
	/*( stat=n if y, print plot statistics; if l, insert extra spaces )*/
    {
	if (vpstat_string[0] == 'y' || vpstat_string[0] == 'Y' ||
	    vpstat_string[0] == '1')
	    vpstat = YES;
	else
	    if (vpstat_string[0] == 'l' || vpstat_string[0] == 'L')
		vpstat = 2;
	    else
		vpstat = NO;
    }

    if (NULL == (vpaligns = sf_getstring ("align"))) vpaligns="uu";
    /* aligns plot accoording to xy:
       x is one of l, r, c, u for left, right, center, unaligned
       y is one of b, t, c, u for bottom, top, center, unaligned.
       In all cases the given point is aligned to have coordinate zero. */
    if (!sf_getfloat ("xsize", &xsize)) xsize=0.;
    if (!sf_getfloat ("ysize", &ysize)) ysize=0.;
    /* scale the vplot image to fit within a given size rectangle */
    if (xsize != 0. || ysize != 0.)
	vpfit = YES;
    
    if (vpstat || strcmp (vpaligns, "uu") != 0 || vpfit)
    {
	vpalign = YES;
	allow_pipe = NO;
    }

    if (!sf_getints ("gridnum", vparray, 2))
	vparray[0] = vparray[1] = 0;
    /*( gridnum grids the screen, each part has gridsize=xwidth,ywidth
      numy defaults to numx. [xy]size default to [xy]screensize /
      num[xy] )*/
    
    if (vparray[1] == 0)
	vparray[1] = vparray[0];
    
    if (vparray[0] != 0)
    {
	vpbig = false;
	vpstyle = false;
    }

    sf_getbool ("big", &vpbig);
    /* if y, expand the size of the device's screen (and hence
       outermost clipping window) to nearly infinity (bad for rotated
       style!) */
    sf_getbool ("vpstyle", &vpstyle);
    /* if n, omit declaring absolute style in the output file */
    if (vparray[0] != 0)
    {

/* Let it override.

if (vpbig || vpalign)
ERR (FATAL, name, "Incompatible option with gridnum");
*/

	if (!sf_getfloats ("gridsize", atemp, 2)) {
	    atemp[0] = (float) (VP_STANDARD_HEIGHT / VP_SCREEN_RATIO) / vparray[0];
	    atemp[1] = (float) (VP_STANDARD_HEIGHT) / vparray[1];	 
	}   

	vpasize[0] = floorf(0.5+atemp[0] * RPERIN);
	vpasize[1] = floorf(0.5+atemp[1] * RPERIN);
    }


/*
 * We want to go through the input files ourselves
 */

    dev.reader = vp_do_dovplot;

/*
 * device capabilities
 */

    if (vpbig)
    {
	dev.xmax = VP_MAX * RPERIN;
	dev.ymax = VP_MAX * RPERIN * VP_SCREEN_RATIO;
	dev.xmin = -dev.xmax;
	dev.ymin = -dev.ymax;
	default_hshift = -dev.xmin;
	default_vshift = -dev.ymin;
    }
    else
    {
	dev.xmax = VP_STANDARD_HEIGHT * RPERIN / VP_SCREEN_RATIO;
	dev.ymax = VP_STANDARD_HEIGHT * RPERIN;
	dev.xmin = 0;
	dev.ymin = 0;
	default_hshift = 0;
	default_vshift = 0;
    }

    dev.pixels_per_inch = RPERIN;
    dev.aspect_ratio = 1.;
    dev.num_col = VPPEN_NUM_COL;
    if (vparray[0] == 0)
	size = VP_ABSOLUTE;


/*
 * Since font gets hard-wired in after first pass,
 * make it a nice one if they don't specify it.
 */
    dev.txfont = DEFAULT_HARDCOPY_FONT;
    dev.txprec = DEFAULT_HARDCOPY_PREC;

/*
 * Make vplib routines more useful to be included in other programs
 * besides just vppen
 */


/*
 * To keep messages from being lost
 */
    message = dev.message;

    if (!vpstat) vpopen_name(0);
/*
 * The very first time we don't care whether vpopen_name opened an
 * output file or not; we'd have to initialize everything in any case!
 */

    dev.cachepipe = true;
}

static int vpopen_name (int num)
{
    char            *string, string2[20];
    char            *outname;
    static FILE    *vp_pltout = NULL;
    static int      gotwhich = 0;
    int		newout;


/*
 * If last time we opened a file for output, then this time
 * we'll also want to re-write the color table.
 */
    if (gotwhich > 0)
    {
	newout = 1;
    } else {
	newout = 0;
    }

    gotwhich = 0;

    if (NULL != (string = sf_getstring ("outN+")))
    {
	gotwhich = 2;
    }
    else if (NULL != (string = sf_getstring ("outN")))
	/*( outN redirect frames to corresponding files (include %d in
	 * the filename template) )*/
    {
	gotwhich = 1;
    }

    if (gotwhich)
    {
	outname = sf_charalloc(120);
	snprintf (outname, 120, string, num);
    } else {
	snprintf (string2, 20, "out%d+", num);
	if (NULL != (outname = sf_getstring (string2)))
	{
	    gotwhich = 2;
	}
	else
	{
	    snprintf (string2, 20, "out%d", num);
	    if (NULL != (outname = sf_getstring (string2)))
		gotwhich = 1;
	    /*( out# redirect frame # to corresponding file )*/
	}
    }

    if (gotwhich)
    {
	if (vp_pltout != (FILE *) NULL)
	    fclose (vp_pltout);

	if (gotwhich == 2)
	    vp_pltout = fopen (outname, "a");
	else
	    vp_pltout = fopen (outname, "w");

	if (vp_pltout == (FILE *) NULL)
	{
	    ERR (WARN, name, "Can't open %s", outname);
	    vp_check_filep (pltout);
	    vp_pltout = (FILE *) NULL;
	}
	else
	{
	    vp_check_filep (vp_pltout);
/*
 * If we're opening a new file for output, then
 * we'll need to re-write the color table at the start of it.
 */
	    newout = 1;
	}
    }
    else
    {
	vp_check_filep (pltout);
	vp_pltout = (FILE *) NULL;
    }

    return newout;
}


void vpplot (int x, int y, int draw)
/*< plot >*/
{
    vpsetflag = NO;

    if (draw)
	vp_draw ((float) x / RPERIN, (float) y / RPERIN);
    else
	vp_move ((float) x / RPERIN, (float) y / RPERIN);

    dev.lost = NO;
}

static float   *xp;
static float   *yp;
static int      vnpts;

void vpstartpoly (int npts)
/*< start polygon >*/
{
    vpsetflag = NO;
    dev.lost = YES;
    vnpts = 0;

    xp = (float *) malloc ((unsigned) (npts * sizeof (float)));
    yp = (float *) malloc ((unsigned) (npts * sizeof (float)));
}

void vpmidpoly (int x, int y)
/*< middle polygon >*/
{
    xp[vnpts] = (float) (x) / RPERIN;
    yp[vnpts] = (float) (y) / RPERIN;
    vnpts++;
}

void vpendpoly (int last)
/*< end polygon >*/
{
    if (ipat == 0)
    {
	vp_area (xp, yp, vnpts, -1, pat[ipat].xdim_orig, pat[ipat].ydim_orig);
    }
    else
    {

	if (ipat - 1 != vpcolor)
	    vp_color (ipat - 1);

	vp_fill (xp, yp, vnpts);

	if (ipat - 1 != vpcolor)
	    vp_color (vpcolor);

    }

    free ((char *) xp);
    free ((char *) yp);
}

void vpraster (int xpix, int ypix, int xmin, int ymin, int xmax, int ymax, 
	       unsigned char **raster_block, int orient, int dither_it)
/*< raster >*/
{
    vpsetflag = NO;
    dev.lost = YES;

    vp_raster (raster_block, (bool) (vpbit > 0), vpbit, 
	       xpix, ypix, 
	       (float) xmin / RPERIN, (float) ymin / RPERIN,
	       (float) xmax / RPERIN, (float) ymax / RPERIN, orient);
}

extern int      erase;

void vpreset (void)
/*<  Reset everything we can think of.
 * Ignore initial erases, and instead look at the command line
 * value of "erase" to decide whether to have an initial erase
 * or not. >*/
{

/*
 * vpsetflag is used to squeeze out redundant attribute-setting commands.
 */
    vpsetflag = NO;

    if (erase & FORCE_INITIAL)
	vp_erase ();

    if (!vpdumb && vpstyle)
    {
	vp_style (VP_ABSOLUTE);
    }

    if (!vpdumb)
    {
	dev.attributes (SET_WINDOW, dev.xmin, dev.ymin, dev.xmax, dev.ymax);
	dev.attributes (SET_COLOR, VP_WHITE, 0, 0, 0);
	dev.attributes (NEW_FAT, 0, 0, 0, 0);
	dev.attributes (NEW_DASH, 0, 0, 0, 0);
	dev.attributes (NEW_FONT, dev.txfont, dev.txprec, dev.txovly, 0);
	dev.attributes (NEW_ALIGN, txalign.hor, txalign.ver, 0, 0);
	dev.attributes (NEW_OVERLAY, overlay, 0, 0, 0);
    }
}

void vptext (char *string, float pathx, float pathy, float upx, float upy)
/*< text >*/
{
    void (*savevector)(int x1, int y1, int x2, int y2, int nfat, int vpdashon);
    void (*saveattributes)(int command, int value, int v1, int v2, int v3);
    void (*savearea)(int npts, struct vertex  *head);

    vpsetflag = NO;
    dev.lost = YES;

    if (*string == '\0')
	return;

    vp_gtext ((float) xold / RPERIN, (float) yold / RPERIN,
	      pathx / RPERIN, pathy / RPERIN,
	      upx / RPERIN, upy / RPERIN,
	      string);

/*
 *   Now reset the pen position to the end of the text.
 *   Do a dummy run through (if this indeed a gentext font)
 */
    if (dev.txfont < NUMGENFONT)
    {
	savevector = dev.vector;
	saveattributes = dev.attributes;
	savearea = dev.area;

/*
 *   Disconnect everything except error messages
 */
	dev.vector = nullvector;
	dev.attributes = nullattributes;
	dev.area = nullarea;

	gentext (string, pathx, pathy, upx, upy);

	dev.vector = savevector;
	dev.attributes = saveattributes;
	dev.area = savearea;

/*
 * Jon note that this shows you how to find the size of the text.
 */
	vp_move ((float) xold / RPERIN, (float) yold / RPERIN);
    }
}

#define MOVE 0
#define DRAW 1

void vpvector (int x1, int y1, int x2, int y2, int nfat, int vpdashon)
/*< vector >*/
{
    static int      xlst, ylst;
    int             d1, d2;

    if (nfat < 0)
	return;

    /*
     * Important special case: Zero-length vector at the end of what you've
     * already plotted. Don't need to do anything. 
     */
    if (x1 == x2 && y1 == y2 && !dev.lost && x1 == xlst && y1 == ylst)
    {
	return;
    }

/*
 * As stated in the documentation, dev.vector must be
 * ready to accept changes in fatness and linestyle without
 * warning at any time.
 */

    if (nfat != fat)
    {
	vp_fat (ROUND ((float) nfat * FATPERIN / RPERIN));
	dev.lost = YES;
    }

    if (vpdashon != dashon)
    {
	dev.attributes (NEW_DASH, vpdashon, 0, 0, 0);
    }

    /*
     * Minimize movement of "pen" Don't turn around dashed lines, since order
     * of drawing matters. 
     */
    if (!dev.lost && !vpdashon)
    {
	d1 = abs (x1 - xlst) + abs (y1 - ylst);
	d2 = abs (x2 - xlst) + abs (y2 - ylst);
	if (d2 < d1)
	{
	    d1 = x1;
	    d2 = y1;
	    x1 = x2;
	    y1 = y2;
	    x2 = d1;
	    y2 = d2;
	}
    }

    if ((x1 != xlst) || (y1 != ylst) || dev.lost)
    {
	/* Make sure it is a move, not a draw */
	dev.plot (x1, y1, MOVE);
    }
    dev.plot (x2, y2, DRAW);
    xlst = x2;
    ylst = y2;

/*
 * Restore fat and dash stuff if we changed it.
 */
    if (nfat != fat)
    {
	vp_fat (ROUND ((float) fat * FATPERIN / RPERIN));
	dev.lost = YES;
    }

    if (vpdashon != dashon)
    {
	dev.attributes (NEW_DASH, dashon, 0, 0, 0);
    }
/*
 * Above can be inefficient, but that's a rare case and it's hard
 * to get around. (Very hard.) This works!
 */
}

static void vp_check_filep (FILE *plot)
{
    if (isatty (fileno (plot)))
	ERR (FATAL, name,
	     "Dumping binary data to your terminal is unhealthy.");

    vp_filep (plot);
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
