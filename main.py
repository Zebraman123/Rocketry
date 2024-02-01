from rocketpy import Environment, SolidMotor, Rocket, Flight, Function
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-dark-palette")
import numpy as np
from scipy.signal import savgol_filter
#Location, Elevation in meters
#tripolinorthtexas - seymour
env = Environment(
    latitude=33.501037, longitude=-99.338722, elevation=1289
)

#Year, Month, Day, Hour
env.set_date(
    (2023, 11, 18, 12)
)
#range has to be number of years desired + 1
startyear = [2023]
for x in range(21): 
    if x == 0:
        continue
    startyear.append(startyear[0]-x)
#for x in startyear:print(x)

#atmospheric data
#env.set_atmospheric_model(type="Forecast", file="GFS")

#Expected Apogee of rocket
env.max_expected_height = 2289

#shows enviromental information based on location and date
#env.info()

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

#Parachute
Main = OneL.add_parachute(
    "Main",
    cd_s = 2.1,
    trigger = "apogee"
)

#Motor 
H97 = SolidMotor(
    thrust_source="/mnt/c/Users/zebra/Documents/Rocketry/LONETHRUSTCURVE.csv",
    dry_mass=0.145, #0.282-0.137 from apogeerockets
    dry_inertia=(39.43/1000, 39.43/1000,0.01/1000), #too small for 
    nozzle_radius=3.98 / 1000,#based on part 3
    grain_number=4, #based on picture
    grain_density=2085.96, #based on calculations from meeting notes
    grain_outer_radius=11.85 / 1000, #OD is 0.933in based on number 8 from the motor assembly
    grain_initial_inner_radius=0.50395 / 1000, #based off meeting notes, no idea where this came from
    grain_initial_height=44.45 / 1000, #Part number 8 length
    grain_separation=0 / 1000, #Picture shows no sep
    grains_center_of_mass_position=451.6 / 1000, #for now both com just halfway through motor
    center_of_dry_mass_position=451.6 / 1000,
    nozzle_position=0,
    burn_time=1.6,#from thrustcurve.csv
    throat_radius=7.93 / 1000, #based on calculations from meeting notes
    coordinate_system_orientation="nozzle_to_combustion_chamber",
)

OneL.add_motor(H97, 1.003)

OneL.plots.draw()
OneL.info()
H97.plots.draw()

test_flight = Flight(
    rocket=OneL, environment=env,rail_length = 5,inclination = 90,heading =0
)
#test_flight.all_info()
#you have to remove the parachute at the end so you dont have multiple parachutes?
OneL.parachutes.remove(Main)