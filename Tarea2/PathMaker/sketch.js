var i;

function preload(){
    moves = loadStrings('assets/out.txt')
    coords = loadJSON('assets/data.json');
    conn = loadJSON('assets/connect5.json');
    img = loadImage("assets/mexico.gif"); 
}


function setup() {
    createCanvas(940, 700);
    image(img, 0, 0, 940, 700);
    
    stroke(0);
    for(i in conn){
        for(j in conn[i]){
            line(coords[i][0], coords[i][1], coords[j][0], coords[j][1])
        }
    }
    fill(0,255,255);
    for(i in coords){
        ellipse(coords[i][0],coords[i][1],10,10);
    }
    moves = moves[0].replace("(",'').replace(")","").split(' ')
    fill(0,0,0);
    ellipse(coords[moves[0]][0],coords[moves[0]][1],20,20);
    fill(0,200,0)
    end = moves.length-1
    ellipse(coords[moves[end]][0],coords[moves[end]][1],20,20);
    print(moves)
    print(coords)
    
    textSize(20);
    
    fill(255)
    stroke(0)
    rect(20, 370, 315, 65)
    
    fill(0)
    strokeWeight(1)
    text('From: '+coords[moves[0]][2], 25, 395)
    text('To: '+coords[moves[end]][2], 25, 425)
    
    i = 0
    frameRate(2)
    stroke(255, 255, 0);
    strokeWeight(3);
}

function draw() {
    line(coords[moves[i]][0], coords[moves[i]][1], coords[moves[i+1]][0], coords[moves[i+1]][1]);
    i += 1
    if(i == moves.length-1){
        noLoop()
    }
}