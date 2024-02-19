import csv
import math

def csv_to_arrays(csv_file, has_header=True):
    columns = {}  # Dictionary to hold lists for each column
    errors = []  # List to hold any errors that occur during processing
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            if has_header:
                next(csv_reader)  # Skip the header row
            for row in csv_reader:
                for i, value in enumerate(row):
                    if i not in columns:
                        columns[i] = []
                    try:
                        columns[i].append(float(value))
                    except ValueError:
                        errors.append(f"Skipping non-numeric value: {value}")
    except FileNotFoundError:
        print(f"File not found: {csv_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return tuple(columns.values())

def point_distance(x1, y1, x2, y2):
    # Calculate the distance between two points
    # Returns the distance between the two points
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_absoluteAngles(Prox_X, Prox_Y, Dist_X, Dist_Y):
    # Calculate the absolute angle between two points
    # Prox: proximal point
    # Dist: distal point
    # Returns the absolute angle in degrees
    y_calc = Prox_Y - Dist_Y
    x_calc = Prox_X - Dist_X
    try:
        #angle = math.degrees(math.atan2((Prox_Y - Dist_Y), (Prox_X - Dist_X))) # Corrects the angle to the correct quadrant, but it will be done manually
        angle = math.degrees(math.atan(y_calc / x_calc))
    except Exception as e:
        angle = 0
        print(f"An error occurred: {str(e)}")
    
    # Correct the angle to the correct quadrant
    if y_calc >= 0 and x_calc <= 0 or y_calc <= 0 and x_calc <= 0:
        angle += 180
    elif y_calc < 0 and x_calc > 0:
        angle += 360
    return angle

def calculate_angularVelocityAcceleration(RelativeAngleVelocity, time):
    # Calculate the angular velocity of a joint
    # relativeAngles: list of relative angles in degrees
    # time: list of time values in seconds
    # Returns the angular velocity in degrees per second
    angularVelocity = []
    for i in range(1, len(RelativeAngleVelocity) - 1):
        angularVelocity.append((RelativeAngleVelocity[i + 1] - RelativeAngleVelocity[i - 1]) / (time[i + 1] - time[i - 1]))
    return angularVelocity