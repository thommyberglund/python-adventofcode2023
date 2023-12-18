class mapClass:
    def __init__(self,destination,source,range):
        self.destination = destination
        self.source = source
        self.range = range

    def __str__(self):
        return f"Destination: {self.destination} {type(self.destination)}, Source: {self.source}, Range: {self.range}"

def loadMap(line, input_map):
    current_line = line.split()
    if(len(current_line)) != 3:
        return
    input_map.append(mapClass(int(current_line[0]),int(current_line[1]),int(current_line[2])))



seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
map_holder = []
row_index = 0
file = open('input.txt', 'r')
lines = file.read().splitlines()
seeds = []
#for index, line in enumerate(lines):
#    if line == "seed-to-soil map:":
#        row_index = index + 1
#        break
#while 
#print(seeds)

map_holder.append(seed_to_soil)
map_holder.append(soil_to_fertilizer)
map_holder.append(fertilizer_to_water)
map_holder.append(water_to_light)
map_holder.append(light_to_temperature)
map_holder.append(temperature_to_humidity)
map_holder.append(humidity_to_location)

for line in lines:
    if len(line.strip()) == 0:
       row_index += 1
       continue
    match row_index:
        case 0:
            line_list = lines[0].lstrip("seeds:").split()
            for line in line_list:
                seeds.append(int(line))
        case 1:
            loadMap(line, seed_to_soil);
        case 2:
            loadMap(line, soil_to_fertilizer);
        case 3:
            loadMap(line, fertilizer_to_water);
        case 4:
            loadMap(line, water_to_light);
        case 5:
            loadMap(line, light_to_temperature);
        case 6:
            loadMap(line, temperature_to_humidity);
        case 7:
            loadMap(line, humidity_to_location);
            
            
loc = []
for seed in seeds:
    dest = seed
    for map in map_holder:
        for item in map:
            if dest >= item.source and dest < (item.source + item.range):
                dest = dest - item.source + item.range
                break
    loc.append(dest)
print(loc)
solution = []
for i in loc:
    if i in seeds:
        print(i)
        solution.append(i)
