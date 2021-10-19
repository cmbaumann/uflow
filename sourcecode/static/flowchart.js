
//When the page loads, make all courses have a white background
window.onload = function() {
    var x = document.getElementsByClassName("column");
    for (i = 0; i < x.length; i++) {
        x[i].style.backgroundColor = "white";
    }
};

    //Initialize current option and current color, as well as the status colors
    let curColor = "#ffffff";
    let curOption = "";
    let tak_col = "#00ff00";
    let ipr_col = "#0000ff";
    let fut_col = "#ff0000";

    //Changes the colors used into various kinds of colorblind alternatives (figure out what colors to use)
    function color_cb_opt(id) {
        //console.log(id);
        if (id == "0") {
            tak_col = "#00ff00";
            ipr_col = "#0000ff";
            fut_col = "#ff0000";
        }
        else if (id == "1") {
            tak_col = "#00ffff";
            ipr_col = "#ff00ff";
            fut_col = "#ffff00";

        }
        else if (id == "2") {
            tak_col = "#000000";
            ipr_col = "#5f5f5f";
            fut_col = "#afafaf";

        }
        else if (id == "3") {
            tak_col = "#0ffff0";
            ipr_col = "#f00fff";
            fut_col = "#fff00f";
        }
        if (curOption) {
            if (curOption == "taken") {document.getElementById(curOption).style.backgroundColor=tak_col; curColor=tak_col;}
            else if (curOption == "inprogress") {document.getElementById(curOption).style.backgroundColor=ipr_col; curColor=ipr_col;}
            else if (curOption == "future") {document.getElementById(curOption).style.backgroundColor=fut_col; curColor=fut_col;}
        }
        for (var i=1; i<=37; i++) {
            var newid = "d" + i.toString();
            var curCourse = document.getElementById(newid).value;
            if (curCourse == "taken") {document.getElementById(i).style.backgroundColor = tak_col;}
            else if (curCourse == "inprogress") {document.getElementById(i).style.backgroundColor = ipr_col;}
            else if (curCourse == "future") {document.getElementById(i).style.backgroundColor = fut_col;}
        }
    }

    //Course option selector. Sets current option and color
    function color(id) {
        if (id == curOption) {
            curColor = "#ffffff"
            curOption = "";
            document.getElementById(id).style.backgroundColor=curColor;
        }
        else if (id == ("taken")) {
            curColor = tak_col;
            curOption = "taken";
            document.getElementById(id).style.backgroundColor=curColor;
            document.getElementById("inprogress").style.backgroundColor="white";
            document.getElementById("future").style.backgroundColor="white";
        }
        else if (id == "inprogress") {
            curColor = ipr_col;
            curOption = "inprogress";
            document.getElementById(id).style.backgroundColor=curColor;
            document.getElementById("taken").style.backgroundColor="white";
            document.getElementById("future").style.backgroundColor="white";
        }
        else if (id == "future") {
            curColor = fut_col;
            curOption = "future";
            document.getElementById(id).style.backgroundColor=curColor;
            document.getElementById("taken").style.backgroundColor="white";
            document.getElementById("inprogress").style.backgroundColor="white";
        }
    }

    //Changes course value and bg color
    function change(id) {
        newid = "d" + id
        if (curOption == "taken") {
            change_sub(id, newid, "taken");
        }
        else if (curOption == "inprogress") {
            change_sub(id, newid, "inprogress");
        }
        else if (curOption == "future") {
            change_sub(id, newid, "future");
        }
    }

    function change_sub(id, newid, opt) {
        if (curOption == document.getElementById(newid).value) {
            document.getElementById(newid).value="";
            document.getElementById(id).style.backgroundColor = "#ffffff";
            console.log(document.getElementById(newid).value);
        }
        else {
            document.getElementById(newid).value=curOption;
            document.getElementById(id).style.backgroundColor = curColor;
            console.log(document.getElementById(newid).value);
        }
    }