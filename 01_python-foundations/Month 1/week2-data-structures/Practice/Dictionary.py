                                    # Example 1

# user_profile = {"username" : "YashW" , "email" : "yash@gmail.com" , "status" : "Inactive"}
#
# # Update the status to "Active" using the update() method.
# # 1
# user_profile["status"] = "Active"
# # 2
# user_profile.update({"status" : "Active"})
#
# # Use .get() to try and retrieve a key called last_login. Since it doesn't exist, make the method return "Never logged in"
#
# ans = user_profile.get("last login" , "Never Logged In")
# print(ans)
#
# # Last print
# print(user_profile)

                                  # Example 2 : Nested Library

library = {
            "shelf_A": {"title": "The Hobbit", "count": 2},
            "shelf_B": {"title": "1984", "count": 5}
            }

# # Access the count of "1984" on shelf_B and add 10 to it.
#
# 1. Get the current count safely
current_count = library["shelf_B"]["count"]

# 2. Update the value
library["shelf_B"]["count"] = current_count + 10

print(library["shelf_B"])

# Add a new shelf called shelf_C which contains a dictionary with a title of "Dracula" and a count of 3.

library.update({"shelf_C" : {"title": "Dracula", "count": 3}})
#
# # Delete shelf_A from the library using the pop() method.
#
# #1 del library["shelf_A"]
# #2
# library.pop("shelf_A")
#
# print(library)


                                        # Example 3 : The Method Master

scores = {}
dict = {'math' : 0 , 'science' : 0 , 'history': 0}

#Create a dictionary called scores using the dict.fromkeys() method. Use the list ['math', 'science', 'history'] and set the initial value for all of them to 0.

scores = dict.fromkeys(['math' , 'science' , 'history'] , 0)

print(scores)


#Use .setdefault() to add a score for "Art" as 95
#Now, use .setdefault() again on "math", but try to set it to 100. (Observe if it actually changes the 0 or stays the same!)
ans = scores.setdefault("Art", 95)
ans2 = scores.setdefault("math", 100)
ans3 = scores.setdefault("science", 80)
print(ans)
print(ans2)
print(ans3)

#Use .popitem() to remove the very last item you added and store it in a variable called removed_item.
removed_item = scores.popitem()
print(removed_item)


