import csv
import math

def csv_to_arrays(csv_file, has_header=True):
    # Frame
    Frm = []
    # Crésta Hilíaca
    Cix, Ciy = [], []
    # Trocánter Mayor
    TMx, TMy = [], []
    # Rodilla
    Rodx, Rody = [], []
    # Tobillo
    Tobx, Toby= [], []
    # Talón
    Talx, Taly = [], []
    # Dedos
    Dedx, Dedy = [], []
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            if has_header:
                next(csv_reader)  # Skip the header row
            for row in csv_reader:
                if len(row) >= 2:
                    Fr, Cx, Cy, Tx, Ty, Rx, Ry, Tox, Toy, Tax, Tay, Dx, Dy = float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4]), \
                        float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]), float(row[11]), float(row[12])
                    Frm.append(Fr)
                    Cix.append(Cx); Ciy.append(Cy); TMx.append(Tx); TMy.append(Ty)
                    Rodx.append(Rx); Rody.append(Ry); Tobx.append(Tox); Toby.append(Toy)
                    Talx.append(Tax); Taly.append(Tay); Dedx.append(Dx); Dedy.append(Dy)
                else:
                    print("Skipping a row with insufficient data:", row)
    except FileNotFoundError:
        print(f"File not found: {csv_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return Frm, Cix, Ciy, TMx, TMy, Rodx, Rody, Tobx, Toby, Talx, Taly, Dedx, Dedy

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