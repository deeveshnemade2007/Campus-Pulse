import pandas as pd
import os
import subprocess
import sys

FILE = "data/campus_data.csv"


def generate_data():
    subprocess.run([sys.executable, "generate_data.py"], check=True)


def load_data():
    if not os.path.exists(FILE):
        print("\nDataset not found. Generating it now...")
        generate_data()

    return pd.read_csv(FILE)


def show_summary(df):
    usage = df["Electricity_kWh"]

    print("\n========== ELECTRICITY SUMMARY ==========")
    print("Total Electricity Usage:", usage.sum(), "kWh")
    print("Average Reading:", round(usage.mean(), 2), "kWh")
    print("Highest Reading:", usage.max(), "kWh")
    print("Lowest Reading:", usage.min(), "kWh")


def show_buildings(df):
    print("\n========== BUILDING-WISE USAGE ==========")

    result = df.groupby("Building")["Electricity_kWh"].mean()

    for building, usage in result.items():
        print(building, ":", round(usage, 2), "kWh/day")


def detect_high_usage(df):
    try:
        limit = float(input("\nEnter alert limit in kWh: "))

        if limit < 0:
            print("Please enter a non-negative limit.")
            return

        alerts = df[df["Electricity_kWh"] > limit]

        print("\n========== HIGH USAGE ALERTS ==========")

        if alerts.empty:
            print("No readings exceeded the limit.")
        else:
            print(alerts.to_string(index=False))
            print("\nTotal high-usage readings:", len(alerts))

    except ValueError:
        print("Please enter a valid number.")


def calculate_savings(df):
    try:
        percentage = float(input("\nEnter expected savings percentage (0-100): "))

        if not 0 <= percentage <= 100:
            print("Enter a percentage between 0 and 100.")
            return

        total = df["Electricity_kWh"].sum()
        saved = total * percentage / 100

        print("\n========== SAVINGS ESTIMATE ==========")
        print("Current Usage:", round(total, 2), "kWh")
        print("Potential Savings:", round(saved, 2), "kWh")
        print("Usage After Savings:", round(total - saved, 2), "kWh")

        rate = float(input("Enter electricity price per kWh (₹): "))

        if rate < 0:
            print("Electricity price cannot be negative.")
            return

        print("Estimated Cost Savings: ₹", round(saved * rate, 2))

    except ValueError:
        print("Please enter a valid number.")


def show_daily_usage(df):
    print("\n========== DAILY ELECTRICITY USAGE ==========")

    daily = df.groupby("Day")["Electricity_kWh"].sum()

    for day, usage in daily.items():
        print("Day", day, ":", usage, "kWh")


def main():
    print("\n========================================")
    print(" CAMPUSPULSE ELECTRICITY ANALYZER")
    print("========================================")
    print("Note: All electricity readings are simulated.")

    while True:
        print("\n============== MAIN MENU ==============")
        print("1. Generate Electricity Dataset")
        print("2. View Electricity Summary")
        print("3. View Building-Wise Usage")
        print("4. Detect High Electricity Usage")
        print("5. Estimate Electricity Savings")
        print("6. View Daily Electricity Usage")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            generate_data()

        elif choice == "7":
            print("\nThank you for using CampusPulse!")
            break

        elif choice in ["2", "3", "4", "5", "6"]:
            try:
                df = load_data()

                if choice == "2":
                    show_summary(df)
                elif choice == "3":
                    show_buildings(df)
                elif choice == "4":
                    detect_high_usage(df)
                elif choice == "5":
                    calculate_savings(df)
                elif choice == "6":
                    show_daily_usage(df)

            except Exception as error:
                print("An error occurred:", error)

        else:
            print("Invalid choice. Please select 1 to 7.")


if __name__ == "__main__":
    main()