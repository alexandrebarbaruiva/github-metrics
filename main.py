from github import Github


class Collector:
    def __init__(self, access=None, user=None, password=None):
        self.github = Github("user", "password")
