
function setCookie(name, value, days) {
  let expires = "";
  if (days) {
      const date = new Date();
      date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
      expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

document.querySelectorAll('input[name="duration"]').forEach(input => {
  input.addEventListener('change', function () {
    if (this.checked) { // Ensure this input is the one selected
      setCookie('planDuration', this.value); // Save to localStorage
      console.log("Saved plan duration:", this.value, 1); // Debugging message
    }
  });
});

// Store the selected class and its value
document.querySelectorAll('input[name="clas"]').forEach(input => {
    input.addEventListener('change', function () {
      setCookie('selectedClass', this.value, 1);  // Save selected class to local storage
    });
});

document.querySelectorAll('input[name="plan"]').forEach(input => {
  input.addEventListener('change', function () {
    setCookie('selectedplan', this.value, 1);  // Save selected class to local storage
  });
});






document.addEventListener('DOMContentLoaded', () => {
  const changePlanButton = document.getElementById('change_plan');
  const selectPlan = document.querySelector('.select_plan');
  const icon = changePlanButton.querySelector('.fa-chevron-down');

  changePlanButton.addEventListener('click', (e) => {
    e.preventDefault();
    selectPlan.classList.toggle('visible');
    icon.classList.toggle('rotate-icon');
  });
});
