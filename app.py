from flask import Flask
import sys
from housing.exception import HousingException
from housing.logger import logging
app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
    
    return """This is Machichne Learning Project
    and CI/CD pipeline has been established"""

if __name__ == '__main__':
    app.run(debug=True)