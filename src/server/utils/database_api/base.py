# -------------- #
# System imports #

import asyncio
import os
from pathlib        import Path
from time import time
from typing import Self, Any
from types import TracebackType


# ------------------- #
# Third party imports #

import aiopg
import psycopg2
from psycopg2.extras import DictCursor, RealDictCursor, RealDictRow


# ------------- #
# Local imports #

class APIInterface:
    def __init__(self,
                 db_name:str|None=None,
                 db_user:str|None=None,
                 db_pass:str|None=None,
                 db_host:str|None=None,
                 db_port:str|None=None,
                 *args, **kwargs) -> None:
        """ Creates object to manipulate one particular DB.
            
            Parameters:

            : db_name - Name of the database to connect to. Example: "myDB";
            : db_user - User which has access to the DB. Example: "user";
            : db_pass - User password;
            : db_host - Host (or IP addr) of the DB. Example: "localhost";
            : db_port - Port of the DB. Example: "5432".
        """
        
        self._get_db_parameters(
                db_name,
                db_user,
                db_pass,
                db_host,
                db_port,
                )

        self.DSN = f'dbname={self.DB_NAME} user={self.DB_USER} password={self.DB_PASS} host={self.DB_HOST}'


    async def query(self, query:str) -> list[RealDictRow] | None:
        async with aiopg.connect(self.DSN) as con:
            async with con.cursor(
                    cursor_factory=RealDictCursor) as cursor:
                await cursor.execute(query)
                # result = {}
                try:
                    result = await cursor.fetchall()
                    # async for row in cursor:
                    #     result.append(row)
                    return result
                except psycopg2.ProgrammingError:
                    # no results to fetch
                    return None
                finally:
                    # Commit to store changes in the DB.
                    await cursor.execute("COMMIT")


    def _get_db_parameters(self,
            db_name:str|None,
            db_user:str|None,
            db_pass:str|None,
            db_host:str|None,
            db_port:str|None,
            ):
        """ Finds all necessary parameters needed to create
            connection to the PostgreSQL database.
            
            Parameters:

            : db_name - Name of the database to connect to. Example: "myDB";
            : db_user - User whihc has access to the DB. Example: "user";
            : db_pass - User password;
            : db_host - Host (or IP addr) of the DB. Example: "localhost";
            : db_port - Port of the DB. Example: "5432".
        """

        # If parameter not given in constructor -
        # Retreive it from ENV:
        # DB_NAME
        if not db_name:
            self.DB_NAME = os.getenv('POSTGRES_DB')
        else:
            self.DB_NAME = db_name
        # DB_USER
        if not db_user:
            self.DB_USER = os.getenv('POSTGRES_USER')
        else:
            self.DB_USER = db_user
        # DB_PASSWORD
        if not db_pass:
            self.DB_PASS = os.getenv('POSTGRES_PASSWORD')
        else:
            self.DB_PASS = db_pass
        # DB_HOST
        if not db_host:
            self.DB_HOST = os.getenv('POSTGRES_HOST')
        else:
            self.DB_HOST = db_host
        # DB_PORT
        if not db_port:
            self.DB_PORT = os.getenv('POSTGRES_PORT')
        else:
            self.DB_PORT = db_port

        # Check that all parameters are correct:
        # If not - exception will be raised.
        self._validate_db_parameters()


    def _validate_db_parameters(self) -> None:
        """ Checks that db parameters are not None and not empty.
            
            Parameters to check:

            : self.DB_NAME - Name of the database to connect to. Example: "myDB";
            : self.DB_USER - User whihc has access to the DB. Example: "user";
            : self.DB_PASS - User password;
            : self.DB_HOST - Host (or IP addr) of the DB. Example: "localhost";
            : self.DB_PORT - Port of the DB. Example: "5432".
        """

        if not self.DB_NAME or not self.DB_USER or not self.DB_PASS \
                or not self.DB_HOST or not self.DB_PORT:
            # raise Exception("Not all parameters are given!")
            print("Not all parameters are given!")

        


########
# MAIN #
########

async def main():

    db = APIInterface()
    sql = f"SELECT * FROM USERS;"
    start = time()

    response = await db.query(sql)
    print(response)
    response = await db.query(sql)
    print(response)
    response = await db.query(sql)
    print(response)
    response = await db.query(sql)
    print(response)

    end = time()
    print(start)
    print(end)
    print(end-start)

    start = time()
    result1, result2, result3 = await asyncio.gather(
        db.query(sql),
        db.query(sql),
        db.query(sql),
    )
    # print(result1, result2, result3)
    print()
    end = time()
    print(start)
    print(end)
    print(end-start)


if __name__ == "__main__":
    asyncio.run(main())
