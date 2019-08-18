
(function ($) {
  // USE STRICT
  "use strict";

  try {
    //bar chart
    var ctx = document.getElementById("barChart");
    if (ctx) {
      ctx.height = 200;
      var myChart = new Chart(ctx, {
        type: 'bar',
        defaultFontFamily: 'Poppins',
         data: {
          datasets: [{
			 
			 
            data: [15, 18, 9, 6, 19],
            backgroundColor: [
              "#A2A2D0",
              "#ACE5EE",
              "#126180",
              "#000075",
              "#7366BD"
            ]

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
            display: false,
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

    //pie chart
    var ctx = document.getElementById("pieChart");
    if (ctx) {
      ctx.height = 200;
      var myChart = new Chart(ctx, {
        type: 'pie',
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

    try {

    //line chart
    var ctx = document.getElementById("lineChart");
    if (ctx) {
      ctx.height = 150;
      var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          datasets: [{
			 
			
            data: [15, 18, 9, 6, 19],
            backgroundColor: [
             "#000075"
              
            ]

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
            display: false,
            labels: {
              fontFamily: 'Poppins'
            }

          },
		  responsive: true,
          tooltips: {
            mode: 'index',
            intersect: false
          },
         scales: {
            xAxes: [{
              ticks: {
                fontFamily: "Poppins"

              }
            }],
            yAxes: [{
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

    //doughut chart
    var ctx = document.getElementById("doughutChart");
    if (ctx) {
      ctx.height = 150;
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


})(jQuery);



