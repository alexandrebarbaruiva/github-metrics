from github import Github
from config import get_config


class Collector:
    def __init__(self, access=[]):
        if len(access) == 1:
            self.g = Github(access[0])

    def get_org(self, org):
        o = self.g.get_organization(org)
        return o

    def get_org_repos(self, org):
        o = self.g.get_organization(org)
        repos = [repo.full_name for repo in list(o.get_repos())]
        return repos

    def get_all_contributors(self, repo):
        r = self.g.get_repo(repo)
        contributors = [user.login for user in list(r.get_contributors())]
        return contributors

    def get_stats_contributors(self, repo):
        r = self.g.get_repo(repo)
        itens = [{item.author.login: item.raw_data['weeks']} for item in list(r.get_stats_contributors())]
        return itens


if __name__ == '__main__':
    a = get_config()['log']
    credentials = [get_config("GITHUB")[a]]
    collector = Collector(credentials)
    print(collector.get_org_repos("ComputerSocietyUnB"))
    print(collector.get_all_contributors("ComputerSocietyUNB/CodingDojo"))
    print(collector.get_stats_contributors("ComputerSocietyUNB/CodingDojo"))
    print("Done")
