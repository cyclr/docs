const sidenav = document.getElementById("sidebarMenu");
const sidenavInstance = mdb.Sidenav.getInstance(sidenav);
let btnbacktotop = document.getElementById("btn-back-to-top");
let innerWidth = null;

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
    scrollFunction();
};

function scrollFunction() {
    if (
        document.body.scrollTop > 20 ||
        document.documentElement.scrollTop > 20
    ) {
        btnbacktotop.style.display = "block";
    } else {
        btnbacktotop.style.display = "none";
    }
}

function backToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

const setMode = (e) => {
  // Check necessary for Android devices
  if (window.innerWidth === innerWidth || !sidenav) {
    return;
  }
  innerWidth = window.innerWidth;

  if (window.innerWidth < 1400) {
    sidenavInstance.changeMode("over");
    sidenavInstance.hide();
  } else {
    sidenavInstance.changeMode("side");
    sidenavInstance.show();
  }
};

setMode();

//Stop "Scroll Chaining" when using the Side Nav
if (sidenav) {
    sidenavInstance._perfectScrollbar.settings.wheelPropagation = false;
}

// Event listeners
window.addEventListener("resize", setMode);
btnbacktotop.addEventListener("click", backToTop);

