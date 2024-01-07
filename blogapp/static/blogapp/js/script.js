// Get all the article-card elements
const specialtyCards = document.querySelectorAll(".article-card");

// Loop through each article-card and swap the positions of specialty_content and img if the row is odd
specialtyCards.forEach((card, index) => {
  if (index % 2 !== 0) {
    // Check if the row is odd (index is zero-based)
    const container = card.querySelector(".article-card-container");
    const content = card.querySelector(".article-card-content");
    const img = card.querySelector(".article_img_container");

    // Swap the positions
    container.insertBefore(img, content);
  }
});
document.addEventListener("DOMContentLoaded", function () {
  var spans = document.querySelectorAll("span");

  spans.forEach(function (span) {
    console.log(span);
    span.removeAttribute("style");
  });
});
