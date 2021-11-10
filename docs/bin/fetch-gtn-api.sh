for topic in $(curl https://training.galaxyproject.org/training-material/api/topics.json | jq .[].name -r); do
	curl https://training.galaxyproject.org/training-material/api/topics/$topic.json | \
		jq '.materials[] | ["/topics/" + .topic_name + "/tutorials/" + .tutorial_name, "\"" + .title + "\""] | @tsv' -r | \
		sed 's/\t/: /g' | sed 's/\/topics\///g' | sed 's/tutorials\///g' >> out.yaml
done;
