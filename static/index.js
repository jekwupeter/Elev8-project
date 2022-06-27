let dropdown = document.getElementById("dropdown");
let navdrop = document.getElementById("navdrop");

function show() {
    dropdown.classList.toggle("hide");
}

function hover() {
    navdrop.style.borderStyle = solid;
}

navdrop.onclick = show;
navdrop.hover = hover;