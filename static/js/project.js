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