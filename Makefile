develop:
	pip install -r requirements.txt

html:
	rm -rf html
	python -m sphinx site html
	python -m sphinx site html/instructor
	rm html/instructor/_static/student.css

.PHONY: html
