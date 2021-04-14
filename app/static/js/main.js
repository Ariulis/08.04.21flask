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
const formPreviewButton = document.querySelector(".form-preview button");
const indexPageForm = document.querySelector(".index-page .form");

if (formPreviewButton) {
  formPreviewButton.addEventListener("click", function () {
    formPreviewButton.parentElement.style.display = "none";
    indexPageForm.style.display = "block";
  });
}

preloader
  .querySelector(".spinner-border")
  .classList.add(`text-${bootstrapColors[Math.floor(Math.random() * 8)]}`);

document.addEventListener("DOMContentLoaded", function () {
  setTimeout(() => (preloader.style.display = "none"), 600);
});
