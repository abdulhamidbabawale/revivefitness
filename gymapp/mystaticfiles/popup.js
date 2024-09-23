const openbtn = document.getElementById("openlogin");
const closebtn = document.getElementById("closelogin");
const modal = document.getElementById("login_box");

openbtn.addEventListener("click",() =>{
modal.classList.add("open");
});
closebtn.addEventListener("click",() =>{
  modal.classList.remove("open");
});
