**Julo**

This a new way to organize your purchases

Reminds:
- Setting up the sign up page
- Set form.py       

<!-- JS Plugins Init. -->
<script>
  (function() {
    window.onload = function () {
      // INITIALIZATION OF BOOTSTRAP VALIDATION
      // =======================================================
      HSBsValidation.init('.js-validate', {
        onSubmit: data => {
          data.event.preventDefault()
          alert('Submited')
        }
      })


      // INITIALIZATION OF TOGGLE PASSWORD
      // =======================================================
      new HSTogglePassword('.js-toggle-password')


      // INITIALIZATION OF SELECT
      // =======================================================
      HSCore.components.HSTomSelect.init('.js-select')
    }
  })()
</script>
# Julo
