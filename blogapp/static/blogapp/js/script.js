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
// document.addEventListener("DOMContentLoaded", function () {
//   var spans = document.querySelectorAll("span");

//   spans.forEach(function (span) {
//     console.log(span);
//     span.removeAttribute("style");
//   });
// });
function searchFunction() {
  let input, filter, articles, preview, title, i, txtValue;
  input = document.getElementById("search");
  filter = input.value.toUpperCase();
  articles = document.getElementsByClassName("article-preview");
  noResultsMsg = document.getElementById("no-results-msg");

  var foundArticles = false;
  for (i = 0; i < articles.length; i++) {
    preview = articles[i];
    title = preview.getElementsByClassName("article-preview-title")[0];
    txtValue = title.textContent || title.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      preview.style.display = "";
      foundArticles = true;
    } else {
      preview.style.display = "none";
    }
  }
  noResultsMsg.style.display = foundArticles ? "none" : "block";
}
