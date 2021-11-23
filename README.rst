Example of python proxy with change content
===========================================

This is a sample Python proxy that redirects a request to http://news.ycombinator.com, receives a response, processes the html <body> tag, and appends a Unicode (TM) character to each 6-character word.

Prerequisites
=============

`pip install --upgrade -r requirements.txt`

Usage
=====

In project directory run `python ./run.py` and then, for example, open in browser http://127.0.0.1:8002/item?id=13713480

Run tests
=========

`python -m unittest discover -s ./tests/`

Notes
=====

Target url http://news.ycombinator.com and proxy port 8002 are hardcoded in script.
