import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model="llama-3.1-8b-instant")

    def extract_jobs(self, cleaned_text):  # ⬅️ 4 spaces indentation
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing
            following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={'page_data': cleaned_text})
        try:
            jobs_parser = JsonOutputParser()
            res = jobs_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big, Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):  # ⬅️ 4 spaces indentation
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Huzaifa, a web developer at Web Marketing Solutions. Web Marketing Solutions is a dynamic company 
            specializing in web development and digital marketing services. We help businesses establish a strong online
            presence through modern, responsive websites, user-friendly designs, and optimized digital strategies. 
            Our team combines technical expertise with creative solutions to deliver tailored services in 
            website development, search engine optimization (SEO), social media marketing, content creation, and 
            online advertising. At Web Marketing Solutions, we are committed to driving growth for our clients by 
            transforming their digital vision into impactful results.
            Also, add the most relevant ones from the following links to showcase Web Marketing's portfolio: {link_list}
            Remember, you are Huzaifa, Web Developer at Web Marketing Solutions. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content