const myButton = document.getElementById("myButton");
const loading = document.getElementById("loading");
const text = document.getElementById("text");
const result = document.getElementById("result");

myButton.addEventListener("click", () => {
  loading.classList.remove("hidden");
  setTimeout(() => {
    loading.classList.add("hidden");
    text.classList.remove("hidden");
    result.classList.remove("hidden");
    myButton.classList.add("hidden");
  }, 150000);
});
