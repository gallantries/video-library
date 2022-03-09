# Slack Bot

Everything in the scheduled directory will be sent once, after the specific time. It's as easy as composing the json and dumping it in the folder.

## Editing the templates

1. Update the markdown templates in `templates/*.md`

## Rebuilding the scheduled messages

Run `templates/build.py` which will generate your messages:

```console
$ python templates/build.py 2022-03-14T09:00:00 --days 5 --course gtn scheduled/announce
$ python templates/build.py 2022-03-14T09:00:00 --days 5 --course gat scheduled/event-gat
```

And check the results in scheduled/

## Cron

There is a script, ./cron.py that is meant to run on cron. It will send messages which are older than "now" (so run it at 5 min past the hour?) and move them to a folder to make sure they aren't sent again.

```
5 * * * * cd /this/directory && python cron.py folder SLACK_URL="https://hooks.slack.com/services/T01.../B01.../uUK.."
```

