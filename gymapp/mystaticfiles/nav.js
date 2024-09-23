
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
