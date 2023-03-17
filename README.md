# WorkRamp Challenge
This projects was built using Python, Pytest and Playwrigth to run two simple tests over a page. It was implemented following POM design pattern, and the structure is simply enough to get the tests running.

## Prerequisites
You must have locally installed Python 3.9+ (This project was built using Python@3.11.2)

## Install Instructions
1. Clone this git repository
```bash
$ git clone https://github.com/henry-sg/workramp_challenge.git
$ cd workramp_challenge
```
2. Create a new virtual environment
```bash
$ python3 -m venv venv
```
3. Activate the virtual environment
```bash
$ source venv/bin/activate
```
4. Install dependencies
```bash
$ pip install -r requirements.txt
```
5. Install browsers to use with Playwright
```bash
$ playwright install
```

## Files Structure
- models: contains base data modeles, used to represent users, guides and tasks
- pages: page of models for the pages used or interated with in the tests
- tests: tests cases

## Running Tests

Before running the tests you must create a file called .env in the root directory of the project. This file will contain the information to handle user authentication. You can just rename the file example.env to .env and modify it with correct credentials
```bash
mv example.env .env
```

To run all tests simply execute:
```bash
$ pytest -s tests --headed --slowmo 1000
```
This will launch the browser and run it on slow motion (1 second after each Playwright action). If you want to run it faster remover --slowmo 1000 parameter or if you want to runint on headless mode (without launching a browser) remove --headed

To run a specific test execute:
```bash
$ pytest -s tests/test_login.py --headed --slowmo 1000
```
```bash
$ pytest -s tests/test_guide.py --headed --slowmo 1000
```