import phonenumbers
from phonenumbers import carrier,geocoder,timezone

phn_no =input("Enter phone number with country code : ")
phn_no =phonenumbers.parse(phn_no)

#get timezone
print(timezone.time_zones_for_number(phn_no))
#get carrier of a phone number
print(carrier.name_for_number(phn_no,"en"))

#getting region information
print(geocoder.description_for_number(phn_no,"en"))
print("valid Mobile Number : ", phonenumbers.is_valid_number(phn_no))
print("Checking possibility of number : ",phonenumbers.is_possible_number(phn_no))
