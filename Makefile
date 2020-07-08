all: test clean

test:
	python3 -m unittest tests/*.py

clean:
	find . -name "*.pyc" -delete
	