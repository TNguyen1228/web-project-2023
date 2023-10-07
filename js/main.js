'use strict';

const header = document.querySelector('header');
const nav = document.querySelector('nav');
const navbarMenuBtn = document.querySelector('.navbar-menu-btn');

const navbarForm = document.querySelector('.navbar-form');
const navbarFormCloseBtn = document.querySelector('.navbar-form-close');
const navbarSearchBtn = document.querySelector('.navbar-search-btn');


function navIsActive() {
  header.classList.toggle('active');
  nav.classList.toggle('active');
  navbarMenuBtn.classList.toggle('active');
}

navbarMenuBtn.addEventListener('click', navIsActive);

const searchBarIsActive = () => {
  return navbarForm.classList.toggle('active');
};

navbarSearchBtn.addEventListener('click', searchBarIsActive);
navbarFormCloseBtn.addEventListener('click', searchBarIsActive);


/* add filter */

document.getElementById("genre-filter").addEventListener("change", function() {
  var selectedGenre = this.value;
  var movieCards = document.querySelectorAll(".movie-card");

  movieCards.forEach(function(card) {
      var cardGenres = card.querySelector(".genre").classList;

      if (selectedGenre === "all" || cardGenres.contains(selectedGenre)) {
          card.style.display = "block";
      } else {
          card.style.display = "none";
      }
  });
});