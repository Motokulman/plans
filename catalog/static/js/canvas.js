var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');
var raf;
var running = false;
var mouseOldPos;
var mousePos;
//var a = {{a}} ;

var ball = {

  draw: function() {
    ctx.beginPath();
    ctx.moveTo(mouseOldPos.x, mouseOldPos.y);
    ctx.lineTo(mousePos.x, mousePos.y);
    ctx.stroke();
    console.log(b);
    b='c'
    console.log(b);
  }
};

function clear() {
  ctx.fillStyle = 'rgba(255, 255, 255, 1)';
  ctx.fillRect(0,0,canvas.width,canvas.height);
}

// function draw() {
//   clear();
//   ball.draw();
//   // ball.x += ball.vx;
//   // ball.y += ball.vy;

//   // if (ball.y + ball.vy > canvas.height || ball.y + ball.vy < 0) {
//   //   ball.vy = -ball.vy;
//   // }
//   // if (ball.x + ball.vx > canvas.width || ball.x + ball.vx < 0) {
//   //   ball.vx = -ball.vx;
//   // }

//   raf = window.requestAnimationFrame(draw);
// }

canvas.addEventListener('mousemove', function(e) {
  //var rect = canvas.getBoundingClientRect();
  ctx.lineWidth = 10.0; 
  ctx.lineCap = 'square';
  if (running) {
    clear();
    mousePos = getMousePos(canvas, e);
    ball.draw();
  }
});

canvas.addEventListener('click', function(e) {
  if (!running) {
    mouseOldPos = getMousePos(canvas, e);
    //raf = window.requestAnimationFrame(draw);
    running = true;

  } else {
    //window.cancelAnimationFrame(raf);
    running = false;
  }

});

// canvas.addEventListener('mouseout', function(e) {
//  // window.cancelAnimationFrame(raf);
//   running = false;
// });

function getMousePos(canvas, e) {
  // necessary to take into account CSS boudaries
  var rect = canvas.getBoundingClientRect();
  return {
      x: e.clientX - rect.left,
      y: e.clientY - rect.top
  };
}

