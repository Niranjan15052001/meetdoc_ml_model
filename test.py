import requests
mydata={
    'Symptom1':'vomiting',
    'Symptom2':'headache',
    'Symptom3':'nausea',
    'Symptom4':'spinning_movements'
}
r=requests.get("http://niru150789.pythonanywhere.com/api/v1/preprocess",data=mydata)