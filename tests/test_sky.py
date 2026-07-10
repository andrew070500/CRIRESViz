from criresviz.models import Sky



sky = Sky.from_file("../resources/generated/sky/output.fits")
print(sky)

#sky = Sky.from_skycalc(wmin=3500, airmass=2)
#print(sky)

print(sky.available_parameters)
print(sky.get_parameter("therm_t1"))
print(sky.get_parameter("therm_t1", "wdelta"))

