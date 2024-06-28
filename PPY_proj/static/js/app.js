


var buttons = document.querySelectorAll('.dropdown button');

// Loop through each button and attach click event listener
buttons.forEach(function(button) {
    button.addEventListener('click', function() {
        var dropdownContent = this.nextElementSibling;
        dropdownContent.classList.toggle("show");
    });
});


// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropdown button, .dropdown button *')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}


function openNavf() {
  document.getElementById("note-sidenav").style.display = "block";
  document.getElementById("openNav").style.display = "none";
  document.getElementById("exit").style.display = "none";
  document.getElementById("newNote").style.display = "none";

  document.getElementById("header-container").classList.add('col-9');
  document.getElementById("header-container").classList.remove('col-12');
}

function closeNavf() {
  document.getElementById("note-sidenav").style.display = "none";
  document.getElementById("openNav").style.display = "block";
  document.getElementById("exit").style.display = "block";
  document.getElementById("newNote").style.display = "block";

  document.getElementById("header-container").classList.add('col-12');
  document.getElementById("header-container").classList.remove('col-9');
}

document.getElementById("closeNav").addEventListener("click", closeNavf)
document.getElementById("openNav").addEventListener("click", openNavf)


$(document).ready(function() {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    let csrftoken = getCookie('csrftoken');
    $('.selectNote').click(function() {
        let divText = $('#editor').val();
        
        console.log(divText + "---gjbkkhjgjkhbjbkbjk")
        $.ajax({
            type: 'POST',
            url: '/get-div-text/',
            data: {
                'div_text': divText,
                'object_id': objectId,
                'csrfmiddlewaretoken': csrftoken
            }
        });
    });
});


$(document).ready(function() {
    // Toggle visibility of content inside item-container
    $('.changeNoteName').click(function() {
        let container = $(this).closest('.note');
        container.find('.item-content').toggleClass('hide');
    });
});






  
