from django.db import models

class Facility(models.Model):
    complex_name = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=100)
    tier = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    longitude = models.DecimalField(max_digits=25, decimal_places=20)  # Adjust precision as needed
    latitude = models.DecimalField(max_digits=25, decimal_places=20)  # Adjust precision as needed
    org = models.CharField(max_length=100)
    typ_of_org = models.CharField(max_length=100)
    steward = models.CharField(max_length=100)
    oper = models.CharField(max_length=100)
    label = models.CharField(max_length=255)
    website = models.URLField()
    phone = models.CharField(max_length=20)
    notes = models.TextField()
    gym = models.BooleanField(default=False)
    gymnast_fac = models.BooleanField(default=False)
    fitnss_wght = models.BooleanField(default=False)
    fit_studio = models.BooleanField(default=False)
    multi_purp_rooms = models.BooleanField(default=False)
    meet_rooms = models.BooleanField(default=False)
    indr_pool = models.BooleanField(default=False)
    outdr_pool = models.BooleanField(default=False)
    fw_25m = models.BooleanField(default=False)
    fw_50m = models.BooleanField(default=False)
    fw_18m = models.BooleanField(default=False)
    lanes_pool = models.BooleanField(default=False)
    teach_pool = models.BooleanField(default=False)
    wave_pool = models.BooleanField(default=False)
    other_pool = models.BooleanField(default=False)
    indr_wad_pool = models.BooleanField(default=False)
    diving_tank = models.BooleanField(default=False)
    springboard = models.BooleanField(default=False)
    platform = models.BooleanField(default=False)
    dive_slide = models.BooleanField(default=False)
    play_slide = models.BooleanField(default=False)
    rope_swing = models.BooleanField(default=False)
    steam = models.BooleanField(default=False)
    hot_tub = models.BooleanField(default=False)
    sauna = models.BooleanField(default=False)
    climb_wall = models.BooleanField(default=False)
    track_indr = models.BooleanField(default=False)
    outdr_wad_pool = models.BooleanField(default=False)
    spray_park = models.BooleanField(default=False)
    ice_indr = models.BooleanField(default=False)
    stand_ice = models.BooleanField(default=False)
    nhl_ice = models.BooleanField(default=False)
    olymp_ice = models.BooleanField(default=False)
    fig_skating = models.BooleanField(default=False)
    curl_rnk = models.BooleanField(default=False)
    curl_sheets = models.BooleanField(default=False)
    indr_surface = models.BooleanField(default=False)
    indr_turf = models.BooleanField(default=False)
    dry_pad = models.BooleanField(default=False)
    racqfac_indr = models.BooleanField(default=False)
    squash_crts = models.BooleanField(default=False)
    raqball_crts = models.BooleanField(default=False)
    badmint_crts = models.BooleanField(default=False)
    tennis_crt = models.BooleanField(default=False)
    outdr_field = models.BooleanField(default=False)
    artf_turf_outdr = models.BooleanField(default=False)
    diam_fac_outdr = models.BooleanField(default=False)
    track_outdr = models.BooleanField(default=False)
    public_glf = models.BooleanField(default=False)
    semi_priv_glf = models.BooleanField(default=False)
    hole_18 = models.BooleanField(default=False)
    hole_9 = models.BooleanField(default=False)
    driverang_outdr = models.BooleanField(default=False)
    driverang_indr = models.BooleanField(default=False)
    ski_nordictrck = models.BooleanField(default=False)
    municpal_op = models.BooleanField(default=False)
    notprofit_op = models.BooleanField(default=False)
    profit_op = models.BooleanField(default=False)
    private_op = models.BooleanField(default=False)

class Activity(models.Model):
    name = models.CharField(max_length=255)
    facilities = models.ManyToManyField(Facility, related_name='activities')

    def __str__(self):
        return self.name