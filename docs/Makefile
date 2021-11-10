build:
	ruby bin/yaml2json.rb < api/swagger.yaml > api/swagger.json
	JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter --trace
