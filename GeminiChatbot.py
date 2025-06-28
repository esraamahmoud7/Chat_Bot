import google.generativeai as genai
import Sys_Data

# import detect_intent


class GeminiChatbot:
    def __init__(self, api_key,Token):
        genai.configure(api_key=api_key)
        self.Token = Token
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=f"""
                    You are an AI assistant inside the HireNy platform.
                    
                    You help job seekers and recruiters with:
                    - Job applications
                    - CV writing
                    - Interview scheduling
                    - Course recommendations
                    - Salary insights
                    
                    Use real-time data passed in the prompt if available. If not, rely on your general knowledge.
                    
                    If a user asks for private info (like application status), tell them to check their dashboard.
                    """
        )
        self.chat = self.model.start_chat(history=[])


    def get_response(self, user_input):
        prompt = f"""
            User asked: {user_input}
             and you can use this data if he asks
            System task flows to guide behavior:
            {Sys_Data.task_flows}
        
            Real-time system data (jobs, services, courses, user tech info):
            {Sys_Data.Data}
            and user tech info incase he wants to know how to improve his skills or the needed courses to improve
            """

        response = self.chat.send_message(prompt)
        return response.text