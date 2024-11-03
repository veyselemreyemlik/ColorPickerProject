// Fotoğrafı Canvas'a yükleme ve renk tespiti
const imageLoader = document.getElementById("imageLoader");
const canvas = document.getElementById("imageCanvas");
const ctx = canvas.getContext("2d");
const colorCode = document.getElementById("colorCode");

// Fotoğraf yüklendiğinde göster
imageLoader.addEventListener("change", function (e) {
  const reader = new FileReader();
  reader.onload = function (event) {
    const img = new Image();
    img.onload = function () {
      canvas.width = img.width;
      canvas.height = img.height;
      ctx.drawImage(img, 0, 0);
    };
    img.src = event.target.result;
  };
  reader.readAsDataURL(e.target.files[0]);
});

// Canvas üzerinde tıklanan noktadaki rengi al
canvas.addEventListener("click", function (event) {
  const rect = canvas.getBoundingClientRect();
  const x = event.clientX - rect.left;
  const y = event.clientY - rect.top;
  const imgData = ctx.getImageData(x, y, 1, 1).data;
  const rgb = `rgb(${imgData[0]}, ${imgData[1]}, ${imgData[2]})`;
  colorCode.innerText = rgb;
});
