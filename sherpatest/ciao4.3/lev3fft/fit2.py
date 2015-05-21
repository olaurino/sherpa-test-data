#!/usr/bin/env python
from sherpa.astro.ui import *
import time

def setup(srcid, image_file, psf_file, reg_file,
          mysrc="gauss2d", mybkg="const2d"):
    
    load_data(srcid, image_file)
    load_psf("psf%i" % srcid, psf_file)
    set_psf(srcid, "psf%i" % srcid)

    set_coord(srcid, "physical")
    notice2d_id(srcid, "region(" + reg_file + "[SRCREG])")

    # Switch to WCS for fitting
    set_coord(srcid, "wcs")

    # Use Nelder-Mead, C-statistic as fit method, statistic
    set_method("neldermead")
    set_stat("cstat")

    set_source(srcid, '%s.src + %s.bkg' % (mysrc, mybkg))
    guess(srcid, src)


if __name__ == '__main__':

    ifile1 = "acisf07999_000N001_r0035_regevt3_srcimg.fits"
    pfile1 = "acisf07999_000N001_r0035b_psf3.fits"
    rfile1 = "acisf07999_000N001_r0035_reg3.fits"

    ifile2 = "acisf08478_000N001_r0043_regevt3_srcimg.fits"
    pfile2 = "acisf08478_000N001_r0043b_psf3.fits"
    rfile2 = "acisf08478_000N001_r0043_reg3.fits"

    setup(1, ifile1, pfile1, rfile1)
    setup(2, ifile2, pfile2, rfile2)

    #psf2.origin = (158,156)

    tt = time.time()
    fit()
    print 'fit in %g secs' % (time.time()-tt)
