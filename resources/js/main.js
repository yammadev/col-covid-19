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
});
