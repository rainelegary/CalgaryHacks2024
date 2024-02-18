# import_data.py

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TouchGrass.settings')
django.setup()


import csv
from TouchGrassApp.models import Facility  

def import_csv_data(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Create a new instance of Facility model for each row
            facility = Facility.objects.create(
                complex_name=row['COMPLEX_NAME'],
                facility_type=row['FACILITY_TYPE'],
                tier=row['TIER'],
                address=row['ADDRESS'],
                longitude=row['LONGITUDE'],
                latitude=row['LATITUDE'],
                org=row['ORG'],
                typ_of_org=row['TYP_OF_ORG'],
                steward=row['STEWARD'],
                oper=row['OPER'],
                label=row['LABEL'],
                website=row['WEBSITE'],
                phone=row['PHONE'],
                notes=row['NOTES'],
                gym=row['GYM'] == 'Y',  # Convert 'Y' to True, 'N' to False
                gymnast_fac=row['GYMNAST_FAC'] == 'Y',
                fitnss_wght=row['FITNSS_WGHT'] == 'Y',
                fit_studio=row['FIT_STUDIO'] == 'Y',
                multi_purp_rooms=row['MULTI_PURP_ROOMS'] == 'Y',
                meet_rooms=row['MEET_ROOMS'] == 'Y',
                indr_pool=row['INDR_POOL'] == 'Y',
                outdr_pool=row['OUTDR_POOL'] == 'Y',
                fw_25m=row['FW_25M'] == 'Y',
                fw_50m=row['FW_50M'] == 'Y',
                fw_18m=row['FW_18M'] == 'Y',
                lanes_pool=row['LANES_POOL'] == 'Y',
                teach_pool=row['TEACH_POOL'] == 'Y',
                wave_pool=row['WAVE_POOL'] == 'Y',
                other_pool=row['OTHER_POOL'] == 'Y',
                indr_wad_pool=row['INDR_WAD_POOL'] == 'Y',
                diving_tank=row['DIVING_TANK'] == 'Y',
                springboard=row['SPRINGBOARD'] == 'Y',
                platform=row['PLATFORM'] == 'Y',
                dive_slide=row['DIVE_SLIDE'] == 'Y',
                play_slide=row['PLAY_SLIDE'] == 'Y',
                rope_swing=row['ROPE_SWING'] == 'Y',
                steam=row['STEAM'] == 'Y',
                hot_tub=row['HOT_TUB'] == 'Y',
                sauna=row['SAUNA'] == 'Y',
                climb_wall=row['CLIMB_WALL'] == 'Y',
                track_indr=row['TRACK_INDR'] == 'Y',
                outdr_wad_pool=row['OUTDR_WAD_POOL'] == 'Y',
                spray_park=row['SPRAY_PARK'] == 'Y',
                ice_indr=row['ICE_INDR'] == 'Y',
                stand_ice=row['STAND_ICE'] == 'Y',
                nhl_ice=row['NHL_ICE'] == 'Y',
                olymp_ice=row['OLYMP_ICE'] == 'Y',
                fig_skating=row['FIG_SKATING'] == 'Y',
                curl_rnk=row['CURL_RNK'] == 'Y',
                curl_sheets=row['CURL_SHEETS'] == 'Y',
                indr_surface=row['INDR_SURFACE'] == 'Y',
                indr_turf=row['INDR_TURF'] == 'Y',
                dry_pad=row['DRY_PAD'] == 'Y',
                racqfac_indr=row['RACQFAC_INDR'] == 'Y',
                squash_crts=row['SQUASH_CRTS'] == 'Y',
                raqball_crts=row['RAQBALL_CRTS'] == 'Y',
                badmint_crts=row['BADMINT_CRTS'] == 'Y',
                tennis_crt=row['TENNIS_CRT'] == 'Y',
                outdr_field=row['OUTDR_FIELD'] == 'Y',
                artf_turf_outdr=row['ARTF_TURF_OUTDR'] == 'Y',
                diam_fac_outdr=row['DIAM_FAC_OUTDR'] == 'Y',
                track_outdr=row['TRACK_OUTDR'] == 'Y',
                public_glf=row['PUBLIC_GLF'] == 'Y',
                semi_priv_glf=row['SEMI_PRIV_GLF'] == 'Y',
                hole_18=row['HOLE_18'] == 'Y',
                hole_9=row['HOLE_9'] == 'Y',
                driverang_outdr=row['DRIVERANG_OUTDR'] == 'Y',
                driverang_indr=row['DRIVERANG_INDR'] == 'Y',
                ski_nordictrck=row['SKI_NORDICTRCK'] == 'Y',
                municpal_op=row['MUNICPAL_OP'] == 'Y',
                notprofit_op=row['NOTPROFIT_OP'] == 'Y',
                profit_op=row['PROFIT_OP'] == 'Y',
                private_op=row['PRIVATE_OP'] == 'Y'
            )

if __name__ == "__main__":
    csv_file_path = 'Recreation_Facilities_Long_Lat.csv'  # Provide the path to your CSV file
    import_csv_data(csv_file_path)
