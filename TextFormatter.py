import re
# for output shape
class TextFormatter:
    @staticmethod
    def clean(text):
        text = re.sub(r"\n*\*?\*?(\d+)\. (.+?)\*?\*?", r"\n\n\1. \2", text)
        text = text.replace("**", "")
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = text.replace("Tip:", "💡 Tip:")
        return text.strip()

    def format_data_list_pretty(data_list, data_type="general"):
        """
        Formats data items like jobs, services, or courses into pretty bullet list text.
        :param data_list: list of dict items
        :param data_type: one of ["Jobs", "Services", "Courses"]
        :return: formatted string
        """

        if not isinstance(data_list, list) or not all(isinstance(item, dict) for item in data_list):
            return f"Error: Invalid {data_type} data format."

        if not data_list:
            return f"No {data_type.lower()} available."

        output = []

        for item in data_list:
            if data_type == "Jobs":
                output.append(
                    f"- {item.get('jobTitle', 'N/A')} at {item.get('companyName', 'N/A')} "
                    f"({item.get('city', 'N/A')}) — Salary: {item.get('minSalary', '0')} - {item.get('maxSalary', '0')} {item.get('currency', '')}"
                )

            elif data_type == "Services":
                output.append(
                    f"- {item.get('serviceTitle', 'N/A')} from {item.get('companyName', 'N/A')} "
                    f"({item.get('city', 'N/A')}) — Fee: {item.get('salary', '0')} {item.get('currency', '')}"
                )

            elif data_type == "Courses":
                category = ", ".join(item.get("category", [])) if isinstance(item.get("category"), list) else item.get(
                    "category", "")
                output.append(
                    f"- {item.get('title', 'N/A')} ({category}) — {item.get('priceType', 'N/A').capitalize()}"
                )

            else:
                output.append(str(item))  # fallback: raw

        return "\n".join(output)

    def format_tech_info(tech_info):
        """
        Formats the user's tech info (education, skills, certificates, etc.)
        :param tech_info: dict with keys like education, certificates, courses, skills, experience, languages
        :return: formatted string
        """
        if not isinstance(tech_info, dict):
            return "No user technical info available."

        output = []

        # Education
        education = tech_info.get("education", [])
        if education:
            output.append("Education:")
            for edu in education:
                output.append(
                    f"  - {edu.get('degree', 'N/A')} at {edu.get('institutionName', 'N/A')} "
                    f"({edu.get('fromDate', '')} to {edu.get('toDate', '')})"
                )

        # Certificates
        certs = tech_info.get("certificates", [])
        if certs:
            output.append("\nCertificates:")
            for cert in certs:
                output.append(
                    f"  - {cert.get('certificateName', 'N/A')} from {cert.get('institutionName', 'N/A')} "
                    f"(Issued: {cert.get('dateIssued', 'N/A')})"
                )

        # Completed Courses
        courses = tech_info.get("courses", [])
        if courses:
            output.append("\nCompleted Courses:")
            for course in courses:
                output.append(
                    f"  - {course.get('courseName', 'N/A')} from {course.get('institutionName', 'N/A')} "
                    f"(Completed: {course.get('dateCompleted', 'N/A')})"
                )

        # Skills
        skills = tech_info.get("skills", [])
        if skills:
            output.append("\nSkills:")
            skill_names = [s.get("skill", "N/A") for s in skills]
            output.append("  - " + ", ".join(skill_names))

        # Experience
        experience = tech_info.get("experience", [])
        if experience:
            output.append("\nExperience:")
            for exp in experience:
                output.append(
                    f"  - {exp.get('jobTitle', 'N/A')} at {exp.get('companyName', 'N/A')} "
                    f"({exp.get('fromDate', '')} to {exp.get('toDate', '')})"
                )

        # Languages
        langs = tech_info.get("languages", [])
        if langs:
            output.append("\nLanguages:")
            language_names = [l.get("language", "N/A") for l in langs]
            output.append("  - " + ", ".join(language_names))

        return "\n".join(output) if output else "No technical info available."
