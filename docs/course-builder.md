---
layout: default
wide: true
---

# Course Builder

<style type="text/css">
.a {
    padding-left: 0;
    margin-left: 0;
    list-style: none;
}
.b {
	margin-bottom: 0.3em;
}
.b li:hover {
	background-color: #ccc
}

.c {
	overflow-y: scroll;
	max-height: 700px;
}
</style>

<div id="app" class="row">
	<div id="settings" class="row">
		<div>
			<!--
			<div class="row g-3 align-items-center">
				<div class="col-md-2 text-end">
					<label for="i-schedule" class="col-form-label">Daily Schedule</label>
				</div>
				<div class="col-md-3">
					<input type="checkbox" id="i-schedule" class="form-check-input" aria-describedby="i-schedule-help" checked>
				</div>
				<div class="col-md-6">
					<span id="i-schedule-help" class="form-text">
						If selected a daily schedule will be generated
					</span>
				</div>
			</div>
			-->
			<div class="row g-3 align-items-center">
				<div class="col-md-2 text-end">
					<label for="i-start-time" class="col-form-label">Daily Start Time</label>
				</div>
				<div class="col-md-3">
					<input type="time" id="i-start-time" class="form-control" aria-describedby="i-start-time-help" value="10:00" onchange="rerenderSchedule()">
				</div>
				<div class="col-md-6">
					<span id="i-start-time-help" class="form-text">
						When does the course start each day
					</span>
				</div>
			</div>
			<div class="row g-3 align-items-center">
				<div class="col-md-2 text-end">
					<label for="i-lunch-time" class="col-form-label">When is lunch?</label>
				</div>
				<div class="col-md-3">
					<input type="time" id="i-lunch-time" class="form-control" aria-describedby="i-lunch-time-help" value="13:00" onchange="rerenderSchedule()">
				</div>
				<div class="col-md-6">
					<span id="i-lunch-time-help" class="form-text">
						Daily lunch time
					</span>
				</div>
			</div>
			<div class="row g-3 align-items-center">
				<div class="col-md-2 text-end">
					<label for="i-end-time" class="col-form-label">Daily End Time</label>
				</div>
				<div class="col-md-3">
					<input type="time" id="i-end-time" class="form-control" aria-describedby="i-end-time-help" value="16:00" onchange="rerenderSchedule()">
				</div>
				<div class="col-md-6">
					<span id="i-end-time-help" class="form-text">
						When does the course end each day
					</span>
				</div>
			</div>
		</div>
	</div>
	<div class="row mt-5">
		<div id="library" class="col-md-3">
			<h3>Library</h3>
			<div class="c">
			{% for tag in site.data['by_tags'] %}
				<div><b>{{ tag[0] }}</b></div>
				<div>
					<ul class="list-group a">
						{% for video in tag[1]['videos'] %}
						{% assign x = video[0] | split:'/' %}
						{% assign versions = video[1]['versions'] %}
						{% assign version_count = versions | size %}

							<!-- TODO: Some modules have no video, thus no time. {{ version_count }} -->
							{% if version_count > 0 %}
							<a class="b library_{{ video[0] | replace: '/','_' }}" onclick="updateBasket('{{video[0]}}')"><li class="list-group-item">{{ x[1] }}{% if x[2] %}/{{ x[2] }}{% endif %}</li></a>
							{% endif %}
						{% endfor %}
					</ul>
				</div>
			{% endfor %}
			</div>
		</div>
		<div class="col-md-9">
			<ul class="nav nav-tabs" id="myTab" role="tablist">
				<li class="nav-item" role="presentation">
					<button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#home" type="button" role="tab" aria-controls="home" aria-selected="true">Schedule</button>
				</li>
				<li class="nav-item" role="presentation">
					<button class="nav-link" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile" type="button" role="tab" aria-controls="profile" aria-selected="false">Gallantries Workshop Markdown</button>
				</li>
			</ul>
			<div class="tab-content" id="myTabContent">
				<div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
					<div id="schedule"></div>
				</div>
				<div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
					<div id="schedule-markdown"></div>
				</div>
			</div>
		</div>
	</div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js" integrity="sha512-894YE6QWD5I59HgZOGReFYm4dnWc1Qt5NtvYSaNcOP+u1T9qYdvdihz0PPSiiqn/+/3e7Jo4EaG7TubfWGUrMQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

<script type="text/javascript">
var data = {{ site.data['videos'] | jsonify }};
var basket = [];

function updateBasket(id){
	if(basket.indexOf(id) === -1){
		$(`.library_${id.replaceAll("/", "_")} li`).addClass("active")
		basket.push(id);
		$("#basket").append(`<li>${id}</li>`)
	} else {
		basket = basket.filter(x => { return id !== x})
		$(`.library_${id.replaceAll("/", "_")} li`).removeClass("active")
	}

	rerenderSchedule();
}

function calculateDuration(t){
	d = 0;
	h = t.split(/[Hh]/)
	if(h.length === 2){
		// hours
		d += 3600 * parseInt(h[0])
		h = h[1]
	} else { h = h[0] }

	m = h.split(/[Mm]/)
	if(m.length === 2){
		// minutes
		d += 60 * parseInt(m[0])
		m = m[1]
	} else { m = m[0] }

	s = m.split(/[Ss]/)
	if(m.length === 2){
		// minutes
		d += parseInt(m[0])
		m = m[1]
	} else { m = m[0] }

	r = Math.ceil(d / 60 / 15) * 15
	return r;
}

