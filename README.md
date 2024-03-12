# LLM Hiring System

A novel hiring system that uses state of the art NLP technologies such as LLM to help efficiently match and rank candidates to job postings. The system is designed to help hiring managers and recruiters to quickly and efficiently match candidates to job postings.

<img width="999" alt="Screenshot 2024-03-12 at 11 16 32 AM" src="https://github.com/sushantkumar23/llm-hiring-system/assets/4726333/0532aeb2-183e-4442-8756-a843326af881">


## Installation and Usage

The LLM hiring system is a FastAPI application that can be installed and run using the following commands:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Components

The LLM hiring systems consists of the following components:

1. Job Description Parser
2. Candidate Resume Parser
3. Similarity Score Calculator
4. Matching Engine

### Job Description Parser

The job description parser is responsible for parsing the job description and extracting the relevant information such as the job title, job description, and the required skills. The job description parser is implemented in the `job_description_parser.py` file.

### Candidate Resume Parser

The candidate resume parser is responsible for parsing the candidate resume and extracting the relevant information such as the candidate's name, contact information, and the candidate's skills. The candidate resume parser is implemented in the `candidate_resume_parser.py` file.

### Similarity Score Calculator

The similarity score calculator is responsible for calculating the similarity score between the candidate's skills and the job description. The similarity score calculator is implemented in the `similarity_score.py` file.

### Matching Engine

The matching engine is responsible for matching the candidate's skills to the job description and ranking the candidates based on the match. The matching engine is implemented in the `matching_engine.py` file.

## Pydantic Models

The `pydantic` models are used to validate the input data and to serialize the output data. The models are defined in the `models.py` file.

1. JobDescription
2. Resume

## LLM: OpenAI

An `OPENAI_API_KEY` is required to use the LLM model. The OPENAI_API_KEY can be obtained from the OpenAI website. The OPENAI_API_KEY should be set as an environment variable with the name `OPENAI_API_KEY`.

The LLM Model is easily configurable and can be changed from the `config.py` file. Some of the valid instuct models that can be used are `gpt-3.5-turbo`, `gpt-4-0125-preview`, `gpt-4-1106-preview`.

Best performance is achieved with the 'gpt-4-0125-preview' model
Cost effective performance is achieved with the 'gpt-3.5-turbo' model

## Testing

The pytest framework is used for testing the LLM hiring system. The tests are implemented in the `tests` folder for each of the components. The tests can be run using the following command:

```bash
pytest
```

## Deployment

Dockerfile is provided for easy deployment of the LLM hiring system along with a requirements.txt file with a containerized environment.

For quicker deployments, on managed services such as Vercel, the `vercel.json` file is provided for easy deployment.
