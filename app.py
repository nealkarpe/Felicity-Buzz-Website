#!/usr/bin/env python
from app import app
from sys import argv as rd

def main():
	port = 3000
	try:
		port = int(rd[1])
	except:
		pass
	app.run(debug=True, host="127.0.0.1", port=port)


if __name__ == '__main__':
	main()