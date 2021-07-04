# Wind speed conversions and the beaufort scale - www.101computing.net/wind-force/

forces = {0: ["Calm","Sea like a mirror","Smoke rises vertically"],
          1: ["Light air","Ripples with appearance of scales are formed, without foam crests","Direction shown by smoke drift but not by wind vanes."],
          2: ["Light breeze","Small wavelets still short but more pronounced; crests have a glassy appearance but do not break","Wind felt on face; leaves rustle; wind vane moved by wind."],
          3: ["Gentle breeze","Large wavelets; crests begin to break; foam of glassy appearance; perhaps scattered white horses","Leaves and small twigs in constant motion; light flags extended."],
          4: ["Moderate breeze","Small waves becoming longer; fairly frequent white horses","Raises dust and loose paper; small branches moved."],
          5: ["Fresh breeze","Moderate waves taking a more pronounced long form; many white horses are formed; chance of some spray","Small trees in leaf begin to sway; crested wavelets form on inland waters."],
          6: ["Strong breeze","Large waves begin to form; the white foam crests are more extensive everywhere; probably some spray","Large branches in motion; whistling heard in telegraph wires; umbrellas used with difficulty."],
          7: ["High wind, moderate gale, near gale","Sea heaps up and white foam from breaking waves begins to be blown in streaks along the direction of the wind; spindrift begins to be seen","Whole trees in motion; inconvenience felt when walking against the wind."],
          8: ["Gale, fresh gale","Moderately high waves of greater length; edges of crests break into spindrift; foam is blown in well-marked streaks along the direction of the wind","Twigs break off trees; generally impedes progress."],
          9: ["Strong/severe gale","High waves; dense streaks of foam along the direction of the wind; sea begins to roll; spray affects visibility","Slight structural damage (chimney pots and slates removed)."],
          10: ["Storm, whole gale","Very high waves with long overhanging crests; resulting foam in great patches is blown in dense white streaks along the direction of the wind; on the whole the surface of the sea takes on a white appearance; rolling of the sea becomes heavy; visibility affected","Seldom experienced inland; trees uprooted; considerable structural damage."],
          11: ["Violent storm","Exceptionally high waves; small- and medium-sized ships might be for a long time lost to view behind the waves; sea is covered with long white patches of foam; everywhere the edges of the wave crests are blown into foam; visibility affected","Very rarely experienced; accompanied by widespread damage."],
          12: ["Hurricane force","The air is filled with foam and spray; sea is completely white with driving spray; visibility very seriously affected","Devastation"]
          }

speed = float(input("Enter the speed of the wind in knots: "))
kt = 1.852 * speed

# Step 1: Convert this speed in knots knowing that 1 knot = 1.852 km/h
if speed < 1:
    print("Force", list(forces.keys())[0])
    for i in forces[0]:
        print(i)

elif speed <= 3:
    print("Force", list(forces.keys())[1])
    for i in forces[1]:
        print(i)

elif speed <= 6:
    print("Force", list(forces.keys())[2])
    for i in forces[2]:
        print(i)

elif speed <= 10:
    print("Force", list(forces.keys())[3])
    for i in forces[3]:
        print(i)

elif speed <= 16:
    print("Force", list(forces.keys())[4])
    for i in forces[4]:
        print(i)

elif speed <= 21:
    print("Force", list(forces.keys())[5])
    for i in forces[5]:
        print(i)

elif speed <= 27:
    print("Force", list(forces.keys())[6])
    for i in forces[6]:
        print(i)

elif speed <= 33:
    print("Force", list(forces.keys())[7])
    for i in forces[7]:
        print(i)

elif speed <= 40:
    print("Force", list(forces.keys())[8])
    for i in forces[8]:
        print(i)

elif speed <= 47:
    print("Force", list(forces.keys())[9])
    for i in forces[9]:
        print(i)

elif speed <= 55:
    print("Force", list(forces.keys())[10])
    for i in forces[10]:
        print(i)

elif speed <= 63:
    print("Force", list(forces.keys())[11])
    for i in forces[11]:
        print(i)

elif speed >= 64:
    print("Force", list(forces.keys())[12])
    for i in forces[12]:
        print(i)


# Step 2: Use the Beaufort scale to work out the matching wind force


# Step 3: Display the wind force, description, sea conditions and land conditions corresponding to this wind force


# Step 4: Review the code in step 1 to allow the user to enter the wind speed in the unit of their choice (km/h, mph, knots)
