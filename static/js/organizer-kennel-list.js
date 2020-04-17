var app = new Vue({
  el: "#list",
  delimiters: ['{$', '$}'],
  data: {
    item: {},
    states_select: [],
    countries_select: [],
  },
  mounted: function(){
    if('states' in CONFIG['selects']){
      this.states_select = CONFIG['selects']['states'];
    }
    if('countries' in CONFIG['selects']){
      this.countries_select = CONFIG['selects']['countries'];
    }
  },
  methods: {   
    getData: function(slug){
     var self = this;
     var url = CONFIG['url_item'];
     url += slug + '/'
     axios.get(url)
     .then(function (response) {
      self.item = response.data;
    })
     .catch(function (error) {
      console.log(error);
    });

   },
   submitData: function(slug) {
    var self = this;
    var url = CONFIG['url_item'];
    url += slug + '/'
    axios.put(url, self.item)
    .then(function (response) {
      console.log(response.data);
    })
    .catch(function (error) {
      console.log(error);
    });
    window.location.reload();
  },
  getModal: function(slug){
    this.getData(slug);
    this.$bvModal.show(CONFIG['edit_modal']);
  },
  closeModal: function(id){
    this.item = {};
    this.$bvModal.hide(id);
  },
  confirmDelete: function(slug, people){
    this.getData(slug);
    this.people = people;    
    this.$bvModal.show(CONFIG['delete_modal']);      
  },
  realDelete: function(slug){
   var self = this;
   //remove fk in person records
   console.log(this.people);
   for o in this.people{
    
   }



   /*var id = CONFIG['delete_modal'];
   var url = CONFIG['url_item'];
   url += slug + '/'
   axios.delete(url)
   .then(function (response) {
   })
   .catch(function (error) {
    console.log(error);
  })
   .then(function () {
    this.item = {};
    window.location.reload();
  });*/
 },
}
});
