const nav = document.getElementById("nav");
const navLinks = document.getElementsByClassName("nav-link");

window.addEventListener("scroll", () => {
  if (window.scrollY >= 60) {
    nav.style.backgroundColor = `rgba(229, 231, 235, 1)`;
    for (link of navLinks) {
      link.style.color = `rgba(34,9,1, 1)`;
    }
  } else {
    nav.style.backgroundColor = `rgba(229, 231, 235, 0)`;
    for (link of navLinks) {
      link.style.color = `rgba(243, 244, 246, 1)`;
    }
  }
});
