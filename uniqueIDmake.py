import pandas as pd
datafile = pd.read_csv ('uniqueID.csv')
datafile["StudentID"] = ""


Courses = {"Advertising":200, "Archaeology":214, "Cinema Sciences":412 , "Economics":102, "History":636, "Journalism":231, "Languages":785, "Literature":124, "Mathematics":215, "Music":786, "Fine Arts":147, "Philosophy":300, "Political Science":152, "Psychology":193, "Public Administration":696, "Sociology":555, "Theology":465, "Theatre":798, "Urban Planning":159, "Veterinary Medicine":961, "Zoology":333}

Campuses = {"Noida":101, "Delhi":102, "Gurgaon":103, "Mumbai":104, "Pune":105, "Bangalore":106, "Hyderabad":107, "Chennai":108, "Kolkata":109, "Ahmedabad":110, "Jaipur":111, "Lucknow":112, "Chandigarh":113, "Indore":114, "Bhopal":115, "Patna":116, "Ranchi":117, "Bhubaneswar":118, "Vishakhapatnam":119, "Kochi":120, "Goa":121, "Shimla":122, "Dehradun":123, "Rajkot":124, "Surat":125, "Vadodara":126, "Nagpur":127, "Agra":128, "Amritsar":129, "Bareilly":130, "Bhavnagar":131, "Bhilai":132, "Bhiwandi":133, "Bikaner":134, "Bokaro Steel City":135, "Chandigarh":136, "Coimbatore":137, "Cuttack":138, "Dhanbad":139, "Durg-Bhilai Nagar":140, "Durgapur":141, "Erode":142, "Faridabad":143, "Firozabad":144, "Ghaziabad":145, "Gorakhpur":146}




count = 0
for i in range(5000):
    First_Name = datafile.iloc[i,0]
    # print(First_Name)
    Last_Name = datafile.iloc[i,1]
    # print(Last_Name)
    Course = datafile.iloc[i,2]
    # print(Course)
    Campus = datafile.iloc[i,4]
    # print(Campus)
    PassYear = (datafile.iloc[i,3])
    
    # if Course!=datafile.iloc[i-1,2] or Campus!=datafile.iloc[i+1,4]:
    #     count = 0
    count = count + 1
    print(Courses[Course])
    print(Campuses[Campus])
    StudentID = "A" + str(PassYear) + str(Courses[Course]) + str(Campuses[Campus]) + f"{count:03}"
    datafile.iloc[i,5] = StudentID

head = ["First_Name","Last_Name","Course","PassYear","Campus","StudentID"]
datafile.loc[0] = head

print(datafile.head())
datafile.to_csv('uniqueID.csv', header=False, index=False)

# First_Name,Last_Name,Course,PassYear,Campus


