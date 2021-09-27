function fill_elecitve() {
    // temp fix 
    // ultimately want to be able to pass course_id as arg from html file
    // var course_id = "7"
    
    var elective_box = document.getElementById("7Box");
    var elective_textarea = document.getElementById("fillOutElective");
    var elective_name = elective_textarea.value; 
    var submit_button = document.getElementById("7Submit");
    var submit_info = document.getElementById("7ElectiveHelp");
    var edit_button = document.getElementById("7Edit");
    
    submit_button.onclick = function() {
        submit_button.style.visibility = "hidden";
        submit_info.style.visibility = "hidden";
        document.getElementById(course_id + "OutputElective").innerHTML = elective_name;
        edit_button.style.visibility = "visible";
    };
};