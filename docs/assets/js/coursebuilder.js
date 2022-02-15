//var app = new Vue({
	//el: '#app',
	//data () {
		//return {
			//videos: null,
		//video_ids: null
		//}
	//},
	//mounted () {
	//}
//})
new Vue({
	el: '#app',
	data() {
		return {
			library: null,
			categories: null,
			loading: true,
			errored: false,
			basket: [],
		};
	},
	methods: {
		addToBasket: function(video_id){
			if(this.basket.indexOf(video_id) == -1){
				this.basket.push(video_id)
			}
		},
		getVideosForSection: function(section){
			return this.library[section]
		},
	},
	mounted() {
		axios
			.get('/video-library/api/tags.json')
			.then(response => {
				this.library = response.data;
				this.categories = Object.keys(response.data);
			})
			.catch(error => {
				console.log(error)
				this.errored = true
			})
			.finally(() => this.loading = false)
	}
})

