var img;
var coords;
var conn;
var moves;

function preload(){
    coords = loadJSON('assets/data.json');
    conn = loadJSON('assets/connect5.json');
    img = loadImage("assets/mexico.gif"); 
    //moves = loadStrings('assets/out.txt');
}

function setup() {
    createCanvas(940, 700);
    image(img, 0, 0, 940, 700);
    fill(0,255,255);
    for(i in coords){
        ellipse(coords[i][0],coords[i][1],10,10);
    }
    stroke(0)
    for(i in conn){
        for(j in conn[i]){
            line(coords[i][0], coords[i][1], coords[j][0], coords[j][1])
        }
    }
    
    for(i in moves){
        moves[i] = moves[i].split(',')
    }
    
    stroke(255,0,0)
    //line(coords[moves[1][0]][0], coords[moves[1][0]][1], coords[moves[1][0]][0])
    
}

function draw() {
  //print(coords)
}