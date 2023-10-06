$(document).ready(function() {
    $('#userForm').submit(function(event) {
      event.preventDefault(); // Prevent the form from submitting normally
  
      var formData = $(this).serialize(); // Serialize form data
  
      $.ajax({
        type: 'POST',
        url: 'process.php', // PHP script that will handle the data
        data: formData,
        success: function(response) {
          // Handle the response from the server, e.g., display a success message
          console.log(response);
        }
      });
    });
  });
  