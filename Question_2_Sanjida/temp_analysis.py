import os
import glob
import pandas as pd

def get_season(month):
    if month in ["December", "January", "February"]:
        return "Summer"
    elif month in ["March", "April", "May"]:
        return "Autumn"
    elif month in ["June", "July", "August"]:
        return "Winter"
    else:
        return "Spring"

def main():
    csv_files = glob.glob(os.path.join("temperatures", "*.csv"))
    months = ["January","February","March","April","May","June",
              "July","August","September","October","November","December"]

    station_temps = {}
    season_temps = {"Summer":[], "Autumn":[], "Winter":[], "Spring":[]}

    for file in csv_files:
        df = pd.read_csv(file)

        for i in range(len(df)):
            station = df.loc[i, "STATION_NAME"]
            if station not in station_temps:
                station_temps[station] = []

            for m in months:
                temp = df.loc[i, m]
                if pd.isna(temp):
                    continue
                station_temps[station].append(temp)
                season_temps[get_season(m)].append(temp)

    with open("average_temp.txt", "w") as f:
        for s in ["Summer","Autumn","Winter","Spring"]:
            avg = sum(season_temps[s]) / len(season_temps[s])
            f.write(f"{s}: {avg:.1f}°C\n")

    ranges = {}
    for s, t in station_temps.items():
        if len(t) > 0:
            ranges[s] = (max(t)-min(t), max(t), min(t))

    max_range = max(v[0] for v in ranges.values())

    with open("largest_temp_range_station.txt", "w") as f:
        for s, (r, mx, mn) in ranges.items():
            if abs(r - max_range) < 1e-9:
                f.write(f"{s}: Range {r:.1f}°C (Max: {mx:.1f}°C, Min: {mn:.1f}°C)\n")

    stds = {}
    for s, t in station_temps.items():
        if len(t) >= 2:
            stds[s] = pd.Series(t).std()

    min_std = min(stds.values())
    max_std = max(stds.values())

    with open("temperature_stability_stations.txt", "w") as f:
        for s, sd in stds.items():
            if abs(sd - min_std) < 1e-9:
                f.write(f"Most Stable: {s}: StdDev {sd:.1f}°C\n")
        for s, sd in stds.items():
            if abs(sd - max_std) < 1e-9:
                f.write(f"Most Variable: {s}: StdDev {sd:.1f}°C\n")

    print("Done")

if __name__ == "__main__":
    main()
