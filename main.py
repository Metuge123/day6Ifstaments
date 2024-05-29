print("SECURE LOGIN")
username = input("Username >")
password = input("password >")
if username == 'mark' and password == 'password':
  print("Welcome Mark!")
elif username == 'suzanne' and password == 'suzanne':
  print("Hey there suzanne")
elif username == 'suzanne':
  print("Hey there suzanne!")
else:
  print("Go away!")

print()
season = input("what is your favorite season?")
if season == "spring":
  print("Ah! The birds are chirping and flowers blooming.")
elif season == "summer":
  print("Catch some sun and cool off with a lemonade.")
elif season == "autumn":
  print("The leaves are changing and the air is crisp. Enjoy!")
elif season == "winter":
  print("Stay warm by the fire and watch the snow fall.")
else:
  print("I don't know that season. Please try again.")
