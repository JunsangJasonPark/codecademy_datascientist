# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def convert_damage(data):
  new_data = []
  for item in data:
    if "M" in item:
      temp = float(item.strip("M")) * conversion['M']
      new_data.append(int(temp))
    elif "B" in item:
      temp = float(item.strip("B")) * conversion['B']
      new_data.append(int(temp))
    elif item =='Damages not recorded':
      new_data.append(item)
  return new_data
# test function by updating damages
#print(convert_damage(damages))

# 2 
# Create a Table
args = names, months, years, max_sustained_winds, areas_affected, convert_damage(damages), deaths
def create_table(name, month, year, max_wind, areas, damage, death):
  table = {}
  for i in range(len(name)):
    table[name[i]] = {
      "Name": name[i],
      "Month": month[i],
      'Year': year[i],
      'Max Sustained Wind': max_wind[i],
      'Areas Affected': areas[i],
      'Damage': damage[i],
      'Deaths': death[i]}
  return table
table = create_table(*args)
# Create and view the hurricanes dictionary

# 3
# Organizing by Year
def org_year(table):
  new_table = {}
  for key, value in table.items():
    if value['Year'] not in new_table:
      new_table[value['Year']] = [value]
    else:
      new_table[value['Year']].append(value)
  return new_table
# create a new dictionary of hurricanes with year and key
by_year_table = org_year(table)
# print(by_year_table)

# 4
# Counting Damaged Areas
def area_count(areas_affected):
  area_count = {}
  for areas in areas_affected:
    for area in areas:
      if area not in area_count:
        area_count[area] = 1
      elif area in area_count:
        area_count[area] += 1
  return area_count
# create dictionary of areas to store the number of hurricanes involved in
#print(area_count(areas_affected))

# 5 
# Calculating Maximum Hurricane Count
def most_affected(area_count):
  temp_key = ''
  temp_value = 0
  for key, value in area_count.items():
    if temp_value == 0:
      temp_key = key
      temp_value = value
    elif temp_value != 0:
        if temp_value > value:
          continue
        else:
          temp_key = key
          temp_value = value
  return temp_key, temp_value
# find most frequently affected area and the number of hurricanes involved in
#print(most_affected(area_count(areas_affected)))

# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(table):
  temp_name = ''
  death = 0
  for name, info in table.items():
    if info['Deaths'] == 0:
      temp_name = name
      death = info['Deaths']
    else:
      if death > info['Deaths']:
        continue
      else:
        temp_name = name
        death = info['Deaths']
  return temp_name, death

# find highest mortality hurricane and the number of deaths
#print(deadliest_hurricane(table))

# 7
# Rating Hurricanes by Mortality
def rate_mortality(table):
  for item in table:
    if table[item]['Deaths'] > 10000:
      table[item]['Mortality'] = 5
    elif table[item]['Deaths'] > 1000:
      table[item]['Mortality'] = 4
    elif table[item]['Deaths'] > 500:
      table[item]['Mortality'] = 3
    elif table[item]['Deaths'] > 100:
      table[item]['Mortality'] = 2
    elif table[item]['Deaths'] > 0:
      table[item]['Mortality'] = 1
    else:
      table[item]['Mortality'] = 0
  return table

# categorize hurricanes in new dictionary with mortality severity as key
mortality_table = rate_mortality(table)

# 8 Calculating Hurricane Maximum Damage
def greatest_damage(table):
  return_key = ''
  return_value = 0
  for key, value in table.items():
    if isinstance(value['Damage'], int):
      if value['Damage'] > return_value:
        return_value = value['Damage']
        return_key = key
      else:
        continue
    else:
      continue
  return return_key, return_value

print(greatest_damage(table))



# find highest damage inducing hurricane and its total cost

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
def rate_by_damage(table):
  result = {4: [], 3: [], 2: [], 1: [], "Unknown": []}
  for key, value in table.items():
    if isinstance(value['Damage'], int):
      if value['Damage'] > damage_scale[4]:
        result[4].append(key)
      elif value['Damage'] > damage_scale[3]:
        result[3].append(key)
      elif value['Damage'] > damage_scale[2]:
        result[2].append(key)
      elif value['Damage'] > damage_scale[1]:
        result[1].append(key)
    else:
      result["Unknown"].append(key)
  return result

print(rate_by_damage(table))



# categorize hurricanes in new dictionary with damage severity as key
