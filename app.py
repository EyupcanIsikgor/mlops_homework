"""
Ana Flask uygulaması - MLOps Homework
"""

from flask import Flask

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint - Smoke test için kullanılır.
    """
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

