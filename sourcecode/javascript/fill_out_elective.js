function fill_elecitve() {
    // temp fix 
    // ultimately want to be able to pass course_id as arg from html file
    var course_id = "7"
    
    var elective_box = document.getElementById(course_id + "Box");
    var elective_textarea = document.getElementById("fillOutElective");
    var elective_name = elective_textarea.value
    var submit_button = document.getElementById(course_id + "Submit");
    var submit_info = document.getElementById(course_id + "ElectiveHelp");
    var edit_button = document.getElementById(course_id + "Edit");

    edit_button.style.display = "none";

    submit_button.onclick = function() {
        submit_button.style.display = "none";
        submit_info.style.display = "none";
        document.getElementById(course_id + "OutputElective").innerHTML = elective_name;
        edit_button.style.display = "block";
    };
};