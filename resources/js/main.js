// Init
function init() {
  $('html').show();
  $('.scrollspy').scrollSpy();
  $('.tooltipped').tooltip();
}

/**
 * When document ready execute
 */
$(document).ready(function() {
  init();
  map();
  chart();
});

// Statistics
new Vue({
  el: '#statistics',
  data: {
    country: {
      active: summary.country.active,
      last: summary.country.last
    }
  }
});

// About
new Vue({
  el: '#about',
  data: {
    world: {
      active: summary.world.active
    },
    genders: {
      males: extras.genders.males,
      females: extras.genders.females
    }
  }
});
