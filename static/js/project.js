var nav = new Vue({
  el: "#navbarSlot",
  data: {
    currentRoute: window.location.pathname
  },
  mounted: function() {
  },
  methods: {
    navBarActiveLink: function(link){
      var vueUrl = this.currentRoute.replace(/[/\s]/g, '');
      if(link == vueUrl){
        return 'active';
      }
    }
  }
});

window.addEventListener('popstate', () => {
  navVue.currentRoute = window.location.pathname
});

var app = new Vue({
  el: "#maincontent",
  delimiters: ['{$', '$}'],
  data: {
    kennel: {},
    states_select: [],
    countries_select: [],
  },
  mounted: function(){
    this.states_select = CONFIG['selects']['states'];
    this.countries_select = CONFIG['selects']['countries_select']
  },
  methods: {   
    getData: function(slug){
     var self = this;
     var url = CONFIG['url_item'];
     url += slug + '/'
     axios.get(url)
     .then(function (response) {
      console.log(response);
      self.kennel = response.data;

    })
     .catch(function (error) {
      console.log(error);
    });
   },
   getModal: function(slug){
    this.getData(slug)
    self.$bvModal.show(CONFIG['edit_modal'])
  },
  closeModal: function(){
    this.kennel = {};
    $bvModal.hide(CONFIG['edit_modal']);
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
    this.kennel = {};
    self.$bvModal.hide(CONFIG['delete_modal']);
  });
 },
}
});
