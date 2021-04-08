const preloader = document.querySelector(".page-preloader");
const bootstrapColors = [
  "primary",
  "danger",
  "info",
  "success",
  "warning",
  "secondary",
  "light",
  "dark",
];

preloader
  .querySelector(".spinner-border")
  .classList.add(`text-${bootstrapColors[Math.floor(Math.random() * 8)]}`);

document.addEventListener("DOMContentLoaded", function () {
  setTimeout(() => (preloader.style.display = "none"), 600);
});
