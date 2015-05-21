from sherpa.astro.ui import *
load_pha('pn_pi_src_bin10.ds')
load_arf('pn_pi_src.arf')
load_rmf('epn_ff20_sdY9.rmf')
set_stat('chi2xspecvar')
ignore(':2,9.95:')
set_model(xswabs.gal*xswabs.intrin*xspowerlaw.phard)
gal.nH= 0.0119
freeze(gal.nh)
fit()
