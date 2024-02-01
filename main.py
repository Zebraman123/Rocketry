from rocketpy import Environment, SolidMotor, Rocket, Flight
import datetime

#Location, Elevation in meters
#tripolinorthtexas - seymour
env = Environment(
    latitude=33.501037, longitude=-99.338722, elevation=1289
)

#Year, Month, Day, Hour
tomorrow = datetime.date.today() + datetime.timedelta(days=1)

env.set_date(
    (tomorrow.year, tomorrow.month, tomorrow.day, 12)
)

#atmospheric data
env.set_atmospheric_model(type="Forecast", file="GFS")


env.max_expected_height = 1000
#shows enviromental information based on location and date
env.info()

#Thrustcurve.org M1850W Aerotech for etr

#in meters
#length = 0.9144
#radius = 0.04
#in kg
#mass = 1.119806

OneL = Rocket(
    mass = 1.119806,
    radius = 0.04,
    inertia = (0.078,0.078,0),
    coordinate_system_orientation = "nose_to_tail",
    center_of_mass_without_motor = 0.586867,
    power_off_drag ="/mnt/c/Users/zebra/Documents/Rocketry/CDLONE.txt",
    power_on_drag ="/mnt/c/Users/zebra/Documents/Rocketry/CDLONE.txt"
)

nose_cone = OneL.add_nose(length=0.3302, kind="elliptical", position=0)

fin_set = OneL.add_trapezoidal_fins(n=4,root_chord=0.135,tip_chord=0.089, span=0.066,position=-1,cant_angle=0.86)



 #   dry_inertia=(148/10000000, 148/10000000,0.000679),

#Motor 
H97 = SolidMotor(
    thrust_source="/mnt/c/Users/zebra/Documents/Rocketry/LONETHRUSTCURVE.csv",
    dry_mass=0.141,
    dry_inertia=(0, 0,0),
    nozzle_radius=29 / 1000,
    grain_number=4,
    grain_density=2085.96,
    grain_outer_radius=29 / 1000,
    grain_initial_inner_radius=15 / 1000,
    grain_initial_height=120 / 1000,
    grain_separation=0 / 1000,
    grains_center_of_mass_position=0.397,
    center_of_dry_mass_position=0.317,
    nozzle_position=0,
    burn_time=3.9,
    throat_radius=31 / 1000,
    coordinate_system_orientation="nozzle_to_combustion_chamber",
)

#OneL.draw()
OneL.info()