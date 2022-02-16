for topic in $(curl https://training.galaxyproject.org/training-material/api/topics.json | jq .[].name -r); do
	curl https://training.galaxyproject.org/training-material/api/topics/$topic.json > _data/gtn_$topic.json;
done;

python bin/objectives.py
rm -f _data/gtn_*.json
