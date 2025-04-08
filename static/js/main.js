// static/js/main.js

document.addEventListener('DOMContentLoaded', () => {
  const container = document.querySelector('.main-container');
  if (container) {
    container.style.opacity = 0;
    setTimeout(() => {
      container.style.transition = 'opacity 1s ease-in';
      container.style.opacity = 1;
    }, 100);
  }
  console.log("Page loaded with light-themed UI.");
});