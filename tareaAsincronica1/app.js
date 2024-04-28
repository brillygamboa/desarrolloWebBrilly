document.addEventListener('DOMContentLoaded', function() {
    // Change navbar color when scrolling
    window.addEventListener('scroll', function() {
      if (window.scrollY > 50) {
        document.querySelector('.navbar').classList.add('scroll');
      } else {
        document.querySelector('.navbar').classList.remove('scroll');
      }
    });
  });