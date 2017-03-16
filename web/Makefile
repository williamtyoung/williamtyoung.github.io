.PHONY: dev html github 
THEME=hugo-theme-minos
MSG=rebuilt site on `date`

dev:
	hugo server --theme=$(THEME) --watch

html:
	rm -rf public/
	hugo --theme=$(THEME)

github: html
	cp -r public/* ../
	git add -A
	git commit -m "${MSG}"
	git push
