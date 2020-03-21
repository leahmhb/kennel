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
  mounted: function() {
  },
  methods: {   
    getModal: function(slug){
      var self = this;
      var id = 'edit-kennel-modal';
      var url = '/api/kennel/';
      url += slug + '/'
      // Make a request for a user with a given ID
      axios.get(url)
      .then(function (response) {
        console.log(response);
        self.kennel = response.data;
        self.$bvModal.show(id)
      })
      .catch(function (error) {

        console.log(error);
      })
      .then(function () {

      });
    }
  }
});
