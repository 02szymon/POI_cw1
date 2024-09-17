import numpy as np
import pandas as pd

def generate_horizontal(center=(0, 0, 0), width=20, length=20, num_points=6000, file_name="pion.csv"):

    x_center, y_center, z_center = center
    x = np.random.uniform(x_center - width / 2, x_center + width / 2, num_points)
    y = np.random.uniform(y_center - length / 2, y_center + length / 2, num_points)
    z = np.full(num_points, z_center)

    points = np.column_stack((x, y, z))

    df = pd.DataFrame(points, columns=["x", "y", "z"])
    df.to_csv(file_name, index=False)

    return points

def generate_vertical(center=(0, 0, 0), width=20, height=20, num_points=6000, file_name="poziom.csv"):

    x_center, y_center, z_center = center
    x = np.random.uniform(x_center - width / 2, x_center + width / 2, num_points)
    y = np.full(num_points, y_center)
    z = np.random.uniform(z_center - height / 2, z_center + height / 2, num_points)

    points = np.column_stack((x, y, z))

    df = pd.DataFrame(points, columns=["x", "y", "z"])
    df.to_csv(file_name, index=False)

    return points


def generate_cylinder(center=(0, 0, 0), radius=10, height=20, num_points=6000, file_name="cylinder.csv"):

    x_center, y_center, z_center = center
    theta = np.random.uniform(0, 2 * np.pi, num_points)
    z = np.random.uniform(z_center - height / 2, z_center + height / 2, num_points)
    x = x_center + radius * np.cos(theta)
    y = y_center + radius * np.sin(theta)

    points = np.column_stack((x, y, z))

    df = pd.DataFrame(points, columns=["x", "y", "z"])
    df.to_csv(file_name, index=False)

    return points


def save_points_to_csv(points, file_name="polaczone.csv"):

    df = pd.DataFrame(points, columns=["x", "y", "z"])
    df.to_csv(file_name, index=False)


horizontal_points = generate_horizontal()
vertical_points = generate_vertical()
cylinder_points = generate_cylinder()
all_points = np.vstack((horizontal_points, vertical_points, cylinder_points))
save_points_to_csv(all_points)
print("Zzapisano wszystkie do jednego CSV.")

cylinder_points = generate_cylinder()
print("Cylindryczne zapisano do do CSV.")


vertical_points = generate_vertical()
print("Pionowe zapisano do do CSV.")


horizontal_points = generate_horizontal()
print("Poziome zapisano do do CSV.")