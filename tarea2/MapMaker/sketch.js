var input;
var img;
var data = [];
var noIn = false;

function preload() {
    img = loadImage("assets/mexico.gif"); 
}


function mouseClicked(){
    fill(255,0,0);
    if(noIn){
        noIn = false
    }
    else{
        ellipse(mouseX,mouseY,10,10);
        s = input.value()+ ', ' + mouseX+ ', '+ mouseY
        data.push(s);
        print(s)
    }
}



function setup() {
    input = createInput();
    input.position(20, 400);
    createCanvas(940, 700);
    image(img, 0, 0, 940, 700);
    
    createButton('save')
    .position(20, 350)
    .mousePressed(function() {
    print('');
    print('');
    print('')
    print(data);
    noIn = true;
});

    createButton('undo')
    .position(20, 375)
    .mousePressed(function() {
    print('deleting: ' + data.pop());
    noIn = true;
});

}

function draw() {
  //print(mouseX)
}