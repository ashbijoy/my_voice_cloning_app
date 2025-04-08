// static/js/main.js

document.addEventListener('DOMContentLoaded', () => {
  const mainContainer = document.querySelector('.main-container');
  
  // Initially add the "hidden" class if not already set in HTML
  if (mainContainer) {
    mainContainer.classList.add('hidden');
    
    // Use a small timeout to trigger CSS transition
    setTimeout(() => {
      mainContainer.classList.remove('hidden');
      mainContainer.classList.add('animate');
    }, 100);
  }
  
  console.log("Advanced light-themed UI loaded.");
});