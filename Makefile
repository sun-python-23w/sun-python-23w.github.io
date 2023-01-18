develop:
	pip install -r requirements.txt

html:
	rm -rf html
	python -m sphinx site html
	python -m sphinx site html/instructor
	rm html/instructor/_static/student.css

.PHONY: html


# publish: html
# 	git branch -f gh-pages HEAD
# 	git checkout gh-pages

# 	touch html/.nojekyll

# 	git add --force html

# 	git commit -m "Publish"
# 	git push -f origin `git subtree split -P html`:refs/heads/gh-pages

# 	git checkout main
