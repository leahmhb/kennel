var app = new Vue({
  el: "#detail",
  delimiters: ['{$', '$}'],
  data: {
    slide: 0,
    sliding: null,
    item: {},
    document: {
      'document': null,
      'title': null,
      'description': null,
      'doc_type': null,
    },
    image: null,
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
    onSlideStart(slide) {
      this.sliding = true
    },
    onSlideEnd(slide) {
      this.sliding = false
    },
    addDocument(poodle_id){
      this.document.poodle = poodle_id;
      this.$bvModal.show(CONFIG['document_modal']);
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
  closeModal: function(id){
    this.item = {};
    this.$bvModal.hide(id);
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
