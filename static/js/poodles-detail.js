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
  },
  mounted: function(){
  
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
