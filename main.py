from rocketpy import Environment, SolidMotor, Rocket, Flight
import datetime

#Location, Elevation in meters
#tripolinorthtexas - seymour
env = Environment(
    latitude=33.501037, longitude=-99.338722, elevation=1289
)

#Year, Month, Day, Hour
env.set_date(
    (2023, 11, 18, 12)
)

#atmospheric data
env.set_atmospheric_model(type="Forecast", file="GFS")

#Expected Apogee of rocket
env.max_expected_height = 1000

#shows enviromental information based on location and date
env.info()

#Thrustcurve.org M1850W Aerotech for etr

#in meters
#length = 0.9144
#radius = 0.04
#in kg
#mass = 1.119806

#Rocket Body
OneL = Rocket(
    mass = 1.119806,
    radius = 0.04,
    inertia = (0.078,0.078,0),
    coordinate_system_orientation = "nose_to_tail",
    center_of_mass_without_motor = 0.586867,
    power_off_drag ="/mnt/c/Users/zebra/Documents/Rocketry/CDLONE.txt",
    power_on_drag ="/mnt/c/Users/zebra/Documents/Rocketry/CDLONE.txt"
)

#nose
nose_cone = OneL.add_nose(length=0.3302, kind="elliptical", position=0)

#Fin
fin_set = OneL.add_trapezoidal_fins(n=4,root_chord=0.135,tip_chord=0.089, span=0.066,position=-1,cant_angle=0.86)

#Motor 
H97 = SolidMotor(
    thrust_source="/mnt/c/Users/zebra/Documents/Rocketry/LONETHRUSTCURVE.csv",
    dry_mass=0.145, #0.282-0.137 from apogeerockets
    dry_inertia=(0, 0,0), #good
    nozzle_radius=29 / 1000,
    grain_number=4, #good
    grain_density=2085.96, #good
    grain_outer_radius=11.85 / 1000, #OD is 0.933in based on number 8 from the motor assembly
    grain_initial_inner_radius=0.50395 / 1000, #based off meeting notes, no idea where this came from
    grain_initial_height=44.45 / 1000, #Part number 8 length
    grain_separation=0 / 1000, #Picture shows no sep
    grains_center_of_mass_position=0.397, 
    center_of_dry_mass_position=0.317,
    nozzle_position=0,
    burn_time=2.2,#from apogeerockets
    throat_radius=7.93 / 1000, #good
    coordinate_system_orientation="nozzle_to_combustion_chamber",
)

#OneL.draw()
OneL.info()