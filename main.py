import vk_api

import os

from dotenv import load_dotenv

load_dotenv()
Token = os.getenv("TOKEN")
token = vk_api.VkApi(token = Token)
vk = token.get_api()
user_data = vk.users.get(user_ids = 'slaveeks')
print(user_data[0]["first_name"])
