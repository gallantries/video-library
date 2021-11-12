build: api/swagger.json
	JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter --trace

api/swagger.json: api/swagger.yaml
	ruby bin/yaml2json.rb < api/swagger.yaml > api/swagger.json
