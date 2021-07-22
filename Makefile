init:
	python3 -m venv venv

setup:
	pip install -r requirements.txt

run:
	python3 template_app/basic.py

end:
	deactivate
