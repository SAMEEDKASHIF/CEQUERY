
function displayGraphs(dataobj) {
    console.log(dataobj);
    document.getElementById("chart-title").innerHTML = dataobj['summary']['chartTitle'];
  try {
    //bar chart
    var ctx = document.getElementById("barChart");
    if (ctx) {
      var myChart = new Chart(ctx, {
        type: 'bar',
        defaultFontFamily: 'Poppins',
        data: {
          labels: dataobj['summary'].labels,
          datasets: [
            {
              label: "Positive",
              data: dataobj['summary']['positive'],
              borderColor: "rgba(0, 123, 255, 0.9)",
              borderWidth: "0",
              backgroundColor:"#000075",
              fontFamily: "Poppins"
            },
            {
              label: "Negative",
              data: dataobj['summary']['negative'],
              borderColor: "rgba(0,0,0,0.09)",
              borderWidth: "0",
              backgroundColor: "#7366BD",
              fontFamily: "Poppins"
            }
          ]
        },
        options: {
          legend: {
              position: 'top',
              labels: {
                  fontFamily: 'Poppins'
              }
          },
          scales: {
            xAxes: [{
              ticks: {
                fontFamily: "Poppins"

              }
            }],
            yAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Number of Comments'
                },
                ticks: {
                    beginAtZero: true,
                    fontFamily: "Poppins"
                }
            }]
          }
        }
      });
    }


  } catch (error) {
    console.log(error);
  }


  try {

    //doughnut chart
    var ctx = document.getElementById("doughnutChart");
    if (ctx) {
      var myChart = new Chart(ctx, {
        type: 'doughnut',
      data: {
          datasets: [{
            data: [15, 18, 9, 6, 19],
            backgroundColor: [
              "#A2A2D0",
              "#ACE5EE",
              "#126180",
              "#000075",
              "#7366BD"
            ],

          }],
          labels: [
            "Assessment",
            "Course Design",
            "Outcomes",
            "Staff",
			"Support"

          ]
        },
        options: {
          legend: {
            position: 'top',
            labels: {
              fontFamily: 'Poppins'
            }

          },
          responsive: true
        }
      });
    }


  } catch (error) {
    console.log(error);
  }

}