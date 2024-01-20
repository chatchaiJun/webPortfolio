// function openImageSlider(projectTitle, projectId) {
//   const imageSliderContainer = document.getElementById("imageSliderContainer");
//   const imageSliderModal = document.getElementById("imageSliderModal");

//   // Make an AJAX request to fetch project pictures
//   const xhr = new XMLHttpRequest();
//   xhr.onreadystatechange = function () {
//     if (xhr.readyState === XMLHttpRequest.DONE) {
//       if (xhr.status === 200) {
//         const pictures = JSON.parse(xhr.responseText).pictures;

//         // Build HTML for image slider
//         let html = "";
//         pictures.forEach((picture) => {
//           html += `<img src="${picture.image_url}" alt="${projectTitle}" class="slider-image" />`;
//         });

//         imageSliderContainer.innerHTML = html;

//         // Show the modal
//         imageSliderModal.style.display = "block";
//       } else {
//         console.error("Failed to fetch project pictures");
//       }
//     }
//   };

//   const url = `/get_project_pictures/${projectId}/`;
//   xhr.open("GET", url);
//   xhr.send();
// }

// function closeImageSlider() {
//   document.getElementById("imageSliderModal").style.display = "none";
// }
function openImageSlider(projectTitle, projectId) {
  const imageSliderContainer = document.getElementById("imageSliderContainer");
  const imageSliderModal = document.getElementById("imageSliderModal");
  const closeBtn = document.getElementsByClassName("close")[0];

  // Make an AJAX request to fetch project pictures
  const xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        const pictures = JSON.parse(xhr.responseText).pictures;

        // Build HTML for image slider
        let html = "";
        pictures.forEach((picture) => {
          html += `<div class="slider-item"><img src="${picture.image_url}" alt="${projectTitle}" class="slider-image" /></div>`;
        });

        imageSliderContainer.innerHTML = html;

        // Show the modal
        imageSliderModal.style.display = "block";

        // Initialize the slider
        initSlider();
      } else {
        console.error("Failed to fetch project pictures");
      }
    }
  };

  const url = `/get_project_pictures/${projectId}/`;
  xhr.open("GET", url);
  xhr.send();
}

function initSlider() {
  const imageSliderContainer = document.getElementById("imageSliderContainer");
  const sliderItems = document.querySelectorAll(".slider-item");
  let currentIndex = 0;

  function showSlide(index) {
    sliderItems.forEach((item, i) => {
      item.style.display = i === index ? "block" : "none";
    });
  }

  showSlide(currentIndex);

  document.getElementById("prevBtn").addEventListener("click", function () {
    currentIndex = (currentIndex - 1 + sliderItems.length) % sliderItems.length;
    showSlide(currentIndex);
  });

  document.getElementById("nextBtn").addEventListener("click", function () {
    currentIndex = (currentIndex + 1) % sliderItems.length;
    showSlide(currentIndex);
  });
}

function closeImageSlider() {
  document.getElementById("imageSliderModal").style.display = "none";
}
