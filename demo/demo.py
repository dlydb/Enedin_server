import pandas as pd
import time

data = pd.read_csv('data.csv')

while True:
	input("Press a button to start your energy estimation")

	year = int(input("When is your building built (1900 - 2010) "))
	if year < 1920:
		year = 1920
	year = int(year/20) * 20

	nump = int(input("How many people are living there "))
	if nump % 2 == 0:
		nump -= 1
		num_r = 1
	if nump > 6:
		nump = 5
		num_r = nump/6
	else:
		num_r = 1

	flr = int(input("What is the floor area (square feet)  "))
	if flr < 800:
		flr = 800
		flr_r = 1
	elif flr > 3600:
		flr = 3600
		flr_r = flr/4000
	else:
		flr_r = 1
	flr = int(flr / 400) * 400


	st = int(input("How many stories are there  "))
	if st > 3:
		st_r = st / 3
	else:
		st_r = 1


	r = data[(data['year'] == year) & (data['nump'] == nump) & (data['flr'] == flr) & (data['story'] == st)].to_dict('records')[0]
	print(data[(data['year'] == year)].iloc[0]['nump'])

	pay = 12 * float(input("How much did you pay last month $  "))


	ratio = pay / (int(r['house_bill_exist'].replace(',', '')) * num_r * flr_r * st_r)

	time.sleep(1)
	print("\n\nYour approximate payment for a year is $%.2f"%pay)
	print("You can save your home with $%.2f"%((int(r['house_bill_exist'].replace(',','')) - int(r['house_bill_upgrade'].replace(',',''))) * ratio))
	print("You can save %.2f kWh in Electricity"%((int(r['house_elec_exist'].replace(',','')) - int(r['house_elec_upgrade'].replace(',',''))) * ratio))
	print("You can save %.2f Therms in Natural Gas"%((int(r['house_gas_exist'].replace(',','')) - int(r['house_gas_upgrade'].replace(',',''))) * ratio))
	print("You can save %.2f lb. CO2 emissions"%((int(r['house_ems_upgrade'].replace(',','')) - int(r['house_ems_exist'].replace(',',''))) * ratio))

	print("\nYour estimated added_cost is $%.2f"%(int(r['added_cost'].replace(',','')) * ratio))
	print("Your estimated ROI is " + r['estimated_roi'])

	print("\n\nHere is your detailed recommendations:")

	print("\tReplace your therostat: save $%.2f"%(int(r['thermostat_sav'])))
	print("\tReplace the incandescent lights: save $%.2f"%(int(r['lighting_sav'])))
	print("\tReplace your washer: save $%.2f"%(int(r['clotheswasher_sav'])))
	print("\tReplace your water heater: save $%.2f"%(int(r['waterheater_sav'])))
	print("\tHave a professional seal your ducts to reduce leakage: save $%.2f"%(int(r['ductseal_sav'])))
	print("\tReplace your water heater: save $%.2f"%(int(r['clothesdryer_sav'])))
	print("\tReplace your wall insulation: save $%.2f"%(int(r['wall_sav'])))
	print("\tReplace your air sealing: save $%.2f"%(int(r['infiltration_sav'])))




	print('\n\n\n\n\n')