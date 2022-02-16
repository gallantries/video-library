#!/bin/bash
out=$(mktemp -d)
for topic in $(curl https://training.galaxyproject.org/training-material/api/topics.json | jq .[].name -r); do
	curl https://training.galaxyproject.org/training-material/api/topics/$topic.json > "${out}/gtn_${topic}.json";
done;

python3 bin/objectives.py "${out}"/gtn*.json
