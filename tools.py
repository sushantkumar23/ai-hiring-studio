# tools.py


job_description_tools = [
    {
        "type": "function",
        "function": {
            "name": "get_job_description_data",
            "description": "Parse the job description",
            "parameters": {
                "type": "object",
                "properties": {
                    "job_title": {
                        "type": "string",
                        "description": "The job title"
                    },
                    "location": {
                        "type": "string",
                        "description": "The location"
                    },
                    "industry": {
                        "type": "string",
                        "description": "The industry/domain"
                    },
                    "education_degree": {
                        "type": "string",
                        "description": "The education degree"
                    },
                    "technical_skills": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "description": "The technical skills required"

                        },
                        "description": "The technical skills"
                    }
                },
                "required": ["job_title", "industry", "education_degree", "technical_skills"]
            }
        }

    }
]

resume_tools = [
    {
        "type": "function",
        "function": {
            "name": "get_resume_data",
            "description": "Parse the resume",
            "parameters": {
                "type": "object",
                "properties": {
                    "candidate_name": {
                        "type": "string",
                        "description": "The candidate's name"
                    },
                    "email": {
                        "type": "string",
                        "description": "The candidate's email"
                    },
                    "phone": {
                        "type": "string",
                        "description": "The candidate's phone number"
                    },
                    "location": {
                        "type": "string",
                        "description": "The location"
                    },
                    "industry": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "description": "The industry/domain"
                        },
                        "description": "The industries/domains"
                    },
                    "education_degree": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "description": "The education degree"
                        },
                        "description": "The education degrees"
                    },
                    "skills": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "description": "The skills"
                        },
                        "description": "The skills"
                    }
                },
                "required": ["candidate_name", "location", "industry", "education_degree", "skills"]
            }
        }
    }
]
