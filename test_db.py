import db_helper

db_helper.setup_db()
db_helper.add_player("TestUser")
db_helper.add_score("TestUser", 10)

print("Database working!")
