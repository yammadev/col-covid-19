// Summary
var summary = new Vue({
  // Element
  el: '#summary',

  // Data
  data: {
    cases: summary[0].TOTAL,
    recovered: summary[1].TOTAL,
    deaths: summary[2].TOTAL,
    cases_pop: 0,
    recovered_per: 0,
    deaths_per: 0
  },

  // Mounted
  mounted: function() {
    // Update
    this.cases_pop = (this.cases / 49.65).toFixed(2);
    this.recovered_per = (this.recovered * 100 / this.cases).toFixed(2);
    this.deaths_per = (this.deaths * 100 / this.cases).toFixed(2);
  }
});
