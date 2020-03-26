var app = new Vue({
  el: "#list",
  delimiters: ['{$', '$}'],
  data: {
    item: {},
    sex_select: [],
    color_select: [],
    person_owner_select: [],
    person_breeder_select: [],
    poodle_sire_select: [],
    poodle_dam_select: [],
  },
  mounted: function(){
    if('sex' in CONFIG['selects']){
      this.sex_select = CONFIG['selects']['sex'];
    }
    if('color' in CONFIG['selects']){
      this.color_select = CONFIG['selects']['color'];
    }
    if('person_owner' in CONFIG['selects']){
      this.person_owner_select = CONFIG['selects']['person_owner'];
    }
    if('person_breeder' in CONFIG['selects']){
      this.person_breeder_select = CONFIG['selects']['person_breeder'];
    }
    if('poodle_sire' in CONFIG['selects']){
      this.poodle_sire_select = CONFIG['selects']['poodle_sire'];
    }
    if('poodle_dam' in CONFIG['selects']){
      this.poodle_dam_select = CONFIG['selects']['poodle_dam'];
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
  showModal(r) {
    this.$bvModal.show(r)
  },
  hideModal(r) {
    this.$bvModal.hide(r)
  },
  getModal: function(slug){
    this.getData(slug);
    this.showModal(CONFIG['edit_modal']);
  },
  closeModal: function(r){
    this.item = {};
    this.$refs[r].hide()
  },
  confirmDelete: function(slug){
    this.getData(slug);    
    this.showModal(CONFIG['delete_modal']);  
  },
  realDelete: function(slug){
   var self = this;
   var id = CONFIG['delete_modal'];
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
  });
 },
}
});
