from acis_bkg_model import acis_bkg_model

load_pha(1,'obs1.pi')
load_pha(2,'obs2.pi')
load_pha(3,'obs3.pi')
load_pha(4,'obs4.pi')

load_bkg_rmf(1, 'obs1.rmf')
load_bkg_rmf(2, 'obs2.rmf')
load_bkg_rmf(3, 'obs3.rmf')
load_bkg_rmf(4, 'obs4.rmf')

load_bkg_arf(1, 'obs1.arf')
load_bkg_arf(2, 'obs2.arf')
load_bkg_arf(3, 'obs3.arf')
load_bkg_arf(4, 'obs4.arf')

# background for the 1 data set

bkg_arf_1 = get_bkg_arf(1)
bkg_rmf_1= get_bkg_rmf(1)
# scaling factor
bkg_scale_1 = get_data(1).sum_background_data(lambda x,y: 1)

rsp_1 = get_response(1)

bkg_model_1 = const1d.c1 * acis_bkg_model('acis7s')
set_full_model(1,rsp_1(xsphabs.abs1*powlaw1d.pow1) + bkg_scale_1 * bkg_rmf_1(bkg_model_1))
set_bkg_full_model(1,bkg_rmf_1(bkg_model_1))

# background for the 2 data set

bkg_arf_2 = get_bkg_arf(2)
bkg_rmf_2= get_bkg_rmf(2)
bkg_scale_2 = get_data(2).sum_background_data(lambda x,y: 1)

rsp_2 = get_response(2)

bkg_model_2= const1d.c2 * acis_bkg_model('acis7s')
set_full_model(2,rsp_2(abs1*pow1) + bkg_scale_2 * bkg_rmf_2(bkg_model_2))
set_bkg_full_model(2,bkg_rmf_2(bkg_model_2))

# background for the 3 data set

bkg_arf_3 = get_bkg_arf(3)
bkg_rmf_3= get_bkg_rmf(3)
bkg_scale_3 = get_data(3).sum_background_data(lambda x,y: 1)

rsp_3 = get_response(3)

bkg_model_3 = const1d.c3 * acis_bkg_model('acis7s')
set_full_model(3,rsp_3(abs1*pow1) + bkg_scale_3 * bkg_rmf_3(bkg_model_3))
set_bkg_full_model(3,bkg_rmf_3(bkg_model_3))

# background for the 4 data set

bkg_arf_4 = get_bkg_arf(4)
bkg_rmf_4= get_bkg_rmf(4)
bkg_scale_4 = get_data(4).sum_background_data(lambda x,y: 1)
rsp_4 = get_response(4)

bkg_model_4 = const1d.c4 * acis_bkg_model('acis7s')
set_full_model(4,rsp_4(abs1*pow1) + bkg_scale_4 * bkg_rmf_4(bkg_model_4))
set_bkg_full_model(4,bkg_rmf_4(bkg_model_4))


# Fitting and confidence

set_method("levmar")
set_stat("cstat")

fit_bkg()

freeze(c1.c0)
freeze(c2.c0)
freeze(c3.c0)
freeze(c4.c0)

ignore(None,0.5)
ignore(7.,None)

#get_bkg(1).notice()
#get_bkg(2).notice()
#get_bkg(3).notice()
#get_bkg(4).notice()

set_par(abs1.nh,0.0223)
freeze(abs1)
fit()
set_method("neldermead")
fit()

set_conf_opt("max_rstat",20)
    
#conf()
#get_conf_results()

# Printing results

print get_fit_results()
print get_conf_results()

set_conf_opt("sigma",1.6)
conf()

print "source counts_1", calc_data_sum(0.5,7.,1)
print "bkg_counts_1", calc_data_sum(0.5,7.,1,bkg_id=1)
print "source counts_2", calc_data_sum(0.5,7.,2)
print "bkg_counts_2", calc_data_sum(0.5,7.,2,bkg_id=1)
print "source counts_3", calc_data_sum(0.5,7.,3)
print "bkg_counts_3", calc_data_sum(0.5,7.,3,bkg_id=1)
print "source counts_4", calc_data_sum(0.5,7.,4)
print "bkg_counts_4", calc_data_sum(0.5,7.,4,bkg_id=1)

set_model(abs1*pow1)
print "absorbed flux 0.5-2keV",calc_energy_flux(0.5,2.)
print "absorbed flux 2-10 keV", calc_energy_flux(2.,10.)

set_model(pow1)
print "unabsorbed flux 0.5-2keV",calc_energy_flux(0.5,2.)
print "unabsorbed flux 2-10 keV", calc_energy_flux(2.,10.)

exit()



group_counts(10,bkg_id=1)
plot_bkg_fit()
plot_bkg()
ungroup(bkg_id=1)
plot_bkg()
get_bkg().notice(0.5,7.)
plot_bkg()
plot_bkg_fit()
group_counts(5)
group_counts(5,bkg_id=1)
plot_bkg_fit()
ungroup(bkg_id=1)
get_bkg().notice(0.5,7.)
plot_bkg_fit()
ungroup()
plot_bkg_fit()
thaw(bkg_pow1.gamma)
thaw(bkg_pow2.gamma)
fit_bkg()
plot_bkg_fit()
log_scale()
group_counts(5,bkg_id=1)
plot_bkg_fit()
ungroup(bkg_id=1)
plot_bkg_fit()
get_bkg().notice(0.5,7.)
plot_bkg_fit()
set_par(abs1.nh,0.0223)
freeze(abs1)
fit()
