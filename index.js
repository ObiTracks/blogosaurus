console.log("I'm working!!");

const titleColor = document.querySelector("#aboutme");

console.log(titleColor);

titleColor.addEventListener('click', () => {
  console.log("The screen has been clicked and the color will now change");


  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  console.log(color);
  return color;

  document.querySelector("#aboutme").style.backgroundColor = "red";
});
