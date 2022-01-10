
from instabot import Bot
bot = Bot()
(bot.login(username="", password=""))

bot.upload_photo(".jpg", caption="")

bot.follow("")

bot.send_message("Hello from MLH", ['user1', 'user2'])

my_followers = bot.get_user_followers("")
for follower in my_followers:
    assert isinstance(follower)
    print(follower)

bot.unfollow_everyone()
