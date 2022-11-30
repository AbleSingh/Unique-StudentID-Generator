import pandas as pd
from faker import Faker
import random
fake = Faker()

#list of university courses
Courses = {"Advertising":200, "Archaeology":214, "Cinema Sciences":412 , "Economics":102, "History":636, "Journalism":231, "Languages":785, "Literature":124, "Mathematics":215, "Music":786, "Fine Arts":147, "Philosophy":300, "Political Science":152, "Psychology":193, "Public Administration":696, "Sociology":555, "Theology":465, "Theatre":798, "Urban Planning":159, "Veterinary Medicine":961, "Zoology":333}

Campuses = {"Noida":101, "Delhi":102, "Gurgaon":103, "Mumbai":104, "Pune":105, "Bangalore":106, "Hyderabad":107, "Chennai":108, "Kolkata":109, "Ahmedabad":110, "Jaipur":111, "Lucknow":112, "Chandigarh":113, "Indore":114, "Bhopal":115, "Patna":116, "Ranchi":117, "Bhubaneswar":118, "Vishakhapatnam":119, "Kochi":120, "Goa":121, "Shimla":122, "Dehradun":123, "Rajkot":124, "Surat":125, "Vadodara":126, "Nagpur":127, "Agra":128, "Amritsar":129, "Bareilly":130, "Bhavnagar":131, "Bhilai":132, "Bhiwandi":133, "Bikaner":134, "Bokaro Steel City":135, "Chandigarh":136, "Coimbatore":137, "Cuttack":138, "Dhanbad":139, "Durg-Bhilai Nagar":140, "Durgapur":141, "Erode":142, "Faridabad":143, "Firozabad":144, "Ghaziabad":145, "Gorakhpur":146}

Years = [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]

df = pd.DataFrame(columns = ['First_Name', 'Last_Name', 'Course', 'PassYear', 'Campus'])

for i in range(5001):
    First_Name = fake.first_name()
    Last_Name = fake.last_name()
    Course = random.choice(list(Courses.keys()))
    PassYear = random.choice(Years)
    Campus = random.choice(list(Campuses.keys()))
    Newrow = [First_Name, Last_Name, Course, PassYear, Campus]
    df.loc[len(df)] = Newrow

df = (
    df.assign(key=df.groupby('Campus')['Course'].transform('max'))
        .sort_values(['key', 'Campus', 'Course'], ascending=False, ignore_index=True)
        .drop(columns=['key'])
)



df.to_csv('uniqueID.csv', header=False, index=False)