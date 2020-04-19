// Map
function map() {
  // Configs
  var conf = {
   // Map center
   center: {
     lat: 4.6097102,
     lng: -74.081749
   },
   // Zoom
   zoom: {
     init: 8,
     min: 6,
     max: 10
   },
   // References
   ref: {
     el: '<a href="http://openstreetmap.org">OpenStreetMap</a>',
     link: 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
   }
  };

  // Define
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

  // Save
  for(var i in statistics) {
    // Get city
    var city = {
      name: statistics[i].CITY + ', ' + statistics[i].DEPARTAMENT,
      cases: statistics[i].CASES,
      coords: [
        statistics[i].LAT,
        statistics[i].LNG
      ]
    };

    // Mark
    L.marker(city.coords, {
      icon: L.divIcon({
        className: city.cases < 50 ? 'icon-small' : (city.cases < 100 ? 'icon-medium' : 'icon-large'),   // Change value as it grows
        html: '<span class="center-align">' + city.cases + '</span>'  // Number
      })
    }).addTo(map)
      // Popup
      .bindPopup('<p class="center-align">' + '<span>' + city.name + '</span>' + '<br>' + city.cases + '</p>');
  }
}
