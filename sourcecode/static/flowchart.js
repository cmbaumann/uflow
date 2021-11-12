var prereqArray = [
    [], //nothing
    [], //EN 101
    [], //ENGR 103
    [], //MATH 125
    [], //CS 100
    [], //CS 121
    [1], //EN 102,
    [],
    [3], //MATH 126
    [3, 4], //CS 101
    [],
    [3], //MATH 301
    [9], //CS 200
    [4], //ECE 380
    [], //
    [], 
    [11], //MATH 302
    [9, 11], //CS 201
    [13], //MATH 383
    [], //
    [], //
    [8], //GES 255/MATH 355
    [12, 17], //CS 300
    [12, 17], //CS 301
    [],
    [],
    [8], //MATH 237
    [18, 22, 23], //CS 403
    [18, 22, 23], //CS 4xx
    [],
    [],
    [], //Natural Science 1
    [18, 22, 23], //CS 470/475
    [18, 22, 23], //CS 4xx
    [],
    [],
    [31], //Natural Science 2
    [27, 28, 32] //CS 495
];

var postreqArray = [
    [], //nothing
    [6], //EN 101
    [], //ENGR 103
    [8], //MATH 125
    [9], //CS 100
    [], //CS 121
    [], //EN 102,
    [],
    [21, 26], //MATH 126
    [12, 17], //CS 101
    [],
    [16, 17], //MATH 301
    [22, 23], //CS 200
    [18], //ECE 380
    [], //
    [], 
    [], //MATH 302
    [22, 23], //CS 201
    [], //ECE 383
    [], //
    [], //
    [], //GES 255/MATH 355
    [27, 28, 32, 33], //CS 300
    [27, 28, 32, 33], //CS 301
    [],
    [],
    [], //MATH 237
    [37], //CS 403
    [37], //CS 4xx
    [],
    [],
    [36], //Natural Science 1
    [37], //CS 470/475
    [], //CS 4xx
    [],
    [],
    [], //Natural Science 2
    [] //CS 495
];

let pickColMode = 0;
let curColor = "#ffffff";
let curOption = 12;
const default_optionCols = ["#008000", "#0000ff",    "#ff0000", "#800080", "#ffff00", "#808000", "#00FF00", "#FF00FF", "#F4A460", "#ffe4e1", "#00ffff", "#008080", "#aaaaaa"]
let optionCols = ["#008000", "#0000ff",    "#ff0000", "#800080", "#ffff00", "#808000", "#00FF00", "#FF00FF", "#F4A460", "#ffe4e1", "#00ffff", "#008080", "#aaaaaa"]
let optionList = ["taken",   "inprogress", "spring0", "fall0",   "spring1", "fall1",   "spring2", "fall2",   "spring3", "fall3",   "spring4", "fall4",   "deselect"];
//                 green      blue          red        purple     yellow     olive      lime       fuchsia    sdybrn     mstyrose   aqua       teal       white  
//                 0          1             2          3          4          5          6          7          8          9          10         11         12

window.onload = function() {
    /*var path = window.location.pathname;
    var page = path.split("/")[1];
    //console.log(page);

    if (page == "flowchart-edit") {
        console.log("get stuff from database");
        for (var i = 1; i < 14; i++) {
            var id = "c" + i.toString()
            optionCols[i-1] = document.getElementById(id).value;
        }
    } else {
        for (var i = 1; i < 14; i++) {
            var id = "c" + i.toString()
            document.getElementById(id).value = optionCols[i-1];
        }
    }*/
    DBtoOpts();
}

//On click event for option buttons
    //If colorpick mode is on, then set whatever option is clicked to the color of the color display that appears when color mode is on. Change color of all courses with same value as the option
    //If colorpick mode is not on, get the option color and number, set all options but the selected option to white
function color(id) {
    if (pickColMode) {
        for (var i = 0; i < optionList.length; i++) {
            //console.log(i);
            if (id != optionList[i] || id == "deselect") {}
            else { 
                if (curColor == optionCols[i]) { curColor = document.getElementById("c-display").value; }
                optionCols[i] = document.getElementById("c-display").value;
                document.getElementById("c"+(i+1).toString()).value=optionCols[i];
                document.getElementById(id).style.backgroundColor=optionCols[i];
                var courses = document.getElementsByClassName("course");
                for (var q = 0; q < courses.length; q++) {
                    if (document.getElementById("d"+courses[q].id).value == optionList[i]) {
                        courses[q].style.backgroundColor = optionCols[i];
                    }
                }
            }
        }

    } else {
        for (var i = 0; i < optionList.length; i++) {
            //console.log(i);
            if (id != optionList[i]) { document.getElementById(optionList[i]).style.backgroundColor="#ffffff"; }
            else { 
                curColor = optionCols[i];
                curOption = i;
                document.getElementById(id).style.backgroundColor=curColor;
            }
        }
    }
}

