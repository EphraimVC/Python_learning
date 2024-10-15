import pandas as pd

# 1. Skapa en DataFrame från en dictionary av listor som innehåller information om 5 olika länder (namn, befolkning, yta, kontinent).
data={
    "name":["Sweden", "Turkey", "Albania", "France", "Peru"],
    "people":["1b", "9m", "250m", "1m", "2m"],
    "size":[234956,7846759,987937,8367584,789265],
    "continent":["Europe", "Asia","Europe", "Europe", "America"]
}

statistics= pd.DataFrame(data)
print(statistics)
# 2. Ladda filen 'sample_data0.csv' och visa de sista 10 raderna.
df = pd.read_csv("../sample_data0.csv")
print(df.tail(10))


#2.1. hitta den som har högst och lägst prestationspoäng
print("Heighest Performance score")
print(df["Performance_Score"].max())
print("Lowest Performance score")
print(df["Performance_Score"].min())

# 3. Beräkna och visa medianlönen för varje avdelning.
#denna visar medium lön och namnen på alla kolumner
mediumSalary2 = df[["Department", "Salary"]].groupby("Department")["Salary"].median().reset_index()
print(mediumSalary2)
#denna visar medium lön och namnen på första kolumn
mediumSalary = df.groupby("Department")["Salary"].median()
print(mediumSalary)
#denna visar medium lön och namnen på alla kolumner
mediumSalary1 = df.groupby("Department",as_index=False)["Salary"].median()
print(mediumSalary1)

# 4. Hitta den anställda med högst prestationspoäng i varje stad.
bestWorker= df.groupby("City")[["Performance_Score","Name"]].max().reset_index()
print(bestWorker)
#4.1. hitta den som har högst prestations poäng
best= bestWorker.max()
print(best)
# 5. Skapa en ny kolumn 'Lön_per_År_Erfarenhet' genom att dividera 'Salary' med 'Years_Experience'. Hantera eventuella division-med-noll-fel.

# 6. Använd funktionen `pd.melt()` för att omforma DataFrame:n, och gör 'Salary' och 'Performance_Score' kolumnerna till variabler.

# 7. Pivota DataFrame:n för att visa genomsnittlig lön för varje kombination av Stad och Avdelning.
