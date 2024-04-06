import math
import sys

# Constants
theta_spacing = 0.07
phi_spacing = 0.02
R1 = 0.05
R2 = 0.5
K2 = 5
K1 = 80 * K2 * 3 / (8 * (R1 + R2))

# Function to render the frame
def render_frame(A, B):
    # Precompute sines and cosines of A and B
    cosA = math.cos(A)
    sinA = math.sin(A)
    cosB = math.cos(B)
    sinB = math.sin(B)

    # Initialize output frame and z-buffer
    output = [[' '] * 80 for _ in range(24)]
    zbuffer = [[0] * 80 for _ in range(24)]

    # Iterate through theta and phi
    for theta in range(int(2 * math.pi / theta_spacing)):
        costheta = math.cos(theta * theta_spacing)
        sintheta = math.sin(theta * theta_spacing)
        for phi in range(int(2 * math.pi / phi_spacing)):
            cosphi = math.cos(phi * phi_spacing)
            sinphi = math.sin(phi * phi_spacing)

            # Compute coordinates
            circlex = R2 + R1 * costheta
            circley = R1 * sintheta
            x = circlex * (cosB * cosphi + sinA * sinB * sinphi) - circley * cosA * sinB
            y = circlex * (sinB * cosphi - sinA * cosB * sinphi) + circley * cosA * cosB
            z = K2 + cosA * circlex * sinphi + circley * sinA
            ooz = 1 / z

            # Compute 2D projection
            xp = int(40 + K1 * ooz * x)
            yp = int(12 + K1 * ooz * y)

            # Compute luminance
            L = cosphi * costheta * sinB - cosA * costheta * sinphi - sinA * sintheta + cosB * (cosA * sintheta - costheta * sinA * sinphi)
            if L > 0:
                if 0 <= xp < 80 and 0 <= yp < 24:
                    if ooz > zbuffer[yp][xp]:
                        zbuffer[yp][xp] = ooz
                        luminance_index = int(L * 8)
                        output[yp][xp] = ".,-~:;=!*#$@"[luminance_index]

    # Output the frame
    sys.stdout.write("\x1b[H")
    for row in output:
        sys.stdout.write(''.join(row) + '\n')

# Main function
if __name__ == "__main__":
    frames = 6000  # Adjust the number of frames to slow down the animation
    for frame in range(frames):
        t = frame / 100
        A = t
        B = 0.8 * t
        render_frame(A, B)
