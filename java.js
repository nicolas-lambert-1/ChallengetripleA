window.onload = function() {
    var target = document.getElementById('foo');
    target.width = target.clientWidth;
    target.height = target.clientHeight;

    var opts = {
  lines: 12,
  angle: 0,
  lineWidth: 0.57,
  radiusScale: 0.86,
  pointer: {
    length: 0.74,
    strokeWidth: 0.029,
    color: '#000000'
  },
  limitMax: 'false', 
  percentColors: [[0.0, "#a9d70b" ], [0.50, "#f9c802"], [1.0, "#ff0000"]], 
  strokeColor: '#E0E0E0',
  generateGradient: true,
  renderTicks: {
    divisions: 10,
    divWidth: 0.7,
    divLength: 0.21,
    divColor: '#333333',
    subDivisions: 2,
    subLength: 0.06,
    subWidth: 0.6,
    subColor: '#666666'
  }
};

    var gauge = new Gauge(target).setOptions(opts);
    var textField = document.getElementById("gauge-text");
    gauge.setTextField(textField);

    var cpuValue = parseFloat(document.getElementById("cpu").dataset.value);
    
    gauge.maxValue = 100;
    gauge.setMinValue(0);
    gauge.animationSpeed = 64;
    gauge.set(cpuValue);
};

