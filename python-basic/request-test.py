# -*- coding: utf-8 -*-
"""
Create Time: 2022/5/1 0:38
Author: Lison Song
"""
import requests

if __name__ == '__main__':
    response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
    my_projects = response.json()
    for project in my_projects:
        print(f"Project Name:{project['name']} \n"
              f"Project Url:{project['web_url']}\n")

