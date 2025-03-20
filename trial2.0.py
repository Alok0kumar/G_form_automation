import requests
# Successfull submission of the form
# Google Forms API endpoint
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfIFMWue54765iy2eGO7KnSdQaNuipy3dh_i4HcJrX4DPwqIQ/formResponse"

# Make sure entry IDs and responses match the form
data = {
    "entry.559352220": "User1",  # What is your name?
    "entry.924523986": "9",   # How many of you are attending? (if text input)
    "entry.1751303409": "No",  # Do you have any allergies or dietary restrictions?
    "entry.443565211": "de.coderr0101@gmail.com",  # Email Address
    "entry.877086558": "Yes,  I'll be there",   # Can you attend? (Use exact option text)
    "entry.186230675": "Dessert"   # What will you be bringing? (Use exact option text)
}

# Send the form submission request
response = requests.post(form_url, data=data)

if response.status_code == 200:
    print("✅ Form submitted successfully!")
else:
    print(f"❌ Failed to submit form. Status Code: {response.status_code}")
