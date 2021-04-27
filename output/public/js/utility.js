const sidebar = document.getElementById("sidebar");
const container = document.getElementById("container");
const navbar = document.getElementById("navbar");

if(localStorage.getItem('markoveter-theme') != null){
    console.log("Setting to stored theme...");
    setTheme(localStorage.getItem('markoveter-theme'))
} else {
    console.log("Setting to light theme...");
    setTheme('theme-light');
}

function toggleSidebar(){
    if(sidebar.style.display === "none" || sidebar.style.display === ""){
        console.log("Enabling sidebar...");
        sidebar.style.display = "flex";
    } else {
        console.log("Disabling sidebar...");
        sidebar.style.display = "none";
    }
}

function setTheme(themeName) {
    localStorage.setItem('markoveter-theme', themeName);
    document.documentElement.className = themeName;
}