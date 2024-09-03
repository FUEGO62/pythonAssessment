class BackToSender:
    

    def wage_calculator(parcel_size):
        wage = 0
        if parcel_size < 50:
            wage = (parcel_size * 160) + 5000
        elif 50 <= parcel_size <= 59:
            wage = (parcel_size * 200) + 5000
        elif parcel_size >= 70:
            wage = (parcel_size * 500) + 5000
        elif 60 <= parcel_size <= 69:
            wage = (parcel_size * 250) + 5000
        return wage

number = int(input("How many parcels did you deliver? "))
wage = BackToSender.wage_calculator(number)
print(wage)