function DBtoOpts() {
    document.getElementById("btn-change").style.backgroundColor = "#ffffff";
    for (var i = 0; i < 12; i++) {
        optionCols[i] = document.getElementById("c"+(i+1).toString()).value;
        console.log(optionCols[i]);
        document.getElementById(optionList[i]).style.backgroundColor = "#ffffff";
    }
    document.getElementById(optionList[12]).style.backgroundColor = optionCols[12];
}

//Reveal colors of all options
function colorTest() {
    var opts = document.getElementsByClassName('color');
    for (var i = 0; i < opts.length; i++) {
        opts[i].style.backgroundColor = optionCols[i];
    }
}

//Reveals a color picker element on the webpage to use to change the color of the options
    //When this option is clicked, show colors of all options, show the color picker, set the colorpick flag to 1
    //When this option is clicked again, Set all options but the current option to white, hide the color picker, set the colorpick flag to 0
function colorChange() {
    if (!pickColMode) {
        colorTest();
        document.getElementById("btn-change").style.backgroundColor = "#7777ff";
        document.getElementById("color-chooser").style.display = "block";
        pickColMode = 1;
        var opts = document.getElementsByClassName('color');
        for (var i = 0; i < opts.length-1; i++) {
            opts[i].style.borderStyle = "dashed";
        }
        colCanvasChange();
    } else {
        document.getElementById("btn-change").style.backgroundColor = "#ffffff";
        document.getElementById("color-chooser").style.display = "none";
        pickColMode = 0;
        var opts = document.getElementsByClassName('color');
        for (var i = 0; i < opts.length; i++) {
            opts[i].style.borderStyle = "solid";
            if (curOption == i) {opts[i].style.backgroundColor = optionCols[i]; curColor=optionCols[i];}
            else { opts[i].style.backgroundColor = "#ffffff"}
        }
    }
}

//Changes the color of the display used to determine the picked color
function colCanvasChange() {
    colmtrx = document.getElementsByClassName("c-picker");
    var red = parseInt(colmtrx[0].value).toString(16);
    var grn = parseInt(colmtrx[1].value).toString(16);
    var blu = parseInt(colmtrx[2].value).toString(16);
    if (red.length == 1) { red = "0" + red; }
    if (grn.length == 1) { grn = "0" + grn; }
    if (blu.length == 1) { blu = "0" + blu; }
    hexVal = "#" + red + grn + blu;
    console.log(hexVal);
    document.getElementById("c-display").style.backgroundColor = hexVal;
    document.getElementById("c-display").value = hexVal;
}

//Changes the color of the options and the selected courses back to their default color
function colorDefault() {
    var opts = document.getElementsByClassName('color');
    var courses = document.getElementsByClassName('course');
    //Set option colors to default
    for (var i = 0; i < optionCols.length-1; i++) {
        if (curColor == optionCols[i]) { curColor = default_optionCols[i]; }
        optionCols[i] = default_optionCols[i];
        document.getElementById("c"+(i+1).toString()).value = default_optionCols[i]
    }
    for (var i = 0; i < opts.length; i++) {
        if (curColor == optionCols[i]) { opts[i].style.backgroundColor = optionCols[i]; }
        if (pickColMode) { opts[i].style.backgroundColor = optionCols[i]; }
        for (var q = 0; q < courses.length; q++) {
            if (document.getElementById("d"+courses[q].id).value == optionList[i]) {
                courses[q].style.backgroundColor = optionCols[i];
            }
        }
    }
}

//Changes the value of a course based on the current option (curOption) when clicked
function change(id) {

    newid = "d" + id;
    if (curOption == 12) {  //deselect option
        document.getElementById(id).style.backgroundColor = "#ffffff";
        document.getElementById(newid).value="";
    } 
    else { 
        document.getElementById(id).style.backgroundColor = curColor;
        document.getElementById(newid).value = optionList[curOption];
    }
    //console.log("changed: "+ document.getElementById(newid).value + " color: " + document.getElementById(id).style.backgroundColor);
}

function getElectiveHours(index) {
    if (index == 0) { return 3; }
    else if (index == 1) { return 3; }
    else if (index == 2) { return 3; }
    else if (index == 3) { return 4; }
    else if (index == 4) { return 3; }
    else if (index == 5) { return 3; }
    else if (index == 6) { return 3; }
    else if (index == 7) { return 3; }
    else if (index == 8) { return 3; }
    else if (index == 9) { return 3; }
    else if (index == 10) { return 3; }
    else if (index == 11) { return 4; }
    else if (index == 12) { return 3; }
    else if (index == 13) { return 3; }
    else if (index == 14) { return 3; }
    else if (index == 15) { return 4; }
}