function humanToMinutes(human){
	return eval(human.replace(":", " * 60 + "))
}

function minutesToHuman(minutes){
    h = Math.floor(minutes/ 60);
    m = minutes % 60;
    return `${h}:${String(m).padStart(2, '0')}`
}

function rerenderSchedule(){

	var dayStartMinutes = humanToMinutes($("#i-start-time").val()),
		dayEndMinutes = humanToMinutes($("#i-end-time").val()),
		dayLunchMinutes = humanToMinutes($("#i-lunch-time").val()),
		minutesInDay = dayEndMinutes - dayStartMinutes,
		breakLength = 20,
		timeUntilLunch = dayLunchMinutes - dayStartMinutes;

	var day = 0,
		days = {};
	// Given a basket, lay them out.

	basket.forEach(x => {
		// Get the length of one of the copies.
		time = data[x].versions[0].length
		duration = calculateDuration(time)
		console.log(x, duration)

		// Setup the day if it isn't yet
		if(days[day] === undefined){
			days[day] = {
				schedule: [],
				currentTime: dayStartMinutes,
				timeSinceLastBreak: 0,
			}
		}

		ttl = dayLunchMinutes - days[day].currentTime;

		if(days[day].currentTime + duration - dayStartMinutes > minutesInDay){
			// Move to tomorrow
			day += 1;
			days[day] = {
				schedule: [],
				currentTime: dayStartMinutes,
				timeSinceLastBreak: 0,
			}
			days[day].schedule.push({
				title: x,
				code: x,
				start: days[day].currentTime,
				end:  days[day].currentTime + duration,
			});
			days[day].currentTime += duration;
			days[day].timeSinceLastBreak += duration;
		} else {
			// Decide if we should take a break, and if there's enough time
			// until lunch add it. Otherwise push through.
			if(days[day].timeSinceLastBreak > 60 && ttl > 60){
				// Insert a break
				days[day].schedule.push({
					title: `${breakLength} minute break`,
					start: days[day].currentTime,
					end:  days[day].currentTime + breakLength,
				});
				days[day].currentTime += breakLength;
				days[day].timeSinceLastBreak = 0 ;
			}

			// If it's almost lunch, just finish early.
			if(ttl > 0 && ttl < 15){
				// Insert Lunch
				days[day].schedule.push({
					title: `Lunch!`,
					start: days[day].currentTime,
					end:  days[day].currentTime + 60 + ttl,
				});
				days[day].currentTime += 60 + ttl;
				days[day].timeSinceLastBreak = 0 ;
			}

			// Otherwise check if adding this would affect lunch
			var cs = days[day].currentTime,
				ce = days[day].currentTime + duration;
			// Does lunch start during this lecture
			if(cs < dayLunchMinutes && dayLunchMinutes < ce){
				// Split it
				days[day].schedule.push({
					title: x + ' | Part 1',
					code: x,
					start: days[day].currentTime,
					end:  days[day].currentTime + ttl,
				});
				days[day].currentTime += ttl;
				days[day].timeSinceLastBreak += ttl;

				// Insert Lunch
				days[day].schedule.push({
					title: `Lunch!`,
					start: days[day].currentTime,
					end:  days[day].currentTime + 60 + ttl,
				});
				days[day].currentTime += 60;
				days[day].timeSinceLastBreak = 0 ;

				// Split it
				days[day].schedule.push({
					title: x + ' | Part 2',
					start: days[day].currentTime,
					end:  days[day].currentTime + (duration - ttl),
				});
				days[day].currentTime += (duration - ttl);
				days[day].timeSinceLastBreak += (duration - ttl);

			} else {
				days[day].schedule.push({
					title: x,
					code: x,
					start: days[day].currentTime,
					end:  days[day].currentTime + duration,
				});
				days[day].currentTime += duration;
				days[day].timeSinceLastBreak += duration;
			}

		}


	})

	var updated = "";
	Object.keys(days).forEach(day => {
		updated += `<h4>Day ${parseInt(day) + 1}</h4>`;
		updated += "<table class=\"table table-striped\">"
		updated += days[day].schedule.map(item => {
			return `<tr>
				<td>${minutesToHuman(item.start)}</td>
				<td>${minutesToHuman(item.end)}</td>
				<td>${item.title}</td>
			</tr>`
		}).join("")
		updated += "</table>"
	})
	$("#schedule").html(updated)

	var markdown = `---
layout: event
title: "My Awesome Event"
description: "Best training since sliced bread lessons"

program:
`;

	Object.keys(days).forEach(day => {
		markdown += `  day${parseInt(day) + 1}\n`;
		markdown += `    title: "Day ${parseInt(day) + 1}"\n`;
		markdown += `    description: "Some description about today's content"\n`;
		markdown += `    trainings:\n`;

		days[day].schedule.forEach(item => {
			if(item.code){
				markdown += `      - session: ${item.code}\n`;
			}
		})
	})

	markdown += `---\n\nYou can write a bit more about your course here!\n`;
	$("#schedule-markdown").html("<pre>" + markdown + "</pre>")
}
</script>
