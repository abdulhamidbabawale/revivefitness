document.querySelectorAll('input[name="duration"]').forEach(input => {
  input.addEventListener('change', function () {
    if (this.checked) { // Ensure this input is the one selected
      localStorage.setItem('planDuration', this.value); // Save to localStorage
      console.log("Saved plan duration:", this.value); // Debugging message
    }
  });
});

// Store the selected class and its value
document.querySelectorAll('input[name="clas"]').forEach(input => {
    input.addEventListener('change', function () {
        localStorage.setItem('selectedClass', this.value);  // Save selected class to local storage
    });
});
