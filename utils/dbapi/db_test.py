import asyncio

from data import config
from utils.dbapi.db_gino import db
from utils.dbapi import quick_commands

async def db_test():
     await db.set_bind(config.POSTGRES_URI)
     await db.gino.drop_all()
     await db.gino.create_all()

     await quick_commands.add_user(1, 'SOLO', 's')
     await quick_commands.add_user(2, 'DFD', 'Tester Name')
     await quick_commands.add_user(5, 'gfsafdsfsdf', 'ses')
     await quick_commands.add_user(7, 'gfsafdsfsdf', 'aboa')
     await quick_commands.add_user(6775, 'gfsafdsfsdf', 'nhgg')
     users = await quick_commands.select_all_users()
     print(users)

     count = await quick_commands.count_user()
     print(count)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(db_test())