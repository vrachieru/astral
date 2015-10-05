(function () {
  var sky = {};

  if (typeof define === 'function' && define.amd) {
  	define(sky);
  } else if (typeof module !== 'undefined') {
    module.exports = sky;
  } else {
  	window.sky = sky;
  }
}());