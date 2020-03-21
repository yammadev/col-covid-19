// Chart
function chart() {
  // Dataset
  var dataset = {
    ages: [],
    males: [],
    females: []
  };

  // Count (Dev purpouses)
  var count = {
    males: 0,
    females: 0,
  }

  // Append data
  for(var i = 0; i < extras.groups.length; i++) {
    dataset.ages.push(extras.groups[i].ages);         // Get range of age
    dataset.males.push(extras.groups[i].males);       // Get males
    dataset.females.push(extras.groups[i].females);   // Get females

    count.males += extras.groups[i].males;      // Count (Dev purpouses)
    count.females += extras.groups[i].females;  // Count (Dev purpouses)
  }

  // Show (Dev purpouses)
  console.log('Ages[]: ' + dataset.ages);
  console.log('Males[]: ' + dataset.males);
  console.log('Females[]: ' + dataset.females);
  console.log('Males: ' + count.males);
  console.log('Females: ' + count.females);
  console.log('Count: ' + (count.males + count.females));

  // Labels
  var labels = {
    axes: {
      x: 'Rango de edades',
      y: 'No. de Casos'
    },
    bars: {
      males: 'Masculinos',
      females: 'Femeninos'
    }
  };

  // Data
  var data = {
		labels: dataset.ages,         // x data
		datasets: [
      {
  			label: labels.bars.males,
  			backgroundColor: 'rgb(54, 162, 235)',    // Red
  			data: dataset.males      // y data
  		},
      {
  			label: labels.bars.females,
  			backgroundColor: 'rgb(255, 99, 132)',    // Blue
  			data: dataset.females    // y data
  	  }
    ]
  };

  // Context
  var ctx = document.getElementById('chart').getContext('2d');

  // Configs
  var conf = {
    type: 'bar',
    data: data,
    options: {
      tooltips: {
        mode: 'index',
        intersect: false
      },
      responsive: true,
      scales: {
        xAxes: [{
          stacked: true,
          scaleLabel: {
            display: true,
            labelString: labels.axes.x
          }
        }],
        yAxes: [{
          stacked: true,
          scaleLabel: {
            display: true,
            labelString: labels.axes.y
          }
        }]
      }
    }
  };

  // Define
  var chart = new Chart(ctx, conf);
}
