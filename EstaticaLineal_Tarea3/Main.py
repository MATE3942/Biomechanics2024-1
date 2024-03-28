import math

# Get the data from the console
xs = float(input("Enter the x-coordinate of the S point: "))
ys = float(input("Enter the y-coordinate of the S point: "))
xt = float(input("Enter the x-coordinate of the T point: "))
yt = float(input("Enter the y-coordinate of the T point: "))
xm = float(input("Enter the x-coordinate of the M point: "))
ym = float(input("Enter the y-coordinate of the M point: "))
theta_t = float(input("Enter the angle of the T point in degrees: "))
w = float(input("Enter the weight of the person in Newtons: "))

# Calculate the requested data
theta_m = math.degrees(math.atan(((yt-(xt-xs)*math.tan(math.radians(theta_t))) - ym) / (xs - xm)))
Rm = (math.cos(math.radians(theta_t)) / math.sin(math.radians(theta_m - theta_t))) * w
Rt = Rm * (math.cos(math.radians(theta_m)) / math.cos(math.radians(theta_t)))

# Print the results
print(f"\nTheta_m: {theta_m}")
print(f"Rm: {Rm}")
print(f"Rt: {Rt}\n")
input("Press Enter to exit...")