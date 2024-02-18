# management/commands/sort_facilities.py

from django.core.management.base import BaseCommand
from TouchGrassApp.models import Facility, Activity

class Command(BaseCommand):
    help = 'Sort facilities into relevant activities based on Boolean attributes and notes'

    def handle(self, *args, **options):
        # Define your logic to sort facilities into activities
        facilities = Facility.objects.all()
        for facility in facilities:
            activities = []

            if facility.gym:
                activities.append('Gym')
            if facility.gymnast_fac:
                activities.append('Gymnastics')
            if facility.fitnss_wght:
                activities.append('Weightlifting')
            if facility.fit_studio:
                activities.append('Fitness Studio')
            if facility.multi_purp_rooms:
                activities.append('Multi-purpose Rooms')
            if facility.meet_rooms:
                activities.append('Meeting Rooms')
            if facility.indr_pool:
                activities.append('Indoor Swimming')
            if facility.outdr_pool:
                activities.append('Outdoor Swimming')
            if facility.fw_25m or facility.fw_50m or facility.fw_18m:
                activities.append('Water Sports')
            if facility.lanes_pool:
                activities.append('Pool Lanes')
            if facility.teach_pool:
                activities.append('Teaching Pool')
            if facility.wave_pool:
                activities.append('Wave Pool')
            if facility.other_pool:
                activities.append('Other Pool')
            if facility.indr_wad_pool:
                activities.append('Indoor Wading Pool')
            if facility.diving_tank:
                activities.append('Diving Tank')
            if facility.springboard:
                activities.append('Springboard Diving')
            if facility.platform:
                activities.append('Platform Diving')
            if facility.dive_slide:
                activities.append('Dive Slide')
            if facility.play_slide:
                activities.append('Play Slide')
            if facility.rope_swing:
                activities.append('Rope Swing')
            if facility.steam:
                activities.append('Steam Room')
            if facility.hot_tub:
                activities.append('Hot Tub')
            if facility.sauna:
                activities.append('Sauna')
            if facility.climb_wall:
                activities.append('Climbing Wall')
            if facility.track_indr:
                activities.append('Indoor Track')
            if facility.outdr_wad_pool:
                activities.append('Outdoor Wading Pool')
            if facility.spray_park:
                activities.append('Spray Park')
            if facility.ice_indr or facility.stand_ice or facility.nhl_ice or facility.olymp_ice or facility.fig_skating:
                activities.append('Ice Skating')
            if facility.curl_rnk or facility.curl_sheets:
                activities.append('Curling')
            if facility.indr_surface or facility.indr_turf or facility.dry_pad:
                activities.append('Indoor Sports')
            if facility.racqfac_indr:
                activities.append('Indoor Racquetball')
            if facility.squash_crts:
                activities.append('Squash Courts')
            if facility.raqball_crts:
                activities.append('Racquetball Courts')
            if facility.badmint_crts:
                activities.append('Badminton Courts')
            if facility.tennis_crt:
                activities.append('Tennis')
            if facility.outdr_field:
                activities.append('Outdoor Field')
            if facility.artf_turf_outdr:
                activities.append('Artificial Turf Field')
            if facility.diam_fac_outdr:
                activities.append('Diamond Facility')
            if facility.track_outdr:
                activities.append('Outdoor Track')
            if facility.public_glf or facility.semi_priv_glf:
                activities.append('Golf')
            if facility.hole_18 or facility.hole_9:
                activities.append('Golf Course')
            if facility.driverang_outdr or facility.driverang_indr:
                activities.append('Driving Range')
            if facility.ski_nordictrck:
                activities.append('Nordic Skiing')


            for activity_name in activities:
                activity, created = Activity.objects.get_or_create(name=activity_name)
                facility.activities.add(activity)