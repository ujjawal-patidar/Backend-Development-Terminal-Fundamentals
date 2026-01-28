cache ={}
db ={
    "1" : {
        "username" : "Ujjawal Patidar",
        "email" : "ujjawal@gmail.com"
    } ,
    "2" : {
        "username" : "Anant Patidar",
        "email" : "anant@gmail.com"
    }
}

def get_user(userId):
    if(cache.get(userId)):
        print("Fetched from cache : ")
        return cache.get(userId)
    
    print("fetched from database and stored to cache : ")
    cache[userId] = db[userId]
    return cache[userId]

# First time accessing the userid "2"
print("result :" , get_user("2"))

print()
print("updated cache :" , cache)
print("Database data : ", db)

# Now next time if you will type to access user with id "2" it will e returned by cache not need to access database

print()
print(get_user("2"))

print()
print("updated cache :" , cache)
print("Database data : ", db)