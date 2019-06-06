# Dictionary=  unordered
#key value pair

# empty
city ={}
print(city)

city_population = {"New York City":85.5,
                   "Toronto":27.3,
                   "India":132.4,
                   "China":138.7,
                   "Japan":126.4}

# user id =809
# message =“Happy Birth Day!”
# language = “ English”
# datetime = 1482223122760.0
# location = (40.7691, 73.9816)

post={"user id":809, "message":"Happy Birth Day!",
"language":"English",
"datetime":1482223122760.0 ,
"location": (40.7691, 73.9816)}

print(post['message'])

print(post['location'])

#updating the dictionary

post2= dict({"message":"Happy Birth Day!",
"language":"English"})

print(post)

post2["user_id"]  = "209"
post2["datetime"] = "1482223122760.0"

