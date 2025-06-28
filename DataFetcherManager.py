import Sys_Data
from API_Srevices import BackendDataFetcher


class DataFetcherManager:
    def __init__(self):
        self.states = {}
        self.API = BackendDataFetcher()

    def fetch_all(self):
        # add the whole data
        Sys_Data.Data.clear()
        Sys_Data.Data['Courses'] = self.API.fetch_courses()
        Sys_Data.Data['Tech_info'] = self.API.fetch_user_tech_info()
        orgs = self.API.fetch_orgs()
        all_jobs = []
        for org in orgs:
            jobs = self.API.fetch_jobs(org['id'])
            all_jobs.extend(jobs)
        Sys_Data.Data["Jobs"] = all_jobs
        all_Services = []
        for org in orgs:
            service = self.API.fetch_services(org['id'])
            all_Services.extend(service)
        Sys_Data.Data["Services"] = all_Services
        # print(Sys_Data.Data["Services"])




