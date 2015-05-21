from sherpa.astro.ui import *

load_pha("bubble.pi")
set_stat("cstat")
#set_method("neldermead")
notice(0.3,7)

set_model(xsphabs.abs1*xsmekal.mek1)
mek1.norm = 4e-6
#mek1.kt = 18
abs1.nh=0.056
freeze(abs1)
fit()
proj()
covar()
