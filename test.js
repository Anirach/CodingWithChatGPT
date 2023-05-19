// Your code hereconst readline = require('readline');
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let b = rl.question('Enter movie ID: ',  (name) => {
    rl.close();    
     name = name - 1 ;


    const fs = require('fs');

    if(name > 4){
        console.log("Movie not found.");

    }
    if(name < 5){
    fs.readFile('movies1.json', 'utf8', (err, data1) => {
    let obj1 = JSON.parse(data1);
    fs.readFile('movies2.json', 'utf8', function(err,data2) {
        let obj2 = JSON.parse(data2);
        console.log("Title: "+obj1[name].title);
        console.log("Actor: "+obj2[name].actor);
        console.log("Director: "+obj1[name].director);
        console.log("Year: "+obj1[name].year);
        console.log("Rating: "+obj2[name].rating);
        console.log("Synopsis: "+obj2[name].synopsis);

    }
    );
    //console.log(obj);

    
    }
    
);
}



    
}
);





// id  input
// title  m1
// actor  m2
// Director: m1
// Year:  m1
// Rating:  m2
// Synopsis:  m2