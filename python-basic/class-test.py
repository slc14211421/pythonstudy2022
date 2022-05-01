# -*- coding: utf-8 -*-
"""
Create Time: 2022/4/30 23:57
Author: Lison Song
"""


class User:
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}."
              f"You can contact them as {self.email}")


class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author

    def get_post_info(self):
        print(f"Post: {self.message} written by {self.author}")


if __name__ == '__main__':
    tom = User("tom@gmail.com", "tom Janshia", "pwd1", "DevOps Enginner")
    jim = User("jim@gmail.com", "jim Yang", "pwd1", "Developer")
    tom.get_user_info()
    new_post = Post("on as secret mission tody", tom.name)
    new_post.get_post_info()
