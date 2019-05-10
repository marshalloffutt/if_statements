current_users = ['larry', 'barry', 'gary', 'terry', 'jerry']

new_users = ['harry', 'Perry', 'GARY', 'teRry', 'mary']

for user in new_users:
    if user.lower() in current_users:
        print("That name is already in use. You will need to pick a new username.")
    else:
        print("Congratulations " + user + ", welcome to the party.")