// Summary
var summary = new Vue({
  // Element
  el: '#summary',

  // Data
  data: {
    cases: summary[0].TOTAL,
    recovered: summary[1].TOTAL,
    deaths: summary[2].TOTAL,
    cases_today: summary[3].TOTAL,
    cases_yesterday: summary[4].TOTAL,
    cases_diff: 0,
    recovered_per: 0,
    deaths_per: 0
  },

  // Mounted
  mounted: function() {
    // Update
    this.cases_diff = (this.cases_today - this.cases_yesterday);
    this.recovered_per = (this.recovered * 100 / this.cases).toFixed(2);
    this.deaths_per = (this.deaths * 100 / this.cases).toFixed(2);
  }
});
