import Files.Functions as app
import matplotlib.pyplot as plt

# CSV file to read
csvFile = "Datos_cinematicos.csv"
# Read the CSV file and store the data in arrays
Frm, Cix, Ciy, TMx, TMy, Rodx, Rody, Tobx, Toby, Talx, Taly, Dedx, Dedy = app.csv_to_arrays(csv_file=csvFile)

# Hip angle
# Calculate the absolute angles
Theta_at = []
Theta_am = []
w_hip = []
for i in range(len(TMx)):
    Theta_at.append(app.calculate_absoluteAngles(Prox_X=Cix[i], Prox_Y=Ciy[i], Dist_X=TMx[i], Dist_Y=TMy[i]))
    Theta_am.append(app.calculate_absoluteAngles(Prox_X=TMx[i], Prox_Y=TMy[i], Dist_X=Rodx[i], Dist_Y=Rody[i]))
# Calculate the relative angle
for i in range(len(Theta_at)):
    w_hip.append(Theta_am[i] - Theta_at[i])
# Plot the relative angle
plt.plot(Frm, w_hip, color='blue', linewidth=2.0, linestyle='-')
plt.title("Hip relative angle")
plt.xlabel("Frames (120fps)")
plt.ylabel("Relative Angle (°)")
plt.show()

# Knee angle
# Calculate the absolute angles
Theta_am = []
Theta_ap = []
w_knee = []
for i in range(len(Rodx)):
    Theta_am.append(app.calculate_absoluteAngles(Prox_X=TMx[i], Prox_Y=TMy[i], Dist_X=Rodx[i], Dist_Y=Rody[i]))
    Theta_ap.append(app.calculate_absoluteAngles(Prox_X=Rodx[i], Prox_Y=Rody[i], Dist_X=Tobx[i], Dist_Y=Toby[i]))
# Calculate the relative angle
for i in range(len(Theta_am)):
    w_knee.append(Theta_am[i] - Theta_ap[i])
# Plot the relative angle
plt.plot(Frm, w_knee, color='green', linewidth=2.0, linestyle='-')
plt.title("Knee relative angle")
plt.xlabel("Frames (120fps)")
plt.ylabel("Relative Angle (°)")
plt.show()

# Ankle angle
# Calculate the absolute angles
Theta_ap = []
Theta_ae = []
w_ankle = []
for i in range(len(Tobx)):
    Theta_ap.append(app.calculate_absoluteAngles(Prox_X=Rodx[i], Prox_Y=Rody[i], Dist_X=Tobx[i], Dist_Y=Toby[i]))
    Theta_ae.append(app.calculate_absoluteAngles(Prox_X=Talx[i], Prox_Y=Taly[i], Dist_X=Dedx[i], Dist_Y=Dedy[i]))
# Calculate the relative angle
for i in range(len(Theta_ap)):
    w_ankle.append(Theta_ae[i] - Theta_ap[i] - 90)
# Plot the relative angle
plt.plot(Frm, w_ankle, color='red', linewidth=2.0, linestyle='-')
plt.title("Ankle relative angle")
plt.xlabel("Frames (120fps)")
plt.ylabel("Relative Angle (°)")
plt.show()