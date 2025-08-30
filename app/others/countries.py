
#Creates and populates a SQLite database with online food dellivery data from csv file
#Import csv
#import sqlite3
import csv
import sqlite3
print("Hola liz")
#create a connection to a sqlite file called"countries.db" in the "data" directory
connection = sqlite3.connect("data/countries.db")
#Create a cursor
cursor = connection.cursor()
#create the table named "countries.db with 36 colummns
cursor.execute("CREATE TABLE IF NOT EXISTS countries (Country TEXT, Year REAL, GDP REAL,  GDP_percapita REAL, Inflation_rate REAL, Population REAL, Population_Growth_rate REAL, Urban_Population_rate REAL, Life_Expectancy_years REAL, Health_care_Expenditure_per_Capita_USD REAL, Doctor_to_Patient_Ratio REAL, Literacy_Rate REAL,  Education_Expenditure REAL, Internet_Penetration REAL, Smartphone_Adoption REAL, Energy_consumption_TWh REAL, Renewable_Energy_Share REAL, Military_Expenditure_in_Billion_USD REAL, Number_of_Active_Military_Personnel REAL, CO2_Emissions_Million_Metric_Tons REAL, Forest_Coverage REAL, Number_of_Airports REAL, Road_Network_Lengthin_km REAL, Public_Transport_Usage REAL, Human_Development_Index_HDI REAL,  Gender_Equality_Index REAL,  Poverty_Rate REAL, Number_of_International_Visitors_in_Millions REAL, Tourism_Revenue_in_Billion_USD REAL, Agricultural_Land REAL, Unemployment_Rate REAL, Labor_Force_Participation_Rate REAL, Crime_Rate_per_100000 REAL, Corruption_Perception_Index REAL, Freedom_of_Press_Index REAL, Voting_Participation_Rate REAL)")
#open and reads a csv file called countries.csv fron the data directory.
#process the file row by row:
#Skips the header row and prints the column names
#For each data row,extracts all 12 fields
#prints each row´s datain a formatted way to the console
#instert each row into the SQLite database unsing iNSERT statement
with open ('data/countries.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ',')
    line_count = 0
    for row in csv_reader:
        if line_count== 0:
            print(f' Column names are {", ".join(row)}')
            line_count += 1
        else:
             Country = row[0]
             Year  = row[1]
             GDP = row[2]
             GDP_percapita = row[3]
             Inflation_rate = row[4]
             Population = row[5]
             Population_Growth_rate = row[6]
             Urban_Population_rate = row[7]
             Life_Expectancy_years = row[8]
             Health_care_Expenditure_per_Capita_USD = row[9]
             Doctor_to_Patient_Ratio = row[10]
             Literacy_Rate = row[10]
             Education_Expenditure = row[12]
             Internet_Penetration = row[13]
             Smartphone_Adoption= row[14]
             Energy_consumption_TWh = row[15]
             Renewable_Energy_Share = row[16]
             Military_Expenditure_in_Billion_USD = row[17]
             Number_of_Active_Military_Personnel = row[18]
             CO2_Emissions_Million_Metric_Tons = row[19]
             Forest_Coverage = row[20]
             Number_of_Airports = row[21]
             Road_Network_Lengthin_km = row[22]
             Public_Transport_Usage = row[23]
             Human_Development_Index_HDI = row[24]
             Gender_Equality_Index = row[25]
             Poverty_Rate = row[26]
             Number_of_International_Visitors_in_Millions = row[27]
             Tourism_Revenue_in_Billion_USD = row[28]
             Agricultural_Land = row[29]
             Unemployment_Rate = row[30]
             Labor_Force_Participation_Rate = row[31]
             Crime_Rate_per_100000 = row[32]
             Corruption_Perception_Index = row[33]
             Freedom_of_Press_Index = row[34]
             Voting_Participation_Rate = row[35]


             print(f'Country: {Country} \t Year: {Year} \t GDP: {GDP} \t GDP_percapita: {GDP_percapita} \t Inflation_rate: {Inflation_rate} \t Population: {Population}\t Population_Growth_rate: {Population_Growth_rate} \t Urban_Population_rate: {Urban_Population_rate}\t Life_Expectancy_years: {Life_Expectancy_years}\t Health_care_Expenditure_per_Capita_USD: {Health_care_Expenditure_per_Capita_USD}\t Doctor_to_Patient_Ratio: {Doctor_to_Patient_Ratio}\t Literacy_Rate: {Literacy_Rate}\t Education_Expenditure: {Education_Expenditure}\t Internet_Penetration: {Internet_Penetration}\t Smartphone_Adoption: {Smartphone_Adoption}\t Energy_consumption_TWh: {Energy_consumption_TWh}\t Renewable_Energy_Share: {Renewable_Energy_Share}\t Military_Expenditure_in_Billion_USD: {Military_Expenditure_in_Billion_USD}\t Number_of_Active_Military_Personnel: {Number_of_Active_Military_Personnel}\t CO2_Emissions_Million_Metric_Tons: {CO2_Emissions_Million_Metric_Tons}\t Forest_Coverage: {Forest_Coverage}\t Number_of_Airports: {Number_of_Airports}\t Road_Network_Lengthin_km: {Road_Network_Lengthin_km}\t Public_Transport_Usage: {Public_Transport_Usage}\t Human_Development_Index_HDI: {Human_Development_Index_HDI}\t Gender_Equality_Index: {Gender_Equality_Index}\t Poverty_Rate: {Poverty_Rate}\t Number_of_International_Visitors_in_Millions: {Number_of_International_Visitors_in_Millions}\t Tourism_Revenue_in_Billion_USD: {Tourism_Revenue_in_Billion_USD}\t Agricultural_Land: {Agricultural_Land}\t Unemployment_Rate: {Unemployment_Rate}\t Labor_Force_Participation_Rate: {Labor_Force_Participation_Rate}\t Crime_Rate_per_100000: {Crime_Rate_per_100000}\t Corruption_Perception_Index: {Corruption_Perception_Index}\t Corruption_Perception_Index: {Corruption_Perception_Index}\t Freedom_of_Press_Index: {Freedom_of_Press_Index}\t Voting_Participation_Rate: {Voting_Participation_Rate}')

              # TO-DO: Don't add data if its a duplicate
             cursor.execute(f"INSERT INTO countries VALUES ('{Country}', '{Year}', '{GDP}', '{GDP_percapita}', '{Inflation_rate}', '{Population}', '{Population_Growth_rate}', '{Urban_Population_rate}', '{Life_Expectancy_years}', '{Health_care_Expenditure_per_Capita_USD}', '{Doctor_to_Patient_Ratio}', '{Literacy_Rate}', '{Education_Expenditure}', '{Internet_Penetration}', '{Smartphone_Adoption}', '{Energy_consumption_TWh}', '{Renewable_Energy_Share}', '{Military_Expenditure_in_Billion_USD}', '{Number_of_Active_Military_Personnel}', '{CO2_Emissions_Million_Metric_Tons}', '{Forest_Coverage}', '{Number_of_Airports}', '{Road_Network_Lengthin_km}', '{Public_Transport_Usage}',  '{Human_Development_Index_HDI}', '{Gender_Equality_Index}', '{Poverty_Rate}', '{Number_of_International_Visitors_in_Millions}', '{Tourism_Revenue_in_Billion_USD}', '{Agricultural_Land}', '{Unemployment_Rate}', '{Labor_Force_Participation_Rate}', '{Crime_Rate_per_100000}', '{Corruption_Perception_Index}', '{Freedom_of_Press_Index}', '{Voting_Participation_Rate}')")

             connection.commit()
             line_count += 1
    print(f'Processed {line_count} lines.')
    print("query the database and print on the screen")
rows = cursor.execute("SELECT Country, Year, GDP, GDP_percapita, Inflation_rate, Population, Population_Growth_rate, Urban_Population_rate, Life_Expectancy_years, Health_care_Expenditure_per_Capita_USD, Doctor_to_Patient_Ratio, Literacy_Rate, Education_Expenditure, Internet_Penetration, Smartphone_Adoption, Energy_consumption_TWh, Renewable_Energy_Share, Military_Expenditure_in_Billion_USD, Number_of_Active_Military_Personnel, CO2_Emissions_Million_Metric_Tons, Forest_Coverage, Number_of_Airports, Road_Network_Lengthin_km, Public_Transport_Usage, Human_Development_Index_HDI, Gender_Equality_Index, Poverty_Rate, Number_of_International_Visitors_in_Millions, Tourism_Revenue_in_Billion_USD, Agricultural_Land, Unemployment_Rate, Labor_Force_Participation_Rate, Crime_Rate_per_100000, Corruption_Perception_Index, Freedom_of_Press_Index, Voting_Participation_Rate FROM countries").fetchall()
print(rows)
#loop through databse and print the data nicely
#lets do some analytics: count how many birds we have? 
connection.close()