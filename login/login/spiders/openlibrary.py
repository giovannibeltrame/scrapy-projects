import scrapy
import base64
from scrapy import FormRequest
from scrapy.utils.project import get_project_settings

class OpenlibrarySpider(scrapy.Spider):
    name = "openlibrary"
    allowed_domains = ["openlibrary.org"]
    start_urls = ["https://openlibrary.org/account/login"]

    def parse(self, response):
        settings = get_project_settings()
        yield FormRequest.from_response(response, formid="register", formdata={
            "username": settings.get("OPEN_LIBRARY_USERNAME"),
            "password": base64.b64decode(settings.get("OPEN_LIBRARY_PASSWORD")).decode("utf-8"),
            "redirect": "/",
            "debug_token": "",
            "login": "Log In"
        },
        callback=self.after_login)

    def after_login(self, response):
        print("logged in...")