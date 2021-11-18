build: api/swagger.json
	JEKYLL_ENV=production bundle exec jekyll build -d _site/video-library --strict_front_matter --trace

serve:
	jekyll serve -d _site/video-library --trace --strict_front_matter

api/swagger.json: api/swagger.yaml
	ruby bin/yaml2json.rb < api/swagger.yaml > api/swagger.json

check-html-internal:
	htmlproofer \
		--assume-extension \
		--http-status-ignore 405,503,999 \
		--disable-external \
		--allow-hash-href \
		./_site

check-html:
	htmlproofer \
		--assume-extension \
		--http-status-ignore 405,503,999 \
		--allow-hash-href \
		./_site

clean:
	rm -rf _site .jekyll-cache
