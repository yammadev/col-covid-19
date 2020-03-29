// Map
function map() {
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
       className: city.cases < 30 ? 'icon-small' : (city.cases < 100 ? 'icon-medium' : 'icon-large'),   // Change value as it grows
       html: '<span class="center-align">' + city.cases + '</span>'
     })
   }).addTo(map)
     // Popup
     .bindPopup('<p class="center-align">' + '<span>' + city.name + '</span>' + '<br>' + city.cases + '</p>');
  }

  // Show (Dev purpouses)
  console.log('Total cases: ' + cases);
}
