dz = this
document
  .getElementById('upload-btn-bar')
  .addEventListener('click', function handler(e) {
    dz.processQueue()
  })
