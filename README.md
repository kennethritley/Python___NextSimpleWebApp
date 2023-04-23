# Project Title

This is a more sophisticated Flask application. It demonstrates how you can
handle both PUT and GET requests.

## Table of Contents

- [Installation](#installation)
- [Authors](#authors)
- [License](#license)
- [CHANGELOG.md](CHANGELOG.md)


## Changelog

For a detailed list of changes and version history, please refer to the [CHANGELOG.md](CHANGELOG.md) file.

## Installation

No installation necessary. When the app runs it starts the Flask server that
listens to localhost:5000.  It should accept:

- http://127.0.0.1:5000 - Hello World
- http://127.0.0.1:5000/cat - Display the cat's name (GET)
- curl -X POST -F "name=Whiskers" http://127.0.0.1:5000/cat - To change the cat's name (PUT)


## Authors

Your friendly, neighborhood Dr. Ken

## License

Never operate a motor vehicle without the proper license.