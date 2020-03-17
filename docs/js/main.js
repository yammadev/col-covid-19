$(document).ready(function() {
    $(".scrollspy").scrollSpy();
    var a = L.map("map").setView([ 51.505, -.09 ], 13);
    L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw", {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: "mapbox/streets-v11",
        tileSize: 512,
        zoomOffset: -1
    }).addTo(a), L.marker([ 51.5, -.09 ]).addTo(a).bindPopup("<b>Hello world!</b><br />I am a popup.").openPopup(), 
    L.circle([ 51.508, -.11 ], 500, {
        color: "red",
        fillColor: "#f03",
        fillOpacity: .5
    }).addTo(a).bindPopup("I am a circle."), L.polygon([ [ 51.509, -.08 ], [ 51.503, -.06 ], [ 51.51, -.047 ] ]).addTo(a).bindPopup("I am a polygon.");
    var e = L.popup();
    a.on("click", function(o) {
        e.setLatLng(o.latlng).setContent("You clicked the map at " + o.latlng.toString()).openOn(a);
    });
});
//# sourceMappingURL=main.js.map