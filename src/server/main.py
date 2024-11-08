# -------------- #
# System imports #

import asyncio


# ------------------- #
# Third party imports #


# ------------- #
# Local imports #

from utils.datastructures      import database, logger



# --------- #
# CONSTANTS #


# ------- #
# OBJECTS #


# --------- #
# FUNCTIONS #


# ------- #
# CLASSES #


# ---- #
# MAIN #

async def main():
    """
        Main async function.
    """
    
    while True:

        # Demo async request to database
        users = await database.test_get_users()
        logger.server.debug(f"Got users from DB: {users}")

        await asyncio.sleep(2)



if __name__ == "__main__":
    asyncio.run(main())
