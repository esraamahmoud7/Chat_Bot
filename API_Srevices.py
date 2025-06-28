import requests

import Constants


class BackendDataFetcher:
    def __init__(self):
        self.base_url = Constants.BASE_URL
        self.headers = {
            "Authorization": f"Bearer {Constants.OrgTOKEN}",
            "Content-Type": "application/json"
        }

    # 1. Get all available courses
    def fetch_courses(self):
        try:
            url = f"{self.base_url}/api/courses/get-not-registered-courses/"
            response = requests.get(url, headers=self.headers)
            # throw an error to catch
            response.raise_for_status()
            courses = response.json()

            if not courses:
                return " "

            return response.json() if response.status_code == 200 else None

        except Exception as e:
            return f" Failed to fetch courses: {e}"

    def fetch_orgs(self):
        try:
            url = f"{self.base_url}/api/auth/get-all-organizations/"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            orgs = response.json()

            if not orgs:
                return " "

            return orgs if response.status_code == 200 else None

        except Exception as e:
            return f" Failed to fetch orgs: {e}"

    #  2. Get all job posts
    def fetch_jobs(self, org_id):
        try:
            url = f"{self.base_url}/api/posts/jobs/org/{org_id}"
            response = requests.get(url,headers=self.headers)
            response.raise_for_status()
            jobs = response.json()

            # if not jobs:
            #     print("No jobs found")
            #     return []

            return jobs

        except Exception as e:
            print(f"Failed to fetch jobs: {e}")
            return []

    # 3. Get all available services
    def fetch_services(self,org_id):
        try:
            url = f"{self.base_url}/api/posts/services/org/{org_id}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            services = response.json()

            # if not services:
            #     return "No services available."

            return services

        except Exception as e:
            return f" Failed to fetch services: {e}"

    # 4. Get user's technical profile
    def fetch_user_tech_info(self):
        try:
            url = f"{self.base_url}/api/techical-info/technical-info/"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            courses = response.json()

            if not courses:
                return " "

            return response.json() if response.status_code == 200 else None

        except Exception as e:
            return f" Failed to fetch courses: {e}"
