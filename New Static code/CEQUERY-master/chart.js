<!DOCTYPE HTML>
<html>
<head>
<script>
window.onload = function () {

var chart = new CanvasJS.Chart("chartContainer", {
	title: {
		text: "Cooments good and bad"
	},
	axisY: {
		title: "cequery student comments (°C)",
		suffix: " °C"
	},
	data: [{
		type: "column",	
		yValueFormatString: "#,### °C",
		indexLabel: "{y}",
		dataPoints: [
			{ label: "good comments", y: 206 },
			{ label: "bad comments", y: 163 },
		]
	}]
});

function updateChart() {
	var goodcommentsColor, deltaY, yVal;
	var dps = chart.options.data[0].dataPoints;
	for (var i = 0; i < dps.length; i++) {
		deltaY = Math.round(2 + Math.random() *(-2-2));
		yVal = deltaY + dps[i].y > 0 ? dps[i].y + deltaY : 0;
		commentsColor = yVal > 200 ? "#FF2500" : yVal >= 170 ?: null;
		dps[i] = {label: "comments "+(i+1) , y: yVal, color: goodcomments};
	}
	chart.options.data[0].dataPoints = dps; 
	chart.render();
};
updateChart();

setInterval(function() {updateChart()}, 500);

}
</script>
</head>
<body>
<div id="chartContainer" style="height: 370px; width: 100;"></div>
<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
</body>
</html>
