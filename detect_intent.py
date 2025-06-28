
def detect_intent(user_input):
    user_input = user_input.lower()

    if "apply" in user_input and "job" in user_input:
        return "apply_for_job"
    elif "profile" in user_input and ("create" in user_input or "register" in user_input):
        return "create_profile"
    elif "enroll" in user_input and "course" in user_input:
        return "enroll_in_course"
    elif "cv" in user_input or "resume" in user_input or "cover letter" in user_input:
        return "create_cv"
    elif "salary" in user_input and "insight" in user_input:
        return "salary_insights"
    elif "calendar" in user_input:
        return "view_calendar"
    elif "application" in user_input and "view" in user_input:
        return "view_applications"
    elif "assessment" in user_input and "take" in user_input:
        return "take_assessment"
    elif "course" in user_input and "explore" in user_input:
        return "explore_courses"
    elif "candidate" in user_input and "filter" in user_input:
        return "filter_candidates"
    elif "post" in user_input and "create" in user_input:
        return "create_post"
    elif "interview" in user_input and "set" in user_input:
        return "set_interview_time"
    elif "assessment" in user_input and "create" in user_input:
        return "create_assessment"
    else:
        return None
