var img;
var coords;
var conn;
var moves;
var from;

function preload(){
    coords = loadJSON('assets/data.json');
    conn = loadJSON('assets/connect5.json');
    img = loadImage("assets/mexico.gif"); 
    moves = loadJSON('assets/out.json');
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
    
    //for(i in moves){
    //    moves[i] = moves[i].split(',')
    //}
    
    stroke(0, 255, 0);
    strokeWeight(3);
    frameRate(1);
    
    from = moves["start"];
    print(moves)
    //print(coords)
}

function draw() {
    var to = moves[from];
    //print(from)
    line(coords[from][0], coords[from][1], coords[to][0], coords[to][1]);
    from = moves[from];
    if(from == moves["end"]){
        noLoop();
    }
}