function getHours(id) {
    if (id == 1) { return 3; }
    else if (id == 2) { return 3; }
    else if (id == 3) { return 4; }
    else if (id == 4) { return 4; }
    else if (id == 5) { return 1; }
    else if (id == 6) { return 3; }
    else if (id == 7) { return getElectiveHours(0); }
    else if (id == 8) { return 4; }
    else if (id == 9) { return 4; }
    else if (id == 10) { return getElectiveHours(1); }
    else if (id == 11) { return 3; }
    else if (id == 12) { return 4; }
    else if (id == 13) { return 4; }
    else if (id == 14) { return getElectiveHours(2); }
    else if (id == 15) { return getElectiveHours(3); }
    else if (id == 16) { return 1; }
    else if (id == 17) { return 4; }
    else if (id == 18) { return 4; }
    else if (id == 19) { return getElectiveHours(4); }
    else if (id == 20) { return getElectiveHours(5); }
    else if (id == 21) { return 3; }
    else if (id == 22) { return 3; }
    else if (id == 23) { return 3; }
    else if (id == 24) { return getElectiveHours(6); }
    else if (id == 25) { return getElectiveHours(7); }
    else if (id == 26) { return 3; }
    else if (id == 27) { return 3; }
    else if (id == 28) { return getElectiveHours(8); }
    else if (id == 29) { return getElectiveHours(9); }
    else if (id == 30) { return getElectiveHours(10); }
    else if (id == 31) { return getElectiveHours(11); }
    else if (id == 32) { return 3; }
    else if (id == 33) { return getElectiveHours(12); }
    else if (id == 34) { return getElectiveHours(13); }
    else if (id == 35) { return getElectiveHours(14); }
    else if (id == 36) { return getElectiveHours(15); }
    else if (id == 37) { return 3; }
}

function incrementHours(id) {
    // if ((id != 7) &&  (id != 10) && (id != 14) && (id != 15) && (id != 19) && (id != 20) && (id != 24) && 
    //     (id != 25) && (id != 28) && (id != 29) && (id != 30) && (id != 31) && (id != 10) && (id != 33) && 
    //     (id != 34) && (id != 35) && (id != 36)) { //if not an elective (those are handled differently)
            var taken = document.getElementById("hoursTaken").innerHTML;
            var planned = document.getElementById("hoursPlanned").innerHTML;
            var hoursTaken = taken.match(/\d/g);
            console.log("hoursTaken:", hoursTaken);
            var hours1 = "";
            for (var i = 0; i < hoursTaken.length; ++i) {
                hours1 += hoursTaken[i];
            }
            hoursTaken = parseInt(hours1, 10);
            console.log("hoursTaken:", hoursTaken);
            var hoursPlanned = planned.match(/\d/g);
            console.log("hoursPlanned:", hoursPlanned);
            var hours2 = "";
            for (var i = 0; i < hoursPlanned.length; ++i) {
                hours2 += hoursPlanned[i];
            }
            hoursPlanned = parseInt(hours2);
            console.log("hoursPlanned:", hoursPlanned);
            if (optionList[curOption] == "taken") {
                hoursTaken += getHours(id);
                hoursPlanned += getHours(id);
            }
            else {
                hoursPlanned += getHours(id);
            }
            takenString = "Hours Taken: " + hoursTaken
            plannedString = "Hours Planned: " + hoursPlanned
            document.getElementById("hoursTaken").innerHTML = takenString;
            document.getElementById("hoursPlanned").innerHTML = plannedString;
    // }
}

//Checks if the clicked class has a prerequisite and/or postrequisite before setting its value and color
function prereqCheck(id) {
    if(!pickColMode) {
        prereq = searchPrereqArray(id);
        if (prereq.length == 0) {
            postreq = searchPostreqArray(id);
            if (postreq.length == 0) {
                change(id);
                incrementHours(id);
            }
            else {
                alertstring = "You need this class as a prerequisite for ";
                for (var i = 0; i < postreq.length; ++i) {
                    if (i == 0) {
                    alertstring = alertstring + postreq[i];
                    }
                    else if ((i+1) == postreq.length) {
                        alertstring = alertstring + ", and " + postreq[i];
                    }
                    else {
                        alertstring = alertstring + ", " + postreq[i];
                    }
                }
                alert(alertstring);
            }
        }
        else {
            alertstring = "You do not have these prerequisites for this course: ";
                for (var i = 0; i < prereq.length; ++i) {
                    if (i == 0) {
                        alertstring = alertstring + prereq[i];
                    }
                    else if ((i+1) == prereq.length) {
                        alertstring = alertstring + ", and " + prereq[i];
                    }
                    else {
                        alertstring = alertstring + ", " + prereq[i];
                    }
                }
            alert(alertstring);
        }
    }
}

//Searches the prerequisite array
function searchPrereqArray(id) {
    returnarray = [];
    var colorStatus = getColorStatus();
    colorStatus = getNumericalColorStatus(colorStatus);
    var temp;
    if (colorStatus == 1) return returnarray;
    for (var i=0; i<prereqArray[id].length; i++) {
        temp = document.getElementById("d"+prereqArray[id][i]).value;
        temp = getNumericalColorStatus(temp);
        if (temp >= colorStatus) {
            returnarray.push(getClassName(prereqArray[id][i]));
        }
    }
    return returnarray;
}

//Sarches the postrequisite array
function searchPostreqArray(id) {
    returnarray = [];
    var colorStatus = getColorStatus();
    colorStatus = getNumericalColorStatus(colorStatus);
    console.log(colorStatus);
    var temp;
    if (colorStatus == 1) return returnarray;
    for (var i=0; i<postreqArray[id].length; i++) {
        temp = document.getElementById("d"+postreqArray[id][i]).value;
        temp = getNumericalColorStatus(temp);
        if (temp <= colorStatus) {
            returnarray.push(getClassName(postreqArray[id][i]));
        }
    }
    return returnarray;
}

//Gets the corresponding option name of a color
function getColorStatus() {
    switch(curColor) {
        case optionCols[ 0]: return "taken";
        case optionCols[ 1]: return "inprogress";
        case optionCols[ 2]: return "spring0";
        case optionCols[ 3]: return "fall0";
        case optionCols[ 4]: return "spring1";
        case optionCols[ 5]: return "fall1";
        case optionCols[ 6]: return "spring";
        case optionCols[ 7]: return "fall2";
        case optionCols[ 8]: return "spring3";
        case optionCols[ 9]: return "fall3";
        case optionCols[10]: return "spring4";
        case optionCols[11]: return "fall4";
        case optionCols[12]: return "deselect";
        case "#ffffff": return "";
    }
}

//Gets the corresponding value of an option name
function getNumericalColorStatus(colorStatus) {
    switch(colorStatus) {
        case "taken": return 1;
        case "inprogress": return 2;
        case "spring0": return 3;
        case "fall0": return 4;
        case "spring1": return 5;
        case "fall1": return 6;
        case "spring": return 7;
        case "fall2": return 8;
        case "spring3": return 9;
        case "fall3": return 10;
        case "spring4": return 11;
        case "fall4": return 12;
        case "deselect": return 13;
        case "": return 14;
    }
}

//FIXME make this a switch case
//Gets the name of a course
function getClassName(id) {
    if (id == 1) return "EN 101";
    else if (id == 2) return "ENGR 103";
    else if (id == 3) return "MATH 125";
    else if (id == 4) return "CS 100";
    else if (id == 5) return "CS 121";
    else if (id == 6) return "EN 102";
    else if (id == 7) return "HI/SB Elective";
    else if (id == 8) return "MATH 126";
    else if (id == 9) return "CS 101";
    else if (id == 10) return "HU/L/FA Elective";
    else if (id == 11) return "MATH 301";
    else if (id == 12) return "CS 200";
    else if (id == 13) return "ECE 380";
    else if (id == 14) return "HU/L/FA Elective";
    else if (id == 15) return "Natural Science Elective";
    else if (id == 16) return "MATH 302";
    else if (id == 17) return "CS 201";
    else if (id == 18) return "ECE 383";
    else if (id == 19) return "Free Elective";
    else if (id == 20) return "HI/SB Elective";
    else if (id == 21) return "GES 255/ MATH 355";
    else if (id == 22) return "CS 300";
    else if (id == 23) return "CS 301";
    else if (id == 24) return "Free Elective";
    else if (id == 25) return "HI/SB Elective";
    else if (id == 26) return "MATH 237";
    else if (id == 27) return "CS 403";
    else if (id == 28) return "CS 4xx";
    else if (id == 29)  return "Free Elective";
    else if (id == 30) return "HU/L/FA Elective";
    else if (id == 31) return "Natural Sciene Sequence #1";
    else if (id == 32) return "CS 470/ CS 475";
    else if (id == 33) return "CS 4xx";
    else if (id == 34) return "Free Elective";
    else if (id == 35) return "Free Elective";
    else if (id == 36) return "Natural Science Sequence #2";
    else if (id == 37) return "CS 495";
}

function saveMessage() {
    var proceed = confirm("Your flowchart will not be saved.")
    if (proceed == true) {
        return
    }
    else {
        e = window.event;
        e.cancelBubble = true;
        e.stopPropagation();
        e.preventDefault();
    }
}