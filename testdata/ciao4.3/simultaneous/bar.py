from sherpa.astro.ui import *

load_pha(1, "pi2278.fits")
load_arf(1, "arf2278.fits")
load_rmf(1, "rmf2278.fits")

load_pha(2, "pi2286.fits")
load_arf(2, "arf2286.fits")
load_rmf(2, "rmf2286.fits")

rsp1 = get_response(1)
rsp2 = get_response(2)

set_stat('cash')
set_method('neldermead')

set_model(1, rsp1(xswabs.abs1 * powlaw1d.pl1) + \
              rsp2(abs1*powlaw1d.pl2)*scale1d.s1)
set_model(2, rsp2(abs1*pl2) + rsp1(abs1*pl1)*scale1d.s2)

#pl2.gamma = pl1.gamma

fit()
