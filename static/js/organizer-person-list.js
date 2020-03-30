var app = new Vue({
  el: "#list",
  delimiters: ['{$', '$}'],
  data: {
    newKennel: false,
    person: {},
    kennel: {},
    kennels_select: [],
    states_select: [],
    countries_select: [],
  },
  mounted: function(){
    if('kennels' in CONFIG['selects']){
      this.kennels_select = CONFIG['selects']['kennels'];
    }
    if('states' in CONFIG['selects']){
      this.states_select = CONFIG['selects']['states'];
    }
    if('countries' in CONFIG['selects']){
      this.countries_select = CONFIG['selects']['countries'];
    }
  },
  methods: {   
    newKennelModal: function(){
      this.$bvModal.show(CONFIG['kennel_modal']);
    },
    getPerson: function(slug){
     var self = this;
     var url = CONFIG['url_person'];
     url += slug + '/'
     axios.get(url)
     .then(function (response) {
      self.person = response.data;
    })
     .catch(function (error) {
      console.log(error);
    });

   },
   submitKennel: function(slug) {
    var self = this;
    var url = CONFIG['url_kennel'];

    axios.post(url, self.kennel)
    .then(function (response) {
      console.log(response.data);
    })
    .catch(function (error) {
      console.log(error);
    });
    window.location.reload();
  },
  submitNewPerson: function(slug) {
    var self = this;
    var url = CONFIG['url_person'];

    axios.post(url, self.person)
    .then(function (response) {
      console.log(response.data);
    })
    .catch(function (error) {
      console.log(error);
    });
    window.location.reload();
  },
  submitPerson: function(slug) {
    var self = this;
    var url = CONFIG['url_person'];
    url += slug + '/'
    axios.put(url, self.person)
    .then(function (response) {
      console.log(response.data);
    })
    .catch(function (error) {
      console.log(error);
    });
    window.location.reload();
  },
  getModal: function(slug){
    this.getPerson(slug);
    this.$bvModal.show(CONFIG['edit_modal']);
  },
  closeModal: function(id){
    this.person = {};
    this.$bvModal.hide(id);
  },
  confirmDelete: function(slug){
    this.getPerson(slug);
    this.$bvModal.show(CONFIG['delete_modal']);      
  },
  realDelete: function(slug){
   var self = this;
   var id = CONFIG['delete_modal'];
   var url = CONFIG['url_person'];
   url += slug + '/'
   axios.delete(url)
   .then(function (response) {
   })
   .catch(function (error) {
    console.log(error);
  })
   .then(function () {
    this.person = {};
    window.location.reload();
  });
 },
}
});
