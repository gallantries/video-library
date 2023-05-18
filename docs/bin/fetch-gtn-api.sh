#!/bin/bash
out=$(mktemp -d)
cli=""
for topic in $(curl https://training.galaxyproject.org/training-material/api/topics.json | jq .[].name -r); do
	cli="$cli https://training.galaxyproject.org/training-material/api/topics/$topic.json -o ${out}/gtn_${topic}.json"
done;
curl --parallel $cli

python3 bin/objectives.py "${out}"/gtn*.json
