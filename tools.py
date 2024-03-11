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