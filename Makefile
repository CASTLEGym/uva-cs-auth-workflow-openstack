
check: *.py Makefile
	python3 -m flake8 *.py

format: *.py Makefile
	python3 -m autopep8 -i *.py

requirements.txt: *.py Makefile
	pipreqs --force .

clean:
	rm -rf output.json setup-output.json logins.json logins-ouptut.json



