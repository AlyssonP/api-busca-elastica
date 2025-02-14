from dotenv import load_dotenv
import os

if(os.environ.get("env")==None):
    load_dotenv(".env.development")
else:
    load_dotenv(".env.production")

URL_SOLR=str(os.getenv("URL_SOLR"))