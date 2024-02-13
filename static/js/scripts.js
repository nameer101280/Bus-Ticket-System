document.addEventListener("DOMContentLoaded", function() {
    // Add event listener to form submission
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission behavior
        
        // Get the bus ID and seat number from the form
        const busId = document.getElementById('bus_id').value;
        const seatNumber = document.getElementById('seat_number').value;
        
        // Example: Perform client-side validation (you can add more validation as needed)
        if (!busId || !seatNumber) {
            alert('Please fill in all fields.');
            return;
        }
        
        // Example: Display a confirmation message
        alert(`Ticket booked successfully!\nBus ID: ${busId}\nSeat Number: ${seatNumber}`);
        
        // Reset the form after submission
        form.reset();
    });
});

let lastScrollTop = 0;

window.addEventListener("scroll", function() {
    let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

    if (currentScroll > lastScrollTop) {
        // Scroll down
        document.getElementById("mainNavbar").classList.add("navbar-hidden");
    } else {
        // Scroll up
        document.getElementById("mainNavbar").classList.remove("navbar-hidden");
    }
    lastScrollTop = currentScroll;
});
