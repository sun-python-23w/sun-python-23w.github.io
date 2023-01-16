develop:
	pip install -r requirements.txt

html: site/**/*  # All files inside site/
	rm -rf html
	python -m sphinx site html

clean:
	rm -rf html
