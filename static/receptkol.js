function expand(){
  var display = document.getElementById("display");
  var load = document.getElementById("load");
  var result = document.getElementById("result");
  var btn = document.getElementById("button");
  var text = document.getElementById("text");
  var id = setInterval(function() {frame(50);}, 1);
  var height = 0;
  go();
  sleep(2000).then(() => {
  makeresult(text.value);
  })
  function go(){
    result.style.display = 'none';
    btn.disabled = true;
    fadeIn(load);
  }
  function frame(n) {
    if (height == n) {
      clearInterval(id);
    } else {
      height++;
      display.style.height = height;
    }
  }
  function makeresult(text) {
      text_data = JSON.stringify(text);
      $.post("matkol", text_data , function(data){
      var id = setInterval(function() {frame(150);});
      load.style.opacity = 0;
      result.innerHTML = data;
      result.style.color = "green";
      result.style.opacity = 0;
      result.style.display = 'block';
      btn.disabled = false;
      fadeIn(result);
    });
  }
}
const sleep = (milliseconds) => {
  return new Promise(resolve => setTimeout(resolve, milliseconds))
}
function fadeIn(obj){
    var height = 0;
    var id = setInterval(step,3);
    function step(){
      if (height == 100) {
        clearInterval(id);
      } else {
        height++;
        obj.style.opacity = height*0.01;
      }
    }
}

function info(){
  var infoBox = document.getElementById("infoBox");
  if (infoBox.style.display === "block") {
   infoBox.style.display = "none";
  } else {
   infoBox.style.display = "block";
  }

}
