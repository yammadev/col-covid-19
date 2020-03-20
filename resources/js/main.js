/**
 * Initialize
 */
// When document ready execute
$(document).ready(function() {
  init();
  initMap();
});

// Init
function init() {
  $('html').show();
  $('.scrollspy').scrollSpy();
  $('.tooltipped').tooltip();
}

// Map
function initMap() {
  // Configs
  var conf = {
    // Map center
    center: {
      lat: statistics.country.lat,
      lng: statistics.country.lng
    },
    // Zoom
    zoom: {
      init: 6,
      min: 5,
      max: 7
    },
    // References
    ref: {
      el: '<a href="http://openstreetmap.org">OpenStreetMap</a>',
      link: 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
    }
  };

  // Define map
  var map = L.map('map', {
    center: [
      conf.center.lat,
      conf.center.lng
    ],
    zoom: conf.zoom.init
  });

  // Add layer
  L.tileLayer(conf.ref.link, {
    // attribution: '&copy; ' + conf.ref.el + ' Contributors',
    attribution: '&copy; ' + conf.ref.el,
    minZoom: conf.zoom.min,
    maxZoom: conf.zoom.max
  }).addTo(map);

  // Count (Dev purpouses)
  var cases = 0;

  // Append data
  for(var i = 0; i < statistics.cities.length; i++) {
    var city = statistics.cities[i];  // Get city
    var cord = [city.lat, city.lng];  // Get coordinates

    cases += city.cases;    // Count (Dev purpouses)

    // Mark
    L.marker(cord, {
      icon: L.divIcon({
        className: city.cases >= 50 ? 'icon-large' : 'icon-small',
        html: '<span class="center-align">' + city.cases + '</span>'
      })
    }).addTo(map)
      // Popup
      .bindPopup('<p class="center-align">' + '<span>' + city.name + '</span>' + '<br>' + city.cases + '</p>');
  }

  // Show (Dev purpouses)
  console.log(cases);
}

/**
 * Instancias
 */
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
    }
  }
});
