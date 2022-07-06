build: api/swagger.json
	JEKYLL_ENV=production bundle exec jekyll build -d _site/video-library --strict_front_matter --trace

serve:
	jekyll serve -d _site/video-library --trace --strict_front_matter

api/swagger.json: api/swagger.yaml
	ruby bin/yaml2json.rb < api/swagger.yaml > api/swagger.json

check-html-internal:
	bundle exec htmlproofer \
		--assume-extension \
		--http-status-ignore 405,503,999 \
		--disable-external \
		--empty-alt-ignore \
		--allow-hash-href \
		./_site

check-html:
	bundle exec htmlproofer \
		--assume-extension \
		--http-status-ignore 405,503,999 \
		--allow-hash-href \
		--ignore_missing_alt \
		./_site

test: #build check-html-internal
	bundle exec ruby bin/validate-frontmatter.rb
	bundle exec ruby bin/validate-video-schema.rb
	bundle exec ruby bin/validate-instructors.rb


clean:
	rm -rf _site .jekyll-cache
