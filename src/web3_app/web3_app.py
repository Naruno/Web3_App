#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from kot import KOT

from naruno.apps.remote_app import Integration

import time
import fire
import pickle
import contextlib

database = KOT("database")

class web3:
    command_line = False
    def __init__(self, password, port=8000, host="localhost", hour=4):
        self.integration = Integration("Web3", password=password, port=port, host=host)

        self.post_wait_time = hour * 60 * 60


        self.official = "c923c646f2d73fcb8f626afacb1a0ade8d98954a"




    
    def username(self, username:str):
        #its should max 15 char
        if len(username) > 15:
            raise Exception("Username should be max 15 char")
        self.integration.send("username", username, self.official)
    
    def post(self, post:str):
        #its should max 100 char
        if len(post) > 100:
            raise Exception("Post should be max 100 char")
        self.integration.send("post", post, self.official)

    def get_user(self, username:str):
        record = database.get(username)
        if record == None:
            record = {"username": username, "posts": [], "last_post": 0}
        return record


    def run(self):
        while True:
            data = self.integration.get()
            if data != []:
                for each in data:
                    user = each["fromUser"]
                    action = each["data"]["action"]
                    data = each["data"]["app_data"]

                    control = True

                    if not isinstance(data, str):
                        control = False
                    if not isinstance(user, str):
                        control = False
                    
                    if action not in ["username", "post"]:
                        control = False

                    if action == "username":
                        if len(data) > 15:
                            control = False
                    elif action == "post":
                        if len(data) > 100:
                            control = False
                        if time.time() - self.get_user(user)["last_post"] < self.post_wait_time:
                            control = False
                        
                    
                    if control:
                        database_user = self.get_user(user)

                        if action == "username":
                            database_user["username"] = data
                        elif action == "post":
                            database_user["posts"].append(data)

                        database_user["last_post"] = time.time()
                        
                        database.set(user, database_user)



            time.sleep(5)

    def close(self):
        self.integration.close()

def main():
    web3.command_line = True
    fire.Fire(web3)