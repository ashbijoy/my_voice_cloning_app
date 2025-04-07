// static/js/main.js

// This script adds a simple fade-in animation to the container when the page loads.
document.addEventListener('DOMContentLoaded', function () {
    const container = document.querySelector('.container');
    if (container) {
      container.style.opacity = 0;
      setTimeout(() => {
        container.style.transition = 'opacity 1s ease-in';
        container.style.opacity = 1;
      }, 100);
    }
    
    // You can add more interactivity or event listeners below.
    console.log("JavaScript loaded successfully!");
  });