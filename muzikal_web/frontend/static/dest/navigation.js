// Get the navigation bar element
const nav = document.getElementById('nav');
const navLinks = document.getElementsByClassName('nav-link');

// Listen for the scroll event
window.addEventListener('scroll', () => {
    // Calculate the opacity based on the scroll position
    const opacity = window.scrollY / window.innerHeight;

    // Update the background color with the new opacity
    nav.style.backgroundColor = `rgba(229, 231, 235, ${opacity})`;
    for (let i = 0; i < navLinks.length; i++) {
        const link = navLinks[i];
        const iopacity = 1 - opacity*2;
        const color = Math.round(iopacity * 255);
        link.style.color = `rgba(${color},${color}, ${color}, 1)`;
    }
});
