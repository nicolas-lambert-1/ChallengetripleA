window.onload = function() {
    var target = document.getElementById('foo');
    target.width = 200;
    target.height = 200;

    var opts = {
        angle: 0,
        lineWidth: 0.64,
        radiusScale: 0.82,
        pointer: { length: 0.65, strokeWidth: 0.026, color: '#000000' },
        limitMax: false,
        limitMin: true,
        colorStart: '#6FADCF',
        colorStop: '#8FC0DA',
        strokeColor: '#E0E0E0',
        generateGradient: true,
        highDpiSupport: true,
        staticLabels: {
            font: "10px sans-serif",
            labels: [0,50,100,150,200,250,300],
            color: "#000",
            fractionDigits: 0
        }
    };

    var gauge = new Gauge(target).setOptions(opts);
    var textField = document.getElementById("gauge-text");
    gauge.setTextField(textField);

    var cpuValue = 120;
    gauge.maxValue = 300;
    gauge.setMinValue(0);
    gauge.animationSpeed = 64;
    gauge.set(cpuValue);
};
