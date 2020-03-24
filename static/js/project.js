var app = new Vue({
  el: "#maincontent",
  delimiters: ['{$', '$}'],
  data: {
    slide: 0,
    sliding: null,
    item: {},
    states_select: [],
    countries_select: [],
    kennels_select: [],
  },
  mounted: function(){
    if('states' in CONFIG['selects']){
      this.states_select = CONFIG['selects']['states'];
    }
    if('countries' in CONFIG['selects']){
      this.countries_select = CONFIG['selects']['countries'];
    }
    if('kennels' in CONFIG['selects']){
      this.kennels_select = CONFIG['selects']['kennels'];
    }
  },
  methods: {   
   onSlideStart(slide) {
    this.sliding = true
  },
  onSlideEnd(slide) {
    this.sliding = false
  },
  getData: function(slug){
   var self = this;
   var url = CONFIG['url_item'];
   url += slug + '/'
   axios.get(url)
   .then(function (response) {
    console.log(response);
    self.item = response.data;

  })
   .catch(function (error) {
    console.log(error);
  });
 },
 getModal: function(slug){
  this.getData(slug)
  this.$bvModal.show(CONFIG['edit_modal'])
},
closeModal: function(){
  this.item = {};
  this.$bvModal.hide(CONFIG['edit_modal']);
},
confirmDelete: function(slug){
  this.getData(slug);
  this.$bvModal.show(CONFIG['delete_modal']);      
},
realDelete: function(slug){
 var self = this;
 var id = CONFIG['delete_modal'];
 var url = CONFIG['url_item'];
 url += slug + '/'
 axios.delete(url)
 .then(function (response) {
  console.log(response);
})
 .catch(function (error) {
  console.log(error);
})
 .then(function () {
  this.item = {};
  window.location.reload();
});
},
}
});
