// Initialize tooltips for elements with a title attribute
// Requires tippy.js to be loaded on the page.
// This script will upgrade any element that has a `title` attribute
// into a nicer tooltip while preserving accessibility.
document.addEventListener('DOMContentLoaded', function () {
  if (window.tippy) {
    tippy('[title]');
  }
});
