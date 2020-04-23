var app = new Vue({
  el: "#detail",
  delimiters: ['{$', '$}'],
  data: {
    slide: 0,
    sliding: null,
    poodle: {},
    document: {
      'path': null,
      'title': null,
      'description': null,
      'doc_type': null,
    },
    image: {
      'path': null,
      'title': null,
      'description': null,
    }
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
    getPoodle: function(slug){
     var self = this;
     var url = CONFIG['url_item'];
     url += slug + '/'
     axios.get(url)
     .then(function (response) {
      console.log(response);
      self.poodle = response.data;

    })
     .catch(function (error) {
      console.log(error);
    });
   },
   getModal: function(slug){
    this.getPoodle(slug)
    this.$bvModal.show(CONFIG['edit_modal'])
  },
  closeModal: function(id){
    this.poodle = {};
    this.$bvModal.hide(id);
  },
  confirmDelete: function(slug){
    this.getPoodle(slug);
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
    this.poodle = {};
    window.location.assign('/poodles/');
  });
 },
}
});
