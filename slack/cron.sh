#!/bin/bash
# We have a directory of messages with timestamps.
# If they have not been sent and time > their time, we send them.
# Once sent, we document this in a logfile.
NOW=$(date +%s)

process_folder(){
	folder="$1"
	slack_url="$2"

	count=$(find scheduled/$1 -type f -name '*.json' | wc -l)
	if (( count > 0 )); then
		for fn in scheduled/$1/*.json; do
			ds=$(echo "$fn" | sed "s|scheduled/$folder/||g" | cut -c1-25)
			ts=$(date -d "$ds" +%s)
			if (( ts < NOW )); then
				# Send the message
				echo "$fn has not been sent"
				if [[ "$slack_url" != "" ]]; then
					response=$(curl --silent -X POST -H 'Content-type: application/json' --data "@$fn" "${slack_url}")
					# If it was received OK
					if [[ "$response" == "ok" ]]; then
						mv "$fn" "sent/$1/"
					else
						echo "$response"
						exit 1
					fi
				else
					echo mv "$fn" "sent/$1/"
				fi
			fi
		done
	fi
}

process_folder announce       "$SLACK_API_ANNOUNCEMENTS"
process_folder event-gat      "$SLACK_API_GAT"
#process_folder gtn/instructors    "$SLACK_API_INSTRUCTORS"
#process_folder gtn/admins         "$SLACK_API_ADMINS"
#process_folder gtn/admin-training "$SLACK_API_ADMIN_TRANING"
#process_folder gtn/social         "$SLACK_API_SOCIAL"
