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
    kennel: {}
  },
  computed: {
    countries_select: { 
      get: function(){
        var self = this;
        var url = CONFIG['url_countries'];
        axios.get(url)
        .then(function (response) {
          console.log(response);
          return response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
      },
    },
    states_select: {
      get: function(){
        var self = this;
        var url = CONFIG['url_states'];
        axios.get(url)
        .then(function (response) {
          console.log(response);
          return response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
      },
    }
  },
  methods: {   

   getModal: function(slug){
    var self = this;
    var url = CONFIG['url_item'];
    url += slug + '/'
    axios.get(url)
    .then(function (response) {
      console.log(response);
      self.kennel = response.data;
      self.$bvModal.show(CONFIG['edit_modal'])
    })
    .catch(function (error) {
      console.log(error);
    });
  },
  closeModal: function(){
    this.kennel = {};
    $bvModal.hide(CONFIG['edit_modal']);
  },
  confirmDelete: function(slug){
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
    self.kennel = {};
  })
   .catch(function (error) {
    console.log(error);
  })
   .then(function () {
    self.$bvModal.hide(CONFIG['delete_modal']);
  });
 },
}
});
