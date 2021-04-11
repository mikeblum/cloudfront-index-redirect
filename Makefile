.PHONY : clean lint test build

all : clean lint test build

clean :
	rm -rf __pycache__
	rm -f cloudfront-index-redirect.zip

lint :
	pipenv run black .

test :
	python3 -m unittest discover -s . -p "*_test.py" -v

build :	
	zip -9 cloudfront-index-redirect.zip lambda_function.py
