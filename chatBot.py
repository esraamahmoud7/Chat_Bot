# chat_flow.py
from Sys_Data import AboutHireNy


class ChatFlowManager:
    def __init__(self, data, token):
        self.states = {}
        self.data = data
        self.TOKEN = token


    def reset(self, user_id):
        self.states[user_id] = "start"

    def get_prompt(self, user_id):
        state = self.states.get(user_id, "start")

        if state == "start" or state == "restart" or state == "back":
            return {
                "message": "What do you want to do?",
                "options": ["Available jobs", "Available Services", "Explore courses", "About HireNy"]
            }

        elif state == "Available jobs":
            job_titles = [c["jobTitle"] for c in self.data.get("Jobs", [])]
            return {
                "message": "Here are the Available Jobs:",
                "options": job_titles + ["Back"]
            }


        elif state == "Available Services":

            services = [s["serviceTitle"] for s in self.data.get("Services", [])]
            return {
                "message": "Here are the Available Services:",
                "options": services + ["Back"]
            }


        elif state == "Explore courses":
            courses = [c["title"] for c in self.data.get("Courses", [])]
            return {
                "message": "Here are the platform courses:",
                "options": courses + ["Back"]
            }
        elif state == "About HireNy":
            return {
                "message": AboutHireNy,
                "options": ["Back"]
            }

        return {"message": "Invalid state.", "options": ["Restart"]}

    def handle_input(self, user_id, user_input):
        state = self.states.get(user_id, "start")

        # Main menu navigation
        if state == "start":
            if user_input in ["Available jobs", "Available Services", "Explore courses", "About HireNy"]:
                self.states[user_id] = user_input
                return self.get_prompt(user_id)

            else:
                return {"message": "Please choose one of the listed options.", "options": ["Back"]}

        # Sub-menu states
        elif state == "Available jobs":
            if user_input.lower() == "back":
                self.states[user_id] = "start"
                return self.get_prompt(user_id)

            # find the job object by title
            for job in self.data.get("Jobs", []):
                if job["jobTitle"] == user_input:
                    return {
                        "message": f"You selected job: {job['jobTitle']} (ID: {job['id']})",
                        "options": ["Back"]
                    }

            return {"message": "Invalid job selected.", "options": ["Back"]}

        elif state == "Available Services":
            if user_input.lower() == "back":
                self.states[user_id] = "start"
                return self.get_prompt(user_id)

            for service in self.data.get("Services", []):
                if service["serviceTitle"] == user_input:
                    return {
                        "message": f"You selected service: {service['serviceTitle']} (ID: {service['id']})",
                        "options": ["Back"]
                    }

            return {"message": "Invalid service selected.", "options": ["Back"]}


        elif state == "Explore courses":

            if user_input.lower() == "back":
                self.states[user_id] = "start"

                return self.get_prompt(user_id)
            # find the course by title
            for course in self.data.get("Courses", []):

                if course["title"] == user_input:
                    return {
                        "message": f"Course: {course['title']}\nInstructor: {course['instructor']}\nCategory: {', '.join(course['category'])}\nPrice: {course['priceType']} {course['priceAmount']} {course['currency']}",
                        "options": ["Back"]

                    }

            return {"message": "Invalid course selected.", "options": ["Back"]}



        elif state in ["About HireNy"]:
            if user_input.lower() == "back":
                self.states[user_id] = "start"
                return self.get_prompt(user_id)
            else:
                return {
                    "message": f"You selected: {user_input}. (In a real system, data would be fetched here.)",
                    "options": ["Back"]
                }

        return {"message": "I didn't understand that. Returning to main menu.", "options": ["Back to main"]}





