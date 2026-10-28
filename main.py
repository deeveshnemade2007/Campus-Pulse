import pandas as pd
import os
import subprocess
import sys
import matplotlib.pyplot as plt

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
        percentage = float(
            input("\nEnter expected savings percentage (0-100): ")
        )

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


def show_building_graph(df):
    usage = df.groupby("Building")["Electricity_kWh"].mean()

    usage.plot(kind="bar", figsize=(9, 5))
    plt.title("Average Electricity Usage by Building")
    plt.xlabel("Building")
    plt.ylabel("Average Electricity Usage (kWh/day)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.show()


def show_daily_graph(df):
    daily = df.groupby("Day")["Electricity_kWh"].sum()

    plt.figure(figsize=(10, 5))
    plt.plot(daily.index, daily.values, marker="o")
    plt.title("Daily Campus Electricity Usage")
    plt.xlabel("Day")
    plt.ylabel("Total Electricity Usage (kWh)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def show_pie_chart(df):
    usage = df.groupby("Building")["Electricity_kWh"].sum()

    plt.figure(figsize=(8, 6))
    plt.pie(
        usage.values,
        labels=usage.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Building-wise Share of Electricity Consumption")
    plt.tight_layout()
    plt.show()


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
        print("7. Show Building-Wise Bar Graph")
        print("8. Show Daily Usage Line Graph")
        print("9. Show Electricity Consumption Pie Chart")
        print("10. Exit")

        choice = input("\nEnter your choice (1-10): ").strip()

        if choice == "1":
            generate_data()

        elif choice == "10":
            print("\nThank you for using CampusPulse!")
            break

        elif choice in ["2", "3", "4", "5", "6", "7", "8", "9"]:
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
                elif choice == "7":
                    show_building_graph(df)
                elif choice == "8":
                    show_daily_graph(df)
                elif choice == "9":
                    show_pie_chart(df)

            except Exception as error:
                print("An error occurred:", error)

        else:
            print("Invalid choice. Please select 1 to 10.")


if __name__ == "__main__":
    main()