function getData() {
  ajaxGetRequest("/pieChart", pieChart);
  ajaxGetRequest("/lineChart", lineChart);
}
function pieChart(pieGraphData) {
  let Arrestdata = JSON.parse(pieGraphData);
  let data = [{
    hole: 0.4,
    values: Arrestdata,
    labels: ["Brooklyn", "Manhattan", "Bronx", "Queens", "Staten Island"],
    type: "pie",
  }];
  let layout = {title:"NYC Arrests By Borough"}
  let newPlot = Plotly.newPlot("pieChart", data, {title:"NYC Arrests By Borough"})
  let pieDiv = document.getElementById("pieChart");
  pieDiv["innerhtml"] = newPlot
}
function barGraph(barGraphData) {
  let Arrestdata = JSON.parse(barGraphData);
  let data = [{
    x: ["<18", "18-24", "25-44", "45-64", "65+"],
    y: Arrestdata,
    type: "bar",
  }];
  let layout = {title:"Arrests made per Age Group", 
                  xaxis: {
    title: {
      text: 'Age Groups',
      font: {
        family: 'Courier New, monospace',
        size: 18,
        color: '#7f7f7f'
      }
    },
  },
  yaxis: {
    title: {
      text: 'Arrests made',}}}
  let newPlot = Plotly.newPlot("barGraph", data, layout)
  let barDiv = document.getElementById("barGraph");
  barDiv["innerhtml"] = newPlot
}
function lineChart(lineChartData) {
  let Arrestdata = JSON.parse(lineChartData);
  keys = Object.keys(Arrestdata)
  values = Object.values(Arrestdata)
  newx = []
  newy = []
  for (var value of values) {
    newy.push(value)
  }
  for (var key of keys) {
    newx.push(key)
  }
  let data = [{
    x: newx,
    y: newy,
    type: "line",
  }];
    let layout = {title:"NYC Arrests Per Day", 
  xaxis: {
    showgrid: false,
    title: {
      text: 'Dates',
      font: {
        family: 'Courier New, monospace',
        size: 18,
        color: '#7f7f7f'
      }
    },
  },
  yaxis: {
    showgrid: false,
    title: {
      text: 'Arrests made',}}}
  let newPlot = Plotly.newPlot("lineChart", data, layout)
  let lineDiv = document.getElementById("lineChart");
  lineDiv["innerhtml"] = newPlot
}
function getBarGraph() {
  let BoroDiv = document.getElementById("boroText").value;
  let data = {"boroDiv":BoroDiv};
  let dataJSON = JSON.stringify(data)
  ajaxPostRequest("barGraph", dataJSON, barGraph);
}