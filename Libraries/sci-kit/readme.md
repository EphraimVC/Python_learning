## Scikit-learn-övningar

21. Använd scikit-learn:s `train_test_split`-funktion för att dela upp data i tränings- och testuppsättningar. Använd 'Salary' som målvariabel och 'Age', 'Years_Experience' och 'Performance_Score' som egenskaper.

22. Träna en enkel linjär regressionsmodell med scikit-learn för att förutsäga 'Salary' baserat på 'Years_Experience'. Plotta regressionslinjen tillsammans med ett spridningsdiagram av data.

Kom ihåg att importera de nödvändiga biblioteken (pandas, numpy, matplotlib.pyplot, seaborn och sklearn) innan du börjar med dessa övningar. Lycka till!

23. Vidare dataanalys och visualisering

Skapa ett program som använder pandas, numpy och matplotlib för att analysera och visualisera data från en CSV-fil med aktiemarknadsdata. Programmet ska:

1. Läsa in data och förbehandla den (hantera saknade värden, etc.)
2. Beräkna rullande medelvärden och standardavvikelser
3. Identifiera trender och anomalier
4. Skapa visualiseringar som linjediagram, histogram och scatterplots
5. Spara resultaten i en ny CSV-fil och bilderna som PNG-filer

24. Implementera en enkel linjär regression

För mer erfarna programmerare, implementera en enkel linjär regressionsalgoritm från grunden:

1. Skapa en klass `LinearRegression` med metoder för att träna modellen och göra prediktioner.
2. Implementera minsta kvadratmetoden för att hitta den bästa passformen.
3. Använd numpy för matrisoperationer.
4. Testa din implementation på ett enkelt dataset och jämför resultaten med sklearn's LinearRegression.