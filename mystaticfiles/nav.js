
function showSidebar() {
  const sidebar = document.querySelector('.sidebar')
  sidebar.style.display = 'flex'
  const cancel = document.querySelector('#cancel')
  cancel.style.display = 'flex'
  const btn = document.querySelector('#btn')
  btn.style.display = 'none'
}
function hideSidebar() {
  const sidebar = document.querySelector('.sidebar')
  sidebar.style.display = 'none'
  const btn = document.querySelector('#btn')
  btn.style.display = 'flex'
  const cancel = document.querySelector('#cancel')
  cancel.style.display = 'none'

}

  document.addEventListener('DOMContentLoaded', function () {
    var toastElList = [].slice.call(document.querySelectorAll('.toast'))
    var toastList = toastElList.map(function (toastEl) {
      return new bootstrap.Toast(toastEl, { autohide: true, delay: 5000 })  // Customize delay as needed
    })
    toastList.forEach(toast => toast.show())  // Show all toasts automatically
  });

