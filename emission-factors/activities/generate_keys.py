import pandas as pd
import re


def to_camel_case(string):
    return "".join(x.capitalize() for x in str(string).lower().split(" "))


def to_lower_camel_case(string):
    # We capitalize the first letter of each component except the first one
    # with the 'capitalize' method and join them together.
    camel_string = to_camel_case(string)
    return str(string)[0].lower() + camel_string[1:]


def formatString(string):
    if pd.isna(string) == False:
        clean_string = "".join(re.findall(r"([a-zA-Z]|\d|\s|\.*)", string))
        return to_lower_camel_case(clean_string)
    return "BLANK"


def formatKey(region, unit, year, category, activityL1, activityL2):
    return f"{region}_{unit}_{year}_{category}_{activityL1}_{activityL2}"


def convertUnit(unit):
    unit_conversions = {
        "kg": "kg",
        "litres": "l",
        "GJ": "GJ",
        "kWh": "kWh",
        "kWh (Net CV)": "kWh",
        "kWh (Gross CV)": "kWhGross",
        "tonnes": "t",
        "Room per night": "roomsPerNight",
        "miles": "miles",
        "km": "km",
        "m3": "m3",
    }
    try:
        return unit_conversions[unit]
    except:
        raise Exception(
            f"Unit {unit} was not found in unit_conversions. \nPlease add value that corresponds to the manualEmissions-database unit and ensure that the unit is handled in the app and backend"
        )


### Generate keys

df = pd.read_csv(
    "./emission-factors/activities/activity_based_EF_database.csv", sep=";"
)
df["KEY"] = df.apply(
    lambda row: formatKey(
        row["Region"],
        convertUnit(row["Activity unit"]),
        row["Year"],
        formatString(row["GHG Scopes and categories L2"]),
        formatString(row["Activity L1"]),
        formatString(row["Activity L2"]),
    ),
    axis=1,
)
#  KEY-parts
df.to_csv("emission-factors/activities/activity_based_EF_database_out.csv", index=False)


# The output of this function should be the format of the values stored in the databases for the activities and categories
# It should also be the format used in the frontend for mapping values to messages.
def printFormattedUniqueValues(df, column):
    print(f"\n======= {column} =======\n")
    print(
        [
            x
            for x in df[column].apply(lambda row: formatString(row)).unique().tolist()
            if x != None
        ]
    )


printFormattedUniqueValues(df, "Activity L1")
printFormattedUniqueValues(df, "Activity L2")
printFormattedUniqueValues(df, "GHG Scopes and categories L2")
