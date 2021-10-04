function click_submit() {
    var elective_textarea = document.getElementById("electiveText");
    var elective_name = elective_textarea.value; 
    var submit_button = document.getElementById("7Submit");
    var submit_info = document.getElementById("7ElectiveHelp");
    var edit_button = document.getElementById("7Edit");

    // alert("first alert");
    submit_button.style.visibility = "hidden";
    submit_info.style.visibility = "hidden";
    document.getElementById("7OutputElective").innerHTML = elective_name;
    edit_button.style.visibility = "visible";
    // alert('button has been clicked - after all instructions');
}