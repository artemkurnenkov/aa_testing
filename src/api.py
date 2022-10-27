import logging

from flask import Flask, request
from main import sum_for_api, hello

app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

logger_handler = logging.FileHandler(filename="./test_api_log.log", mode="w")
logger.addHandler(logger_handler)
logger_handler.setFormatter(logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s"))


@app.route('/hello', methods=["GET"])
def get_hello():
    logger.info("Return Hello!")
    return hello()


@app.route('/calc', methods=["GET"])
def calc():
    try:
        a = request.args.get('a')
        b = request.args.get('b')

        logger.info("Start calcucation!")

        res = "{0}+{1}={2}".format(a, b, sum_for_api(int(a), int(b)))

    except:
        logger.exception("Error occurred", exc_info=True)
    
    else:
        logger.info("Сalculation done without wrong!")

        return res
    
    finally:
        logger.info("End endpoint /calc")



if __name__ == "__main__":
    app.run()
