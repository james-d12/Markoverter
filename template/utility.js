const sidebar = document.getElementById("sidebar");
const container = document.getElementById("container");
const navbar = document.getElementById("navbar");

if(localStorage.getItem('theme') != null){
    setTheme(localStorage.getItem('markoveter-theme'))
} else {
    setTheme('theme-light');
}

function toggleSidebar(){
    if(sidebar.style.display === "none"){
        sidebar.style.display = "flex";
        container.classList.toggle("enlarged")
        navbar.classList.toggle("enlarged");
    } else {
        sidebar.style.display = "none";
        container.classList.toggle("enlarged")
        navbar.classList.toggle("enlarged");
    }
}

function setTheme(themeName) {
    localStorage.setItem('markoveter-theme', themeName);
    document.documentElement.className = themeName;
